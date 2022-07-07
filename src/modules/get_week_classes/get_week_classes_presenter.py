import os

from src.helpers.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.infra.repositories.class_repository_dynamo import ClassRepositoryDynamo
from src.infra.repositories.class_repository_mock import ClassRepositoryMock
from .get_week_classes_usecase import GetWeekClassesUsecase
from .get_week_classes_controller import GetWeekClassesController
from ...envs import Envs


async def lambda_handler(event, context):

    repo = ClassRepositoryMock() if Envs.IsMock() else ClassRepositoryDynamo()
    usecase = GetWeekClassesUsecase(repo)
    controller = GetWeekClassesController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = await controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
