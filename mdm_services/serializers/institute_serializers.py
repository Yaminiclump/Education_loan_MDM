from rest_framework import serializers

from mdm_services.models.institute_model import Institute


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Institute
        fields='__all__'
