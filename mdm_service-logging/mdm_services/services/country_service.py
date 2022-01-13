import logging

from django.db.models import Q

from mdm_services.error_code import errors
from mdm_services.models.country_model import Country

logger = logging.getLogger("django")


def country_by_id_service(req_data):

    response_obj = None
    try:
        logger.info("request data: %s", req_data)
        if req_data:
            try:
                country_id = req_data.country_id
            except AttributeError:
                country_id = None

            if country_id:
                country_id = Country.objects.filter(id=country_id).filter(status=1)
                if country_id:
                    data = list(country_id.values("id", "name", "serviceable"))
                    response_obj = {"error_code": errors.success["error_code"], "message": errors.success["message"],
                                    "data": data[0]}
                else:
                    response_obj = {"error_code": errors.country_error_1["error_code"], "message": errors.country_error_1["message"]}
            else:
                response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}
        else:
            response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"], "message": errors.generic_error_2["message"]}

    logger.info("response_obj: %s", response_obj)
    return response_obj


def country_list_service():

    response_obj = None
    try:
        logger.info("request data: not required")
        data = list(Country.objects.values("id", "name", "serviceable").filter(status=1))
        response_obj = {"error_code": errors.success["error_code"], "message": errors.success["message"], "data": data}
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"], "message": errors.generic_error_2["message"]}

    logger.info("response_obj: %s", response_obj)
    return response_obj


def search_country_service(req_data):

    response_obj = None
    try:
        logger.info("request data: %s", req_data)
        if req_data:

            try:
                search_text = req_data.search_text
                search_text = search_text.lower()
            except AttributeError:
                search_text = None

            if search_text:
                search_text = search_text.lower()
                country_data = Country.objects.filter(Q(search_tag__contains=search_text)).filter(status=1)
                if country_data:
                    data = list(country_data.values("id", "name", "serviceable"))
                    response_obj = {"error_code": errors.success["error_code"], "message": errors.success["message"], "data": data}

                else:
                    response_obj = {"error_code": errors.country_error_1["error_code"], "message": errors.country_error_1["message"]}
            else:
                response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}
        else:
            response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"], "message": errors.generic_error_2["message"]}

    logger.info("response_obj: %s", response_obj)
    return response_obj
