from src.helpers.errors.controller_errors import MissingParameters, WrongParameterType
from src.helpers.http_status_code import HttpStatusCode
from src.modules.get_week_classes.get_week_classes_usecase import GetWeekClassesUsecase
from src.modules.get_week_classes.get_week_classes_viewmodel import WeekClassesViewModel, ClassViewModel
from src.helpers.http_models import HttpRequest, HttpResponse, OK
from src.helpers.errors.domain_errors import NoItemsFound


class GetWeekClassesController:

    def __init__(self, usecase: GetWeekClassesUsecase):
        self._getWeekClassesUsecase = usecase

    async def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get('ra') is None or request.query_params.get('ra') == "":
                raise MissingParameters('ra')

            if type(request.query_params.get('ra')) is not str:
                raise WrongParameterType('ra', type(request.query_params.get('ra')), str)

            classes = await self._getWeekClassesUsecase(request.query_params.get('ra'))

            classesVm = [ClassViewModel(_class) for _class in classes]

            weekClassesVm = WeekClassesViewModel(classesVm)

            return OK(weekClassesVm.toDict())

        except MissingParameters as e:
            return HttpResponse(
                status_code=HttpStatusCode.BAD_REQUEST.value,
                body={"erro": e.message}
            )

        except WrongParameterType as e:
            return HttpResponse(
                status_code=HttpStatusCode.BAD_REQUEST.value,
                body={"erro": e.message}
            )

        except NoItemsFound as e:
            return HttpResponse(
                status_code=HttpStatusCode.NO_CONTENT.value,
                body={"erro": e.message}
            )

        except Exception as err:
            return HttpResponse(
                status_code=HttpStatusCode.INTERNAL_SERVER_ERROR.value,
                body={"erro": str(err)}
            )