from rest_framework import serializers

from mdm_services.models.pincode_model import Pincode


class PincodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pincode
        fields='__all__'
