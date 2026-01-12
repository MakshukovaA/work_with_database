import csv
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from decimal import Decimal
from phones.models import Phone

class Command(BaseCommand):
    help = 'Imports phones from a CSV file.'

    def handle(self, *args, **options):
        csv_file_path = os.path.join(settings.BASE_DIR, 'phones.csv')

        if not os.path.exists(csv_file_path):
            self.stderr.write(self.style.ERROR('CSV file not found: %s' % csv_file_path))
            return

        count = 0
        try:
            with open(csv_file_path, encoding='utf-8') as file:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    name = (row.get('name') or '').strip()
                    image = (row.get('image') or row.get('image_url') or '').strip()
                    price_str = row.get('price') or '0'
                    release_date_str = row.get('release_date') or ''
                    lte_exists_str = row.get('lte_exists') or row.get('lte') or 'false'

                    if not name:
                        continue

                    try:
                        price = Decimal(price_str)
                    except Exception:
                        price = Decimal('0')

                    release_date = None
                    if release_date_str:
                        release_date = parse_date(release_date_str)

                    is_active = str(lte_exists_str).strip().lower() in ('true', '1', 'yes', 'y', 'on')

                    Phone.objects.update_or_create(
                        name=name,
                        defaults={
                            'image': image,
                            'price': price,
                            'release_date': release_date,
                            'lte_exists': is_active,
                        }
                    )
                    count += 1

                self.stdout.write(self.style.SUCCESS(
                    'Successfully imported %d phones from %s' % (count, csv_file_path)
                ))
                except FileNotFoundError:
                self.stderr.write(self.style.ERROR('Error: The file "%s" was not found.' % csv_file_path))
            except Exception as e:
            self.stderr.write(self.style.ERROR('An error occurred: %s' % str(e)))