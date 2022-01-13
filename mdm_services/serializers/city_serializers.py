from rest_framework import serializers

from mdm_services.models.city_model import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields='__all__'
