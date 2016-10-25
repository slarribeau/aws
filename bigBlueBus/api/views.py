from django.shortcuts import render
from django.http import HttpResponse
from api.models import Stops
from api.serializers import StopsSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.serializers import FooSerializer
from api.models import Routes
from api.models import StopTimes




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#@csrf_exempt
def stops_list(request):
    print("meter list");
    if request.method == 'GET':
        stops = Stops.objects.all()
        serializer = StopsSerializer(stops, many=True)
        return JSONResponse(serializer.data)

#@csrf_exempt
def departures_detail(request, pk, fk):
    print("departure detail" + " " + pk + " " + fk);
    #time="'17:18:00'"
    time="'"+pk+"'"
    stop = "'"+fk+"'"

    query="select DISTINCT ON (route_short_name) api_routes.route_id, route_short_name, api_trips.trip_headsign, departure_time, api_trips.delay from api_stoptimes inner join api_trips on api_stoptimes.trip_id = api_trips.trip_id inner join api_routes on api_trips.route_id=api_routes.route_id inner join api_stops on api_stoptimes.stop_id = api_stops.stop_id where departure_time > " + time + " AND api_trips.service_id = '10' and api_stops.stop_code = " + stop + " ORDER BY route_short_name ASC, departure_time ASC;"

    print(query);
    departures=Routes.objects.raw(query)


    #departures = StopTimes.objects.filter(stop_id='4').filter(departure_time__gte='17:18:00').filter(trip_id__service_id='20160221_10').order_by('trip_id__route_id__route_short_name', 'departure_time').distinct('trip_id__route_id__route_short_name').values('trip_id__trip_headsign', 'trip_id__route_id__route_short_name', 'departure_time', 'trip_id__route_id');

    serializer=FooSerializer(departures,many=True)
    return JSONResponse(serializer.data)

#@csrf_exempt
def stops_detail(request, pk):
    print("meter detail: " + pk);
    #stop = Stops.objects.get(stop_id__exact=pk)
    stop = Stops.objects.get(stop_code__exact=pk)
    serializer = StopsSerializer(stop)
    return JSONResponse(serializer.data)

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

