import pytest

from src.domain.entities.subject import Subject
from src.domain.entities.professor import Professor
from src.helpers.errors.domain_errors import EntityError


class Test_Subject:

    def test_subject(self):
        subject = Subject(code="ECM401", name="Banco de dados",
                          professor=Professor(name="Aparecido Freitas", email="aparecido@email.com",
                                              phoneNumber="999999999"))

        assert subject.name == "Banco De Dados"

    def test_subject_entity_error1(self):
        with pytest.raises(EntityError):
            Subject(code="", name="Banco de dados",
                    professor=Professor(name="Aparecido Freitas", email="aparecido@email.com",
                                        phoneNumber="999999999"))

    def test_subject_entity_error2(self):
        with pytest.raises(EntityError):
            Subject(code="ECM401", name="",
                    professor=Professor(name="Aparecido Freitas", email="aparecido@email.com",
                                        phoneNumber="999999999"))
