from rest_framework.response import Response

from accounts.serializers import UserSerializer
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework_jwt.views import ObtainJSONWebToken

class JSONWebTokenAPIOverride(ObtainJSONWebToken):
    """
    Override JWT
    """
    user_serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        response = super(JSONWebTokenAPIOverride, self).post(
            request, *args, **kwargs)
        if response:
            if response and response.status_code == status.HTTP_200_OK:
                token = response.data.get('token')
                user = User.objects.filter(
                    email=request.data['email']).first()

                response.data = {
                    "status": 200,
                    "message": "Login Successfully",
                    "data": {
                        "access_token": token,
                        "user_id": user.id,
                        "full_name": user.get_full_name(),
                        "email_id": user.email,
                        # "profile_picture": get_site(request) + user.profile.profile_picture.url if user.profile and user.profile.profile_picture else '',
                    }
                }
            else:
                if response.data and response.data.get('non_field_errors'):
                    response.data = {
                        "status": 404,
                        "message": str(response.data.get('non_field_errors')[0]),
                        "data": {}
                    }
                else:
                    response.data = {
                        "status": 404,
                        "message": "Email and Password must not be empty",
                        "data": {}
                    }
            return response
        else:
            response = {
                "status": 404,
                "message": "Something wrong happened",
                "data": {}
            }
            return Response(response)

