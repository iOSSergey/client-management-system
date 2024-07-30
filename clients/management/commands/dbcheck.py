# clients/management/commands/dbcheck.py
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    help = 'Checks the database connection'

    def handle(self, *args, **kwargs):
        try:
            with connections['default'].cursor() as cursor:
                cursor.execute("SELECT 1")
            self.stdout.write(self.style.SUCCESS('Successfully connected to the database'))
        except OperationalError as e:
            self.stdout.write(self.style.ERROR(f'Error connecting to the database: {e}'))
