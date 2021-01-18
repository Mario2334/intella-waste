from rest_framework import serializers

from calendar_events.models import Event
from user.serializers import UserSerializer


class EventSerializer(serializers.ModelSerializer):
    guests=UserSerializer(required=False,many=True)
    class Meta:
        model = Event
        fields = "__all__"