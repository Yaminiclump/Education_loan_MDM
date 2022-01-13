import logging

from django.db.models import Q

from mdm_services.error_code import errors
from mdm_services.models.state_model import State

logger = logging.getLogger("django")


def state_by_id_service(req_data):

    response_obj = None
    try:
        logger.info("request data: %s", req_data)
        if req_data:
            try:
                state_id = req_data.state_id
            except AttributeError:
                logger.exception("Exception: ")
                state_id = None

            if state_id:
                state_data = State.objects.filter(id=state_id).filter(status=1)
                if state_data:
                    data = list(state_data.values("id", "name", "status", "country_id"))
                    response_obj = {"error_code": errors.success["error_code"], "message": errors.success["message"],
                                    "data": data[0]}
                else:
                    response_obj = {"error_code": errors.state_error_1["error_code"], "message": errors.state_error_1["message"]}
            else:
                response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}
        else:
            response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"], "message": errors.generic_error_2["message"]}

    logger.info("response_obj: %s", response_obj)
    return response_obj


def get_state_service(req_data):

    response_obj = None
    try:
        logger.info("request data: %s", req_data)
        if req_data:

            try:
                country_id = req_data.country_id
            except AttributeError:
                country_id = None

            if country_id:
                state_data = State.objects.filter(country__id=country_id).filter(status=1)
                if state_data:
                    data = list(state_data.values("id", "name", "status", "country_id"))
                    response_obj = {"error_code": errors.success["error_code"], "message": errors.success["message"], "data": data}
                else:
                    response_obj = {"error_code": errors.state_error_1["error_code"], "message": errors.state_error_1["message"]}
            else:
                response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}
        else:
            response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"], "message": errors.generic_error_2["message"]}

    logger.info("response_obj: %s", response_obj)
    return response_obj


def search_state_service(req_data):

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
                state_data = State.objects.filter(Q(search_tag__contains=search_text)).filter(status=1)
                if state_data:
                    data = list(state_data.values("id", "name", "status", "country_id"))
                    response_obj = {"error_code": errors.success["error_code"], "message": errors.success["message"], "data": data}
                else:
                    response_obj = {"error_code": errors.state_error_1["error_code"], "message": errors.state_error_1["message"]}
            else:
                response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}
        else:
            response_obj = {"error_code": errors.generic_error_1["error_code"], "message": errors.generic_error_1["message"]}

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"], "message": errors.generic_error_2["message"]}

    logger.info("response_obj: %s", response_obj)
    return response_obj
