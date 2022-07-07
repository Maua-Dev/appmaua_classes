from datetime import time, timezone, timedelta

from src.domain.entities._class import Class
from src.domain.entities.professor import Professor
from src.domain.entities.subject import Subject
from src.domain.enums.week_days_enum import WeekDayEnum
from src.domain.enums.class_type_enum import ClassTypeEnum
from src.domain.enums.degree_enum import DegreeEnum
from src.infra.dtos.class_dynamo_dto import ClassDynamoDTO


class TestClassDynamoDTO:

    def test_dynamo_to_entity(self):
        data = {
            'dayOfWeek': 4,
            'degreeCode': 'ECM',
            'initTime': "07:40:00.000000-03:00",
            'professor': {
                'email': 'rodrigomangoninicola@maua.br',
                'name': 'Rodrigo Mangoni Nicola',
                'phoneNumber': '11940028922'
            },
            'endTime': "09:20:00.000000-03:00",
            'studentRA': '21004765',
            'subjectCode': 'ECM404',
            'subjectName': 'Estrutura de Dados e Técnicas de Programação',
            'classType': 1,
            'classValue': 2,
            'place': "U12"
        }

        classDTO = ClassDynamoDTO.fromDynamo(data)

        expected = Class(initTime=time(7, 40, 0, 0, timezone(timedelta(hours=-3))),
                         endTime=time(9, 20, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.SEXTA,
                         subject=Subject(code="ECM404", name="Estrutura de Dados e Técnicas de Programação",
                                         professor=Professor(name="Rodrigo Mangoni Nicola",
                                                             email="rodrigomangoninicola@maua.br",
                                                             phoneNumber="11940028922")),
                         place="U12", classType=ClassTypeEnum.TURMA, classValue=2, degree=DegreeEnum.ECM)

        assert classDTO.toEntity() == expected

    def test_entity_to_dto_to_entity(self):
        _class = Class(initTime=time(7, 40, 0, 0, timezone(timedelta(hours=-3))),
                       endTime=time(9, 20, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.SEXTA,
                       subject=Subject(code="ECM404", name="Estrutura de Dados e Técnicas de Programação",
                                       professor=Professor(name="Rodrigo Mangoni Nicola",
                                                           email="rodrigomangoninicola@maua.br",
                                                           phoneNumber="11940028922")),
                       place="U12", classType=ClassTypeEnum.TURMA, classValue=2, degree=DegreeEnum.ECM)
        data = ClassDynamoDTO.fromEntity(_class)

        parsedClass = data.toEntity()

        assert parsedClass == _class

    def test_entity_to_dynamo(self):
        expected = {
            'dayOfWeek': 4,
            'degreeCode': 'ECM',
            'initTime': "07:40:00.000000-03:00",
            'professor': {
                'email': 'rodrigomangoninicola@maua.br',
                'name': 'Rodrigo Mangoni Nicola',
                'phoneNumber': '11940028922'
            },
            'endTime': "09:20:00.000000-03:00",
            'studentRA': '21004765',
            'subjectCode': 'ECM404',
            'subjectName': 'Estrutura De Dados E Técnicas De Programação',
            'classType': 1,
            'classValue': 2,
            'place': "U12"
        }

        entity = Class(initTime=time(7, 40, 0, 0, timezone(timedelta(hours=-3))),
                       endTime=time(9, 20, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.SEXTA,
                       subject=Subject(code="ECM404", name="Estrutura de Dados e Técnicas de Programação",
                                       professor=Professor(name="Rodrigo Mangoni Nicola",
                                                           email="rodrigomangoninicola@maua.br",
                                                           phoneNumber="11940028922")),
                       place="U12", classType=ClassTypeEnum.TURMA, classValue=2, degree=DegreeEnum.ECM)

        classDTO = ClassDynamoDTO.fromEntity(entity)

        parsedClass = classDTO.toDynamo("21004765")

        assert parsedClass == expected
