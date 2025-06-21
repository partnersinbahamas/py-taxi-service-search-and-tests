from django.test import TestCase
from ..models import Manufacturer


class TestManufacturerModel(TestCase):
    def setUp(self):
        self.created_manufacturer = Manufacturer.objects.create(
            name="Manufacturer-1",
            country="Country-1",
        )

    def test_manufacturer_creation(self):
        manufacturer = Manufacturer.objects.first()

        self.assertEqual(
            manufacturer.name,
            self.created_manufacturer.name
        )

        self.assertEqual(
            manufacturer.country,
            self.created_manufacturer.country
        )

    def test_manufacturer_str_method(self):
        self.assertTrue(
            str(self.created_manufacturer),
            f"{self.created_manufacturer.name} "
            f"{self.created_manufacturer.country}"
        )
