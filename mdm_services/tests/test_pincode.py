from django.urls import reverse
from mdm_services.models.city_model import City
from mdm_services.models.country_model import Country
from mdm_services.models.pincode_model import Pincode
from mdm_services.models.state_model import State
from rest_framework import status
from rest_framework.test import APITestCase


class PincodeUrlTestCase(APITestCase):
    def test_pincode_search_api(self):
        response = self.client.post("/get_pincode")
        self.assertEquals(response.status_code, 200)

    def test_if_data_is_correct(self):

        search_dict = {
            "pincode": 405010,
            "search_text": 0,
        }
        response = self.client.post("/get_pincode",search_dict)
        self.assertEqual(response.status_code, 200)


class PincodeViewTestCase(APITestCase):
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
        city = City.objects.create(
            name="delhi",
            search_tag="dilli,delhi",
            creation_by="yamini",
            status=1,
            updation_by="yamini",
        )
        Pincode.objects.bulk_create(
            [
                Pincode(
                    value=110001,
                    creation_by="yamini",
                    serviceable=1,
                    updation_by="yamini",
                    status=1,
                ),
                Pincode(
                    value=801101,
                    creation_by="yamini",
                    serviceable=1,
                    updation_by="yamini",
                    status=1,
                ),
                Pincode(
                    value=212011,
                    creation_by="yamini",
                    serviceable=1,
                    updation_by="yamini",
                    status=1,
                ),
            ]
        )

    def test_pincodeView(self):
        response = self.client.post(reverse("get_pincode"), {"search_query": 10})
        result = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(
            len(result), Pincode.objects.filter(value__icontains=10).count()
        )
