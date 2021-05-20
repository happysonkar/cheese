from django.db import models
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField


class Cheese(TimeStampedModel):
    name=models.CharField("Name of the cheese",max_length=255)
    slug=AutoSlugField("Cheese Address",unique=True,always_update=False,populate_from="name")
    description=models.TextField("Description",blank=True)
    class Firmness(models.TextChoices):
        UNSPECIFIED="unspecified","UNSPECIFIED"
        SOFT="soft","SOFT"
        SEMI_SOFT="semi-soft","SEMI-SOFT"
        SEMI_HARD="semi-hard","SEMI-HARD"
        HARD="hard","HARD"

    firmness=models.CharField("Firmness",max_length=20,choices=Firmness.choices,default=Firmness.UNSPECIFIED)
    def __str__(self):
        return self.name