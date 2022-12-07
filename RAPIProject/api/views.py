from rest_framework.response import Response
from rest_framework.decorators import api_view
from weatherApp.models import WeatherData
from .serializers import WeatherDataSerializer


@api_view(['GET'])
def getData(request):
    items = WeatherData.objects.all()
    serializer = WeatherDataSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = WeatherDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 
