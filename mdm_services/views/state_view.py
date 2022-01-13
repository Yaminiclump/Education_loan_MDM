import json
import logging
from types import SimpleNamespace

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

from mdm_services.error_code import errors
from mdm_services.services.state_service import get_state_service, search_state_service

logger = logging.getLogger("django")


@csrf_exempt
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={"country_id": openapi.Schema(type=openapi.TYPE_NUMBER, description="country id"), },
    ),
    operation_id="payload",
)
@api_view(["POST"])
def get_state(request):
    response_obj = None
    try:
        logger.info("request: %s", request.body)

        if request.method == "POST":
            data = json.loads(request.body.decode("utf-8"), object_hook=lambda d: SimpleNamespace(**d))
            response_obj = get_state_service(data)
        else:
            logger.info("Invalid request method: %s", request.method)
            response_obj = {"error_code": errors.invalid_request["error_code"], "message": errors.invalid_request["message"]}

    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"], "message": errors.generic_error_2["message"]}

    logger.info("response: %s", response_obj)
    return JsonResponse(response_obj, safe=False)


@csrf_exempt
@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["search_text"],
        properties={"search_text": openapi.Schema(type=openapi.TYPE_STRING, description="search tag/text"),},
    ),
    operation_id="payload",
)
@api_view(["POST"])
def search_state(request):
    response_obj = None
    try:
        logger.info("request: %s", request.body)

        if request.method == "POST":
            search_query = json.loads(request.body.decode("utf-8"), object_hook=lambda d: SimpleNamespace(**d))
            response_obj = search_state_service(search_query)
        else:
            logger.info("Invalid request method: %s", request.method)
            response_obj = {"error_code": errors.invalid_request["error_code"], "message": errors.invalid_request["message"]}
    except Exception as e:
        logger.exception("Exception: ")
        response_obj = {"error_code": errors.generic_error_2["error_code"], "message": errors.generic_error_2["message"]}

    logger.info("response: %s", response_obj)
    return JsonResponse(response_obj, safe=False)
