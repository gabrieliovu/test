from rest_framework.test import APITestCase
from rest_framework import status
from users.factories import PersonFactory
from users.models import Person


class PersonListTestCase(APITestCase):
    _RESOURCE_URL = '/api/users/'

    def setUp(self):
        super().setUp()
        Person.objects.all().delete()
        self.p1 = PersonFactory(salary=3.01, first_name='Gabriel', last_name='Iovu', industry='IT', 
                                email='test1@gmail.com')
        self.p2 = PersonFactory(salary=2.02, first_name='Nothing', last_name='Here', industry='IT1', 
                                email='test2@gmail.com')
        self.p3 = PersonFactory(salary=1.03, first_name='More', last_name='Tosee', industry='IT2',  
                                email='test3@gmail.com')

    def test_list(self):
        resp = self.client.get(self._RESOURCE_URL)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['count'], 3)
        self.assertDictEqual(dict(resp.data['results'][0]), 
                             {'id': self.p1.id, 
                              'first_name': self.p1.first_name,
                              'last_name': self.p1.last_name, 
                              'email': self.p1.email, 
                              'gender': self.p1.gender,
                              'date_of_birth': self.p1.date_of_birth.strftime("%Y-%m-%d"), 
                              'industry': self.p1.industry, 
                              'salary': str(self.p1.salary), 
                              'years_of_experience': self.p1.years_of_experience
                              }
                             )
    
    def test_sorting(self):
        resp = self.client.get(self._RESOURCE_URL + '?ordering=salary')

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['results'][0]['id'], self.p3.id)
        self.assertEqual(resp.data['results'][1]['id'], self.p2.id)
        self.assertEqual(resp.data['results'][2]['id'], self.p1.id)
        
    def test_pagination(self):
        resp = self.client.get(self._RESOURCE_URL + '?page_size=1')

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 1)
        
    def test_filter_query(self):
        resp = self.client.get(self._RESOURCE_URL + '?query=gabr')

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 1)
        
    def test_filter_industry(self):
        resp = self.client.get(self._RESOURCE_URL + '?industry=IT')

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['results']), 1)


class PersonRetrieveTestCase(APITestCase):
    _RESOURCE_URL = '/api/users/{}/'

    def setUp(self):
        super().setUp()
        Person.objects.all().delete()
        self.p1 = PersonFactory()

    def test_retrieve(self):
        resp = self.client.get(self._RESOURCE_URL.format(self.p1.id))

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertDictEqual(resp.data,
                             {'id': self.p1.id,
                              'first_name': self.p1.first_name,
                              'last_name': self.p1.last_name,
                              'email': self.p1.email,
                              'gender': self.p1.gender,
                              'date_of_birth': self.p1.date_of_birth.strftime('%Y-%m-%d'),
                              'industry': self.p1.industry,
                              'salary': str(self.p1.salary),
                              'years_of_experience': self.p1.years_of_experience
                              }
                             )


class PersonDeleteTestCase(APITestCase):
    _RESOURCE_URL = '/api/users/{}/'

    def setUp(self):
        super().setUp()
        Person.objects.all().delete()
        self.p1 = PersonFactory()
        self.p2 = PersonFactory()
        
    def test_delete(self):
        resp = self.client.delete(self._RESOURCE_URL.format(self.p1.id))

        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.first().id, self.p2.id)


class PersonUpdateTestCase(APITestCase):
    _RESOURCE_URL = '/api/users/{}/'

    def setUp(self):
        super().setUp()
        Person.objects.all().delete()
        self.p1 = PersonFactory()

    def test_update(self):
        resp = self.client.patch(self._RESOURCE_URL.format(self.p1.id), 
                                 data={"first_name": "No more Gabriel"})

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.first().first_name, 'No more Gabriel')
        
    def test_update_bad_email(self):
        resp = self.client.patch(self._RESOURCE_URL.format(self.p1.id), 
                                 data={"email": "No more Gabriel"})

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(resp.data, {'email': ['Enter a valid email address.']})
        
    def test_update_bad_gender(self):
        resp = self.client.patch(self._RESOURCE_URL.format(self.p1.id), 
                                 data={"gender": "G"})

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(resp.data, {'gender': ['"G" is not a valid choice.']})
