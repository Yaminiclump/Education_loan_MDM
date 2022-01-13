import logging

from django.db.models import Q

from mdm_services.error_code import errors
from mdm_services.models.empty_class import EmptyClass
from mdm_services.models.pincode_model import Pincode
from mdm_services.services.city_service import city_by_id_service
from mdm_services.services.country_service import country_by_id_service
from mdm_services.services.state_service import state_by_id_service

logger = logging.getLogger("django")


def get_pincode_service(req_data):
    response_obj = None
    try:
        logger.info("request data: %s", req_data)
        if req_data:

            try:
                pincode = req_data.pincode
            except AttributeError:
                pincode = None

            if pincode:
                pincode_data = Pincode.objects.filter(value=pincode).filter(status=1)
                if pincode_data:
                    logger.debug("pincode_data: %s", pincode_data)
                    data = list(pincode_data.values("id", "value", "city_id", "serviceable"))

                    logger.debug("data[0]: %s", data[0])
                    logger.debug("data[0], city_id: %s", data[0]["city_id"])
                    city_id=data[0]["city_id"]
                    logger.debug("city_id: %s", city_id)

                    city_req_data = EmptyClass()
                    city_req_data.city_id = city_id
                    city_data = city_by_id_service(city_req_data)
                    logger.debug("city_data: %s", city_data)
                    logger.debug("city_data actual: %s", city_data["data"])

                    state_req_data = EmptyClass()
                    state_req_data.state_id = city_data["data"]["state_id"]
                    logger.debug("state_id: %s", state_req_data.state_id)
                    state_data = state_by_id_service(state_req_data)
                    logger.debug("state_data: %s", state_data)
                    logger.debug("state_data actual: %s", state_data["data"])

                    country_req_data = EmptyClass()
                    country_req_data.country_id = state_data["data"]["country_id"]
                    logger.debug("country_req_data: %s", country_req_data.country_id)
                    country_data = country_by_id_service(country_req_data)
                    logger.debug("country_data: %s", country_data)
                    logger.debug("country_data actual: %s", country_data["data"])

                    pincode_resp_data = {"pincpode": data[0], "city" : city_data["data"],
                                         "state" : state_data["data"], "country" : country_data["data"]}

                    logger.debug("pincodeRespData: %s", pincode_resp_data)
                    response_obj = {
                        "error_code": errors.success["error_code"],
                        "message": errors.success["message"],
                        "data": pincode_resp_data
                    }

                else:
                    response_obj = {
                        "error_code": errors.pincode_error_1["error_code"],
                        "message": errors.pincode_error_1["message"],
                    }
            else:
                response_obj = {
                    "error_code": errors.generic_error_1["error_code"],
                    "message": errors.generic_error_1["message"],
                }
        else:
            response_obj = {
                "error_code": errors.generic_error_1["error_code"],
                "message": errors.generic_error_1["message"],
            }
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {
            "error_code": errors.generic_error_2["error_code"],
            "message": errors.generic_error_2["message"],
        }
    logger.info("response_obj: %s", response_obj)
    return response_obj

