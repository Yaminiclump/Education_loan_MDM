from django.urls import reverse
from mdm_services.models.city_model import City
from mdm_services.models.country_model import Country
from mdm_services.models.state_model import State
from rest_framework import status
from rest_framework.test import APITestCase


class CityUrlTestCase(APITestCase):
    def test_city_search_api(self):
        response = self.client.post("/search_city")
        self.assertEqual(response.status_code, 200)

    def test_if_data_is_correct(self):

        search_dict = {
            "name": "begusarai",
            "search_text": "a",
        }
        response = self.client.post("/search_city",search_dict)
        self.assertEqual(response.status_code, 200)


class CityViewTest(APITestCase):
    def setUp(self):
        country = Country.objects.create(
            name="india",
            search_tag="india,bharat",
            serviceable=1,
            creation_by="yamini",
            status=1,
            updation_by="yamini",
        )
        state = State.objects.create(
            name="bihar",
            search_tag="bihar,patna",
            creation_by="yamini",
            status=1,
            updation_by="yamini",
            country=country,
        )
        City.objects.bulk_create(
            [
                City(
                    name="patna",
                    search_tag="patna,patliputra",
                    creation_by="yamini",
                    updation_by="yamini",
                    status=1,
                    state=state,
                ),
                City(
                    name="begusarai",
                    search_tag="begusarai,barauni",
                    creation_by="yamini",
                    updation_by="yamini",
                    status=1,
                    state=state,
                ),
            ]
        )

    def test_cityView(self):
        response = self.client.post(reverse("search_city"), {"search_text": "patli"})
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(result),
            City.objects.filter(search_tag__icontains="ra").filter(status=1).count(),
        )
