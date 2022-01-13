from django.urls import reverse
from mdm_services.models.country_model import Country
from rest_framework import status
from rest_framework.test import APITestCase


class CountryUrlTestCase(APITestCase):
    def test_country_search_api(self):
        response = self.client.post("/search_country")
        self.assertEquals(response.status_code, 200)

    def test_if_data_is_correct(self):

        search_dict = {
            "name": "india",
            "search_text": "a",
        }
        response = self.client.post("/search_country",search_dict)
        self.assertEqual(response.status_code, 200)


class CountryViewTest(APITestCase):
    def setUp(self):
        Country.objects.bulk_create(
            [
                Country(
                    name="india",
                    search_tag="india,bharat",
                    serviceable=1,
                    creation_by="yamini",
                    status=1,
                    updation_by="yamini",
                ),
                Country(
                    name="china",
                    search_tag="china",
                    serviceable=1,
                    creation_by="yamini",
                    status=1,
                    updation_by="yamini",
                ),
                Country(
                    name="USA",
                    search_tag="USA,america",
                    serviceable=1,
                    creation_by="yamini",
                    status=1,
                    updation_by="yamini",
                ),
            ]
        )

    def test_countryView(self):
        response = self.client.post(reverse("search_country"), {"search_query": "in"})
        result = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            len(result), Country.objects.filter(search_tag__icontains="in").count()
        )
