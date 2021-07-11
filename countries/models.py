from uuid import uuid4

from django.db import models
from django.contrib.gis.db import models as gis_models


class Country(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    name = models.TextField(blank=True)
    country_code = models.TextField(blank=True)
    geometry = gis_models.MultiPolygonField(blank=True)

    class Meta:
        db_table = "countries"
