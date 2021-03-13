from django.db import IntegrityError
from django.test import TestCase
from demo.models import Movie


class IntegrityTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(name="run lola run", movie_id=1)

    def test_duplicate(self):
        created = False
        try:
            Movie.objects.create(name="run lola run", movie_id=1)
            created = True
        except IntegrityError:
            pass
        self.assertEqual(created, False, 'No duplicate titles')
