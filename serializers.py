from rest_framework import serializers
import pytz

class EventSerializer(serializers.Serializer):
    summary = serializers.CharField()
    ApplicationId = serializers.IntegerField()
    location = serializers.CharField()
    description = serializers.CharField(required=False, default='_________')
    colorId = serializers.IntegerField(default=7)
    start_date = serializers.DateField()
    start_time = serializers.TimeField()
    end_date = serializers.DateField()
    end_time = serializers.TimeField()
    recurrence = serializers.ListField(default="RRULE:FREQ=DAILY;COUNT=1")
    attendees = serializers.CharField()

class UpdateSerializer(serializers.Serializer):
    summary = serializers.CharField(required=False)
    ApplicationId = serializers.IntegerField(required=False)
    location = serializers.CharField(required=False)
    description = serializers.CharField(required=False, default='_________')
    colorId = serializers.IntegerField(default=7, required=False)
    start_date = serializers.DateField(required=False)
    start_time = serializers.TimeField(required=False)
    end_date = serializers.DateField(required=False)
    end_time = serializers.TimeField(required=False)
    recurrence = serializers.ListField(default="RRULE:FREQ=DAILY;COUNT=1", required=False)
    attendees = serializers.CharField(required=False)




    

    











