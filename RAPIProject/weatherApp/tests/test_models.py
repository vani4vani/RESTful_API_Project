from django.test import TestCase
from ..models import WeatherData

# Create your tests here.

class WeatherTest(TestCase):
    """ Test module for WeatherData model """

    def setUp(self):
        WeatherData.objects.create(
            country = "wales", month_or_season = "FEB", year = 2018, reading_type = "Rainfall")
            # name='Casper', age=3, breed='Bull Dog', color='Black')
        WeatherData.objects.create(
            country = "england", month_or_season = "JAN", year = 2017, reading_type = "Rainfall")
            # name='Muffin', age=1, breed='Gradane', color='Brown')

    def test_weather_results(self):
        england_weather = WeatherData.objects.get(country = "wales")
        wales_weather = WeatherData.objects.get(country = "england")
    #     self.assertEqual(
    #         puppy_casper.get_breed(), "Casper belongs to Bull Dog breed.")
    #     self.assertEqual(
    #         puppy_muffin.get_breed(), "Muffin belongs to Gradane breed.")
