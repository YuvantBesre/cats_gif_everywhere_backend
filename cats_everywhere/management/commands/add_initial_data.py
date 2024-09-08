from django.core.management.base import BaseCommand, CommandError
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
import requests

class Command(BaseCommand):
    help = "Add Initial Data"

    def handle(self, *args, **options):
        from cats_everywhere.models import CatData
        data = [
            {
                'title' : 'Bill of Lading',
                'image' : 'https://neox-development-s3.s3.ap-south-1.amazonaws.com/beautiful-cats-exotic-cat-breed.avif',
                'position' : 0
            },
            {
                'title' : 'Bank Draft',
                'image' : 'https://neox-development-s3.s3.ap-south-1.amazonaws.com/beautiful-cats-birman-breed_kknMEwO.avif',
                'position' : 0
            },
            {
                'title' : 'Invoice',
                'image' : 'https://neox-development-s3.s3.ap-south-1.amazonaws.com/beautiful-cats-american-shorthair_mb4Z0kS.avif',
                'position' : 0
            },
            {
                'title' : 'Bank Draft 2',
                'image' : 'https://neox-development-s3.s3.ap-south-1.amazonaws.com/beautiful-cat-bengal_DMJCIE5.avif',
                'position' : 0
            },
            {
                'title' : 'Bill of Lading 2',
                'image' : 'https://neox-development-s3.s3.ap-south-1.amazonaws.com/beautiful-cats-exotic-cat-breed.avif',
                'position' : 0
            },
        ]
        CatData.objects.all().delete()
        for aData in data:
            response = requests.get(aData['image'])
            if response.status_code == 200:
                temp_file = NamedTemporaryFile(delete=True)
                temp_file.write(response.content)
                temp_file.flush()

                instance = CatData.objects.create(
                    title = aData['title'],
                    position = aData['position']
                )
                instance.image.save(aData['image'].split('https://neox-development-s3.s3.ap-south-1.amazonaws.com/')[1], File(temp_file), save=True)

                self.stdout.write(
                    self.style.SUCCESS('Created record!')
                )