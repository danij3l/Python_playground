from rest_framework.response import Response
from rest_framework.decorators import api_view
from Home.models import Animals
from .serializers import AnimalSerializer

@api_view(['GET'])
def getData(request):
    animals = Animals.objects.all()
    serializer = AnimalSerializer(animals, many=True)
    return Response(serializer.data)