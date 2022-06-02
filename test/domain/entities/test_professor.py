import pytest

from src.domain.entities.professor import Professor
from src.helpers.errors.domain_errors import EntityError


class Test_Professor:

    def test_professor(self):
        prof = Professor("Ana paula Gonçalves serra",
                         "ana.serra@maua.br",
                         "99999-9999")

        assert prof.name == "Ana Paula Gonçalves Serra"
        assert prof.email == "ana.serra@maua.br"
        assert prof.phoneNumber == "99999-9999"

    def test_professor_entity_error1(self):
        with pytest.raises(EntityError):
            Professor('',
                      'email@teste.com',
                      '99999-9999')

    def test_professor_entity_error2(self):
        with pytest.raises(EntityError):
            Professor('Ana Paula Gonçalves Serra',
                      '',
                      '99999-9999')

    def test_professor_entity_error3(self):
        with pytest.raises(EntityError):
            Professor('Ana Paula Gonçalves Serra',
                      'email@teste.com',
                      '')
