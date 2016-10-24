from rest_framework import serializers
from api.models import Stops, Trips, Routes, StopTimes, Foo


"""
from api.models import Stops
from api.serializers import StopsSerializer
s=Stops.objects.get(stop_id='66666')
serializer=StopsSerializer(s)
serializer.data
"""

class FooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foo
        fields = ('route_short_name', 'trip_headsign', 'departure_time', 'delay')

class StopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stops
        fields = ('stop_code', 'stop_name', 'latitude', 'longitude')

class StopTimesSerializer(serializers.ModelSerializer):
    class Meta:
      model = StopTimes
      fields = ('arrival_time', 'departure_time')

class TripsSerializer(serializers.ModelSerializer):
    my_stop_times_trip_id=StopTimesSerializer(many=True, read_only=True);
    class Meta:
      model = Trips
      fields = ('trip_id', 'trip_headsign', 'trip_short_name', 'my_stop_times_trip_id')


class RoutesSerializer(serializers.ModelSerializer):
    my_trip_id=TripsSerializer(many=True, read_only=True);
    class Meta:
      model = Routes
      fields = ('route_long_name', 'route_short_name', 'my_trip_id')
      #fields = ('route_long_name', 'route_short_name')
      #fields = ('id', 'trip_id');

