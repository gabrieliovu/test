import factory
from . import models


class PersonFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    industry = factory.Faker('word')
    email = factory.Sequence(lambda n: 'person{}@example.com'.format(n))
    date_of_birth = factory.Faker('past_date', start_date='-19y')
    salary = factory.Faker('pyfloat', right_digits=2, min_value=0, max_value=1000)
    years_of_experience = factory.Faker('pyint', min_value=1, max_value=27)

    class Meta:
        model = models.Person
