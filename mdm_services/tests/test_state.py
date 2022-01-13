from django.urls import reverse
from mdm_services.models.country_model import Country
from mdm_services.models.state_model import State
from rest_framework import status
from rest_framework.test import APITestCase


class StateUrlTestCase(APITestCase):
    def test_state_search_api(self):
        response = self.client.post("/search_state")
        self.assertEquals(response.status_code, 200)

    def test_if_data_is_correct(self):

        search_dict = {
            "name": "bihar",
            "search_text": "a",
        }
        response = self.client.post("/search_state",search_dict)
        self.assertEqual(response.status_code, 200)


class StateViewTestCase(APITestCase):
    def setUp(self):
        country = Country.objects.create(
            name="india",
            search_tag="india,bharat",
            serviceable=1,
            creation_by="yamini",
            status=1,
            updation_by="yamini",
        )
        State.objects.bulk_create(
            [
                State(
                    name="Himachal",
                    search_tag="Himachal,HP",
                    creation_by="yamini",
                    updation_by="yamini",
                    status=1,
                    country=country,
                ),
                State(
                    name="delhi",
                    search_tag="delhi,dilli",
                    creation_by="yamini",
                    updation_by="yamini",
                    status=1,
                    country=country,
                ),
                State(
                    name="bihar",
                    search_tag="patna,bihar",
                    creation_by="yamini",
                    updation_by="yamini",
                    status=1,
                    country=country,
                ),
            ]
        )

    def test_stateView(self):
        response = self.client.post(reverse("search_state"), {"search_query": "hi"})
        result = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            len(result), State.objects.filter(search_tag__icontains="hi").count()
        )
