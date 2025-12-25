import csv
import os
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils import timezone
from work_with_database.settings import BASE_DIR

APP_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(APP_DIR)
APP_DIR = os.path.dirname(APP_DIR)

class Command(BaseCommand):
    help = 'Imports phones from a CSV file.'

    def handle(self, *args, **options):
        csv_file_path = os.path.join(APP_DIR, 'phones.csv')

        try:
            with open(csv_file_path, encoding='utf-8') as file:
                # ... ваш код ...
                self.stdout.write(self.style.SUCCESS('Successfully imported phones from %s' % csv_file_path))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR('Error: The file "%s" was not found.' % csv_file_path))
        except Exception as e:
            self.stderr.write(self.style.ERROR('An error occurred: %s' % str(e)))