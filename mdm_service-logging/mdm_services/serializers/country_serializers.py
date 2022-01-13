from rest_framework import serializers

from mdm_services.models.country_model import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'
        
