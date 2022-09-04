from rest_framework import authentication
from rest_framework import exceptions
import jwt
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from django.utils.timezone import make_aware

from libs.app_logger import AppLogger

logger = AppLogger(tag="AUTHENTICATION")


class JWTUser(object):
    def __init__(self, payload, user_id, name, role_id, phone_number):
        self.payload = payload
        self.is_authenticated = True
        self.id = user_id
        self.username = name
        self.user_id = user_id
        self.name = name
        self.role_id = role_id
        self.phone_number = phone_number


class JWTAuthentication(authentication.BaseAuthentication):
    """
    Overriding default authenticate to provide jwt Authentication
    """

    def authenticate(self, request):

        authorization_token = request.headers.get('Authorization')

        if not authorization_token:
            logger.debug("No Auth authorization_token")
            raise Unauthorized("Authorization token required")

        payload = self.validate_token(authorization_token)
        user_payload = payload.get(settings.JWT_USER_KEY)
        user_id = user_payload.get("user_id")
        user_name = user_payload.get("name")
        role_id = user_payload.get("role")
        phone_number = user_payload.get("phone_number")
        user = JWTUser(user_payload, user_id, user_name, role_id, phone_number)
        return (user, None)

    def validate_token(self, token):
        try:
            logger.info("Validating Token")
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)
            if payload.get('exp'):
                logger.info("Checking Expiry")
                self.check_exp(payload.get('exp'))
            return payload
        except Exception as e:
            logger.debug(str(e))
            logger.debug("Invalid JWT")
            raise Unauthorized('Invalid JWT')

    def check_exp(self, exp_time):
        if make_aware(datetime.fromtimestamp(exp_time)) <= timezone.now():
            logger.debug("Expired JWT")
            raise Unauthorized('Expired JWT')


class Unauthorized(exceptions.APIException):
    status_code = 401
    default_code = "unauthorized"
    default_detail = "Unauthorized"



