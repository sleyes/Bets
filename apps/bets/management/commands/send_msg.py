# /apps/game/management/commands
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        print "Hola Mundo "
        print args
        print options
