from rest_framework import serializers

from mdm_services.models.state_model import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields='__all__'
