from rest_framework import serializers

from libs.constants import Constants


class AddElevatorSerializer(serializers.Serializer):

    name = serializers.CharField()
    is_operational = serializers.BooleanField(default=True)
    status = serializers.ChoiceField(choices=Constants.ElevatorStatus.list())
    