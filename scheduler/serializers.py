from rest_framework import serializers
from scheduler.models import Client


class SchedulerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'name', 'app_start_time_utc_s']


class StatusSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'name', 'app_start_time_utc_s', 'status']

    @staticmethod
    def get_status(obj):
        return obj.is_on()
