import pytest

from registration_service import (
    RegistrationService,
    InvalidEmailError,
    UnderageError
)

@pytest.fixture
def service():
    return RegistrationService()


def test_successful_registration(service):
    assert service.register_user(
        "alice@example.com",
        25
    ) is True


def test_empty_email_raises_error(service):
    with pytest.raises(InvalidEmailError):
        service.register_user("", 22)


def test_none_email_raises_error(service):
    with pytest.raises(InvalidEmailError):
        service.register_user(None, 22)


def test_invalid_email_format(service):
    with pytest.raises(InvalidEmailError):
        service.register_user("not-an-email", 22)


def test_email_missing_domain(service):
    with pytest.raises(InvalidEmailError):
        service.register_user("user@", 22)


def test_underage_user_raises_error(service):
    with pytest.raises(UnderageError):
        service.register_user(
            "bob@example.com",
            16
        )


def test_minimum_valid_age(service):
    assert service.register_user(
        "charlie@example.com",
        18
    ) is True


def test_zero_age_raises_error(service):
    with pytest.raises(UnderageError):
        service.register_user(
            "dave@example.com",
            0
        )