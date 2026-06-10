import re

class InvalidEmailError(ValueError):
    pass

class UnderageError(ValueError):
    pass

class RegistrationService:

    def register_user(self, email: str, age: int) -> bool:

        if not email or email.strip() == "":
            raise InvalidEmailError("Email must not be empty or null.")

        pattern = r"^[^@]+@[^@]+\.[^@]+$"

        if not re.match(pattern, email):
            raise InvalidEmailError(
                f"'{email}' is not a valid email address."
            )

        if age < 18:
            raise UnderageError(
                f"User must be at least 18 years old. Got: {age}."
            )

        assert isinstance(email, str) and len(email) > 0, \
            "Email invariant check failed."

        return True