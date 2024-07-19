from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from scheduler.models import Client
from django.utils import timezone

from scheduler.serializers import SchedulerSerializer, StatusSerializer


class SchedulerViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = SchedulerSerializer

    @action(
        detail=False,
        methods=["GET"],
        url_path="status",
        serializer_class=StatusSerializer,
    )
    def status(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
