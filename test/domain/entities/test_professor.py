import pytest

from src.domain.entities.professor import Professor
from src.helpers.errors.domain_errors import EntityError


class Test_Professor:

    def test_professor(self):
        prof = Professor(name="Ana paula Gonçalves serra",
                         email="ana.serra@maua.br",
                         phoneNumber="99999-9999")

        assert prof.name == "Ana Paula Gonçalves Serra"
        assert prof.email == "ana.serra@maua.br"
        assert prof.phoneNumber == "99999-9999"

    def test_professor_entity_error1(self):
        with pytest.raises(EntityError):
            Professor(name='',
                      email='email@teste.com',
                      phoneNumber='99999-9999')

    def test_professor_entity_error2(self):
        with pytest.raises(EntityError):
            Professor(name='Ana Paula Gonçalves Serra',
                      email='',
                      phoneNumber='99999-9999')

    def test_professor_entity_error3(self):
        with pytest.raises(EntityError):
            Professor(name='Ana Paula Gonçalves Serra',
                      email='email@teste.com',
                      phoneNumber='')
