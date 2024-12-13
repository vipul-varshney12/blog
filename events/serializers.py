from rest_framework import serializers
from .models import Event, Registration, Venue

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def validate_date(self, value):
        from datetime import date
        if value < date.today():
            raise serializers.ValidationError("Event date must be in the future.")
        return value


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'
