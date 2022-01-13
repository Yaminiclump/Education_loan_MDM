from django.urls import reverse
from mdm_services.models.city_model import City
from mdm_services.models.institute_model import Institute
from rest_framework import status
from rest_framework.test import APITestCase


class InstituteUrlTestCase(APITestCase):
    def test_institute_search_api(self):
        response = self.client.post("/search_institute")
        self.assertEquals(response.status_code, 200)

    def test_if_data_is_correct(self):

        search_dict = {
            "name": "banaras university",
            "search_text": "a",
        }
        response = self.client.post("/search_institute",search_dict)
        self.assertEqual(response.status_code, 200)


class InstituteViewTest(APITestCase):
    def setUp(self):
        city = City.objects.create(
            name="delhi",
            search_tag="delhi,dilli",
            creation_by="yamini",
            status=1,
            updation_by="yamini",
        )

        Institute.objects.bulk_create(
            [
                Institute(
                    name="delhi university",
                    search_tag="du",
                    serviceable=1,
                    creation_by="yamini",
                    status=1,
                    updation_by="yamini",
                ),
                Institute(
                    name="vellore university",
                    search_tag="vit",
                    serviceable=1,
                    creation_by="yamini",
                    status=1,
                    updation_by="yamini",
                ),
                Institute(
                    name="hindu university",
                    search_tag="hu",
                    serviceable=1,
                    creation_by="yamini",
                    status=1,
                    updation_by="yamini",
                ),
            ]
        )

    def test_instituteView(self):
        response = self.client.post(reverse("search_institute"), {"search_query": "hi"})
        result = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            len(result), Institute.objects.filter(search_tag__icontains="u").count()
        )
