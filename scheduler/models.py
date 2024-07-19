from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100)
    app_start_time_utc_s = models.IntegerField()

    def save(self, *args, **kwargs):
        max_seconds = 24 * 60 * 60
        self.app_start_time_utc_s = self.app_start_time_utc_s % max_seconds
        super().save(*args, **kwargs)

    @staticmethod
    def get_current_time_in_seconds():
        now = timezone.now()
        current_time_in_seconds = (now.hour * 3600 + now.minute * 60 + now.second) % (24 * 3600)
        return current_time_in_seconds

    def is_on(self):
        current_time_utc_s = self.get_current_time_in_seconds()
        if self.app_start_time_utc_s > current_time_utc_s:
            if abs(self.app_start_time_utc_s - current_time_utc_s) > 8 * 60 * 60:
                return True
            else:
                return False
        else:
            if abs(current_time_utc_s - self.app_start_time_utc_s) < 16 * 60 * 60:
                return True
            else:
                return False
