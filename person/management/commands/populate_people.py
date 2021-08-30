import json
import os
from typing import Dict
from dateutil import parser
from django.conf import settings
from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from company import models as comp_models
from person import models
from person import utils


class Command(BaseCommand):
    help = 'Used to populate people data'

    def add_arguments(self, parser: CommandParser):
        pass

    def _resolve_company(self, company_id: str) -> comp_models.Company:
        try:
            return comp_models.Company.objects.get(pk=company_id)
        except comp_models.Company.DoesNotExist:
            return None

    def _save_person(self, person_data: Dict) -> None:
        _id = person_data['_id']
        guid = person_data['guid']
        has_died = person_data['has_died']
        balance = utils.parse_money_str(person_data['balance'])
        picture = person_data['picture']
        age = person_data['age']
        name = person_data['name']
        gender = person_data['gender']
        company = self._resolve_company(person_data['company_id'])
        email = person_data['email']
        phone = person_data['phone']
        address = person_data['address']
        about = person_data['about']
        registered = parser.parse(person_data['registered'])
        tags = person_data['tags']
        greeting = person_data['greeting']
        fruits = utils.filter_fruits(person_data['favouriteFood'])
        vegetables = utils.filter_vegetables(person_data['favouriteFood'])

        person = models.Person(id=person_data['index'], _id=_id, guid=guid, has_died=has_died, balance=balance,
                               picture=picture, age=age, name=name, gender=gender, company=company, email=email,
                               phone=phone, address=address, about=about, registered=registered, tags=tags,
                               greeting=greeting, fruits=fruits, vegetables=vegetables)
        person.save()

    def _save_friends(self, person_data: Dict):
        person = models.Person.objects.get(pk=person_data['index'])
        for friend_id in person_data['friends']:
            friend = models.Person.objects.get(pk=friend_id['index'])
            person.friends.add(friend)

        person.save()

    def handle(self, *args, **options):
        people_json_path = os.path.join(settings.BASE_DIR, 'resources', 'people.json')
        if not os.path.exists(people_json_path):
            print('people.json file does not exist')
            return

        with open(people_json_path, 'rb') as fp:
            people = json.load(fp)
            for person_data in people:
                self._save_person(person_data)

            for person_data in people:
                self._save_friends(person_data)
