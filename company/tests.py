from django.test import TestCase
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APIClient


class TestCompany(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_company_employess(self):
        company = baker.make('company.Company')
        detail_path = reverse('company:company-employees', args=(company.id, ))
        response = self.client.get(detail_path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
