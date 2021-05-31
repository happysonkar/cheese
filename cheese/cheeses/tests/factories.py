from django.template.defaultfilters import slugify

import factory
import factory.fuzzy
from ..models import Cheese

class CheeseFactory(factory.django.DjangoModelFactory):
    name=factory.fuzzy.FuzzyText()
    slug=factory.LazyAttribute(lambda obj: slugify(obj.name))
    description=factory.Faker('paragraph',nb_sentences=3)
    firmness=factory.fuzzy.FuzzyChoice([x[0] for x in Cheese.Firmness.choices])
    country_of_origin=factory.Faker('country_code')
    def __str__(self):
        return self.name

    class Meta:
        model=Cheese
