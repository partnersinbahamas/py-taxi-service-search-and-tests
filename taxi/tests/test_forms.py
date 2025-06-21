from django.contrib.auth import get_user_model
from django.test import TestCase
from ..forms import ManufacturerSearchForm, CarSearchForm, CarForm
from ..models import Manufacturer, Driver


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


class TestCarSearchForm(TestCase):
    def test_driver_search_form_with_value(self):
        form_data = {
            "model": "M-1"
        }

        form = CarSearchForm(form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["model"], form_data["model"])

    def test_driver_search_form_without_value(self):
        form_data = {
            "model": ""
        }

        form = CarSearchForm(form_data)

        self.assertTrue(form.is_valid())


class TestCarForm(TestCase):
    def test_form_field_valid(self):
        created_drivers = get_user_model().objects.bulk_create(
            [
                Driver(
                    username="D-1",
                    password="d-1-password",
                    license_number="JIM26531"
                ),
                Driver(
                    username="D-2",
                    password="d-2-password",
                    license_number="DOM26531"
                ),
            ],
        )

        form_data = {
            "model": "M-1",
            "manufacturer": Manufacturer.objects.create(
                name="M-1",
                country="C-1"
            ),
            "drivers": created_drivers
        }

        form = CarForm(form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["model"], form_data["model"])
        self.assertEqual(
            form.cleaned_data["manufacturer"],
            form_data["manufacturer"]
        )
        self.assertEqual(
            list(form.cleaned_data["drivers"]),
            list(created_drivers)
        )
