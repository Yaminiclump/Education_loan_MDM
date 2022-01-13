import json
import logging
from types import SimpleNamespace

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

from mdm_services.error_code import errors
from mdm_services.services.institute_service import get_institute_service, search_institute_service

logger = logging.getLogger("django")


@csrf_exempt
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={"city_id": openapi.Schema(type=openapi.TYPE_NUMBER, description="city id"), },
    ),
    operation_id="payload",
)
@api_view(["POST"])
def get_institute(request):

    response_obj = None
    try:
        logger.info("request: %s", request.body)

        if request.method == "POST":
            data = json.loads(request.body.decode("utf-8"), object_hook=lambda d: SimpleNamespace(**d))
            response_obj = get_institute_service(data)

        else:
            logger.info("Invalid request method: %s", request.method)
            response_obj = {"error_code": errors.invalid_request["error_code"],
                            "message": errors.invalid_request["message"]}

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"],
                        "message": errors.generic_error_2["message"]}

    logger.info("response: %s", response_obj)
    return JsonResponse(response_obj, safe=False)


@csrf_exempt
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["search_text", "city_id"],
        properties={"search_text": openapi.Schema(type=openapi.TYPE_STRING, description="search tag/text"),
                    "city_id": openapi.Schema(type=openapi.TYPE_NUMBER, description="city id"),},
    ),
    operation_id="payload",
)
@api_view(["POST"])
def search_institute(request):

    response_obj = None
    try:
        logger.info("request: %s", request.body)

        if request.method == "POST":
            data = json.loads(request.body.decode("utf-8"), object_hook=lambda d: SimpleNamespace(**d))
            response_obj = search_institute_service(data)

        else:
            logger.info("Invalid request method: %s", request.method)
            response_obj = {"error_code": errors.invalid_request["error_code"],
                            "message": errors.invalid_request["message"]}

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"],
                        "message": errors.generic_error_2["message"]}

    logger.info("response: %s", response_obj)
    return JsonResponse(response_obj, safe=False)


