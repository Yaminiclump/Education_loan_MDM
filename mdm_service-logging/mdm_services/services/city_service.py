import logging

from django.db.models import Q

from mdm_services.error_code import errors
from mdm_services.models.city_model import City

logger = logging.getLogger("django")


def city_by_id_service(req_data):

    response_obj = None
    try:
        logger.info("request data: %s", req_data)
        if req_data:
            try:
                city_id = req_data.city_id
            except AttributeError:
                logger.exception("Exception: ")
                city_id = None

            if city_id:
                city_data = City.objects.filter(id=city_id).filter(status=1)
                if city_data:
                    data = list(city_data.values("id", "name", "state_id"))
                    response_obj = {"error_code": errors.success["error_code"], "message": errors.success["message"],
                                    "data": data[0]}
                else:
                    response_obj = {"error_code": errors.city_error_1["error_code"], "message": errors.city_error_1["message"]}
            else:
                response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}
        else:
            response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"], "message": errors.generic_error_2["message"]}

    logger.info("response_obj: %s", response_obj)
    return response_obj


def get_city_service(req_data):

    response_obj = None
    try:
        logger.info("request data: %s", req_data)
        if req_data:

            try:
                state_id = req_data.state_id
            except AttributeError:
                state_id = None

            if state_id:
                city_data = City.objects.filter(state__id=state_id).filter(status=1)
                if city_data:
                    data = list(city_data.values("id", "name", "state_id"))
                    response_obj = {"error_code": errors.success["error_code"], "message": errors.success["message"], "data": data}
                else:
                    response_obj = {"error_code": errors.city_error_1["error_code"], "message": errors.city_error_1["message"]}
            else:
                response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}
        else:
            response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"], "message": errors.generic_error_2["message"]}

    logger.info("response_obj: %s", response_obj)
    return response_obj


def search_city_service(req_data):

    response_obj = None
    try:
        logger.info("request data: %s", req_data)
        if req_data:

            try:
                search_text = req_data.search_text
                search_text = search_text.lower()
            except AttributeError:
                logger.exception("exception")
                search_text = None

            logger.debug("search_text: %s", search_text)
            if search_text:
                city_data = City.objects.filter(search_tag__contains=search_text).filter(status=1)
                if city_data:
                   data = list(city_data.values("id", "name", "state_id"))
                   response_obj = {"error_code": errors.success["error_code"], "message": errors.success["message"], "data": data}
                else:
                    response_obj = {"error_code": errors.city_error_1["error_code"], "message": errors.city_error_1["message"]}
            else:
                response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}
        else:
            response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"], "message": errors.generic_error_2["message"]}

    logger.info("response_obj: %s", response_obj)
    return response_obj
