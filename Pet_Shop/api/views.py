from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from Home.models import Animals
from .serializers import AnimalSerializer

@api_view(['GET'])
def getData(request):
    animals = Animals.objects.all()
    serializer = AnimalSerializer(animals, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addAnimal(request):
    serializer = AnimalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.errors)
        # [ErrorDetail(string='The submitted data was not a file. Check the encoding type on the form.', code='invalid')]
    return Response(serializer.data) 

#class based view -> we fetch object by Id in url and can update or delete it
class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=AnimalSerializer
    queryset = Animals.objects.all()
