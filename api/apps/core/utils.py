from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.exceptions import ValidationError as RestValidationError
from rest_framework_simplejwt.tokens import RefreshToken


class JwtToken:
    @staticmethod
    def get_jwt_token(user) -> dict:
        """Generates a JWT token for the given user
        Args:
            user (User): The user object for which the token is generated.
        Returns:
            dict: A dictionary containing the access and refresh tokens.
        Raises:
            None
        """

        jtw_token = RefreshToken.for_user(user)
        response = {
            'access': str(jtw_token.access_token),
            'refresh': str(jtw_token)
        }
        return response


class Validate:
    @staticmethod
    def password_validation(raw_password):
        """
        Validates the given password according to the password validation rules.
        Args:
            raw_password (str): The password to be validated.
        Returns:
            None
        Raises:
            RestValidationError: If the password does not meet the validation criteria.
        Notes:
            - This method uses the `validate_password` function from an external module to perform password validation.
            - If the password does not meet the validation criteria, a `ValidationError` is raised and caught.
            - A `RestValidationError` is then raised with the original error message to provide a
                more specific error for the validation failure.
        """
        try:
            validate_password(raw_password)
        except ValidationError as error:
            raise RestValidationError(error)
