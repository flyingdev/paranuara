import json
import os
from django.conf import settings
from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from company import models


class Command(BaseCommand):
    help = 'Used to populate companies data'

    def add_arguments(self, parser: CommandParser):
        pass

    def handle(self, *args, **options):
        companies_json_path = os.path.join(settings.BASE_DIR, 'resources', 'companies.json')
        if not os.path.exists(companies_json_path):
            print('companies.json file does not exist')
            return

        with open(companies_json_path, 'rb') as fp:
            companies = json.load(fp)
            for company_data in companies:
                company = models.Company(id=company_data['index'], name=company_data['company'])
                company.save()
