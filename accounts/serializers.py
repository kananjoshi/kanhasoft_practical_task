from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import JSONWebTokenSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'id', 'email')

class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = 'email'

    def validate(self, attrs):
        success = False
        password = attrs.get("password")
        user_obj = User.objects.filter(email=attrs.get("email").lower()).first()

        if user_obj is not None:
            credentials = {
                'username': user_obj.username,
                'password': password
            }
            if all(credentials.values()):
                if user_obj:
                    payload = jwt_payload_handler(user_obj)

                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user_obj.username,
                    }
                else:
                    raise serializers.ValidationError("User Does Not Exist.")

            else:
                msg = 'Must include email and password'
                msg = msg.format(username_field=self.username_field)
                raise serializers.ValidationError(msg)

        else:
            msg = 'Account with this email does not exists'
            raise serializers.ValidationError(msg)