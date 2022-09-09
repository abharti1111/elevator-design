from rest_framework import generics
from rest_framework.response import Response

from elevator_app.v1.controllers.add_elevator_controller import AddElevatorController
from elevator_app.v1.serializers.add_elevator_serializer import AddElevatorSerializer
from libs.utils.generic_responses import generate_success_response


class AddElevator(generics.CreateAPIView):
    serializer_class = AddElevatorSerializer
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        AddElevatorController(**serializer.validated_data).add_elevator()

        return Response(generate_success_response())