from .models import *
from rest_framework import serializers


class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class RequestParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestParticipant
        fields = '__all__'