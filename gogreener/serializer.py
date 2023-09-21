from rest_framework import serializers
from gogreener.models import *


class AppModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = gogreenerapp
        fields = ["seller_name", "store_name", "store_number", "email", "admin_share", "password", "select_city",
                  "delivery_range", "store_address", "select_id"]


LANGUAGE_CHOICES = (
    ('', '--select an option--'),
    ('English', 'English'),
    ('Tamil', 'Tamil'),
    ('Hindi', 'Hindi'),
    ('Malayalam', 'Malayalam'),
    ('Telugu', 'Telugu')
)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(label='Email Address', help_text='Enter Email Address')
    password = serializers.CharField(label="Password", help_text="Enter Your Password")
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES)
