import random
from django.test import TestCase
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient


class TestCompany(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_company_employees(self):
        company = baker.make('company.Company')
        baker.make('person.Person', company=company, _quantity=5)
        detail_path = reverse('company:company-employees', args=(company.id, ))
        response = self.client.get(detail_path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_company_404(self):
        company_id = random.randint(1, 1000)
        detail_path = reverse('company:company-employees', args=(company_id,))
        response = self.client.get(detail_path)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_empty_employees(self):
        company = baker.make('company.Company')
        detail_path = reverse('company:company-employees', args=(company.id,))
        response = self.client.get(detail_path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.json().get('employees')) == 0)
