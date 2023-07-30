import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        Phone.objects.all().delete()
        
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phones_row = Phone(
                name = phone['name'],
                price = phone['price'],
                image = phone['image'],
                release_date = phone['release_date'],
                lte_exists = phone['lte_exists'],
                slug = slugify(phone['name'])
            )
            phones_row.save()