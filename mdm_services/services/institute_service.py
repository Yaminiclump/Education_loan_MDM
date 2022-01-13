import logging

from django.db.models import Q

from mdm_services.error_code import errors
from mdm_services.models.institute_model import Institute

logger = logging.getLogger("django")


def get_institute_service(req_data):

    response_obj = None
    try:
        logger.info("request data: %s", req_data)
        if req_data:

            try:
                city_id = req_data.city_id
            except AttributeError:
                city_id = None

            if city_id:
                institute_data = Institute.objects.filter(city__id=city_id).filter(status=1)
                if institute_data:
                    data = list(institute_data.values("id", "name", "status", "university_id", "city_id",
                                                      "ranking", "ranking_source", "serviceable", "blacklisted"))

                    response_obj = {"error_code": errors.success["error_code"], "message": errors.success["message"],
                                    "data": data}

                else:
                    response_obj = {"error_code": errors.institute_error_1["error_code"],
                                    "message": errors.institute_error_1["message"]}
            else:
                response_obj = {"error_code": errors.generic_error_1["error_code"],
                                "message": errors.generic_error_1["message"]}
        else:
            response_obj = {"error_code": errors.generic_error_1["error_code"],
                            "message": errors.generic_error_1["message"]}
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {
            "error_code": errors.generic_error_2["error_code"],
            "message": errors.generic_error_2["message"],
        }

    logger.info("response_obj: %s", response_obj)
    return response_obj


def search_institute_service(req_data):
    response_obj = None
    try:
        if req_data:
            logger.info("request data %s", req_data)
            try:
                search_text = req_data.search_text
                search_text = search_text.lower()
            except AttributeError:
                search_text = None

            try:
                city_id = req_data.city_id
            except AttributeError:
                city_id = None

            logger.debug("city_id: %s, search_text: %s", city_id, search_text)

            institute_data = None
            if search_text:
                institute_data = Institute.objects.filter(Q(search_tag__contains=search_text)).filter(status=1)
            if city_id:
                logger.debug("institute_data: %s", institute_data)
                if institute_data:
                    institute_data = institute_data.filter(Q(city__id=city_id))
                else:
                    institute_data = Institute.objects.filter(Q(city__id=city_id))

            logger.debug("institute_data: %s", institute_data)
            if institute_data:
                data = list(institute_data.values("id", "name", "status", "university_id", "city_id",
                                                  "ranking", "ranking_source", "serviceable", "blacklisted"))
                response_obj = {"error_code": errors.success["error_code"], "message": errors.success["message"],
                                "data": data}

            else:
                response_obj = {"error_code": errors.institute_error_1["error_code"],
                                "message": errors.institute_error_1["message"]}

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {
            "error_code": errors.generic_error_2["error_code"],
            "message": errors.generic_error_2["message"],
        }

    logger.info("response_obj: %s", response_obj)
    return response_obj
