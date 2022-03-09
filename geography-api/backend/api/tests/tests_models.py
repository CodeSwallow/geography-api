from django.test import TestCase
from api.models import USState

# Create your tests here.
class USTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        USState.objects.create(name="Alabama", nickname="The Cotton State or the Heart of Dixie")
        USState.objects.create(name="Alaska", nickname="The Great Land, Land of the Midnight Sun")
        cls.stateAL = USState.objects.get(name="Alabama")
        cls.stateAK = USState.objects.get(name="Alaska")

    def test_str(self):
        self.assertEqual(str(self.stateAL), "Alabama, The Cotton State or the Heart of Dixie")
        self.assertEqual(str(self.stateAK), "Alaska, The Great Land, Land of the Midnight Sun")
