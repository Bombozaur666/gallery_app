from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def home(request):
    return Response({'description': 'pong'})



