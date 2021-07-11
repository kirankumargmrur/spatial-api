from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from countries.models import Country
from countries.serializer import CountrySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from django.db.models import Q
from django.http import JsonResponse
from django.db import connection
from django.core import serializers
from django.db.models import F
from django.contrib.gis.db.models.functions import Intersection
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point, Polygon


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100


class CountryCreate(generics.CreateAPIView):
    queryset = Country.objects.all(),
    serializer_class = CountrySerializer


class CountryList(generics.ListAPIView):
    model = Country
    serializer_class = CountrySerializer
    pagination_class = LargeResultsSetPagination
    context_object_name = 'search_api_results'
    search_fields = ['name', 'country_code']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['name']

    def get_queryset(self):
        query = self.request.GET.get("q")

        if query:
            return Country.objects.filter(
                Q(name__icontains=query) | Q(country_code__icontains=query)).distinct()

        return Country.objects.all()


class CountryDetail(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryUpdate(generics.RetrieveUpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDelete(generics.RetrieveDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class IntersectionView(generics.ListAPIView):
    serializer_class = CountrySerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        query = self.request.GET.get("country")

        if query:
            country = Country.objects.get(name=query)
            print(connection.queries)
            return Country.objects.filter(geometry__intersects=country.geometry)

        return Country.objects.all()


class IntersectionViewOfIndia(generics.ListAPIView):
    serializer_class = CountrySerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        country = Country.objects.get(name='India')

        return Country.objects.filter(geometry__intersects=country.geometry)
