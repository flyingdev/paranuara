from django.test import TestCase
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient

from . import models


class TestPerson(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_person_detail(self):
        person = baker.make('person.Person')
        detail_path = reverse('person-detail', args=(person.id, ))
        response = self.client.get(detail_path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_mutual_friends(self):
        person_1 = baker.make('person.Person', has_died=False)
        person_2 = baker.make('person.Person', has_died=False, eye_color=models.Person.EYE_COLOR_BROWN)
        person_3 = baker.make('person.Person', has_died=False)
        person_4 = baker.make('person.Person', has_died=False)
        person_5 = baker.make('person.Person', has_died=False)
        person_6 = baker.make('person.Person', has_died=False)

        person_1.friends.add(person_2)
        person_1.friends.add(person_3)
        person_1.save()

        person_4.friends.add(person_2)
        person_4.friends.add(person_3)
        person_4.friends.add(person_5)
        person_4.friends.add(person_6)

        person_4.save()

        mutual_path = reverse('person-mutual-friends')
        persons = [person_1.id, person_4.id, ]
        response = self.client.post(mutual_path, data={
            'persons': persons,
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
