from django.test import TestCase
from ..forms import ManufacturerSearchForm


class TestManufacturerSearchForm(TestCase):
    def test_manufacturer_search_form_with_value(self):
        form_data = {
            "name": "V-1"
        }

        form = ManufacturerSearchForm(form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], form_data["name"])

    def test_manufacturer_search_form_without_value(self):
        form_data = {
            "name": ""
        }

        form = ManufacturerSearchForm(form_data)
        self.assertTrue(form.is_valid())
