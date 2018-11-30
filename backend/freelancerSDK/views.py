
from django.http import HttpResponseRedirect
from rest_framework import permissions, status, viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from django.utils import timezone

@api_view(['POST', 'GET'])
def hello(req):
    print(req.data.get('hi'))
    return Response({'msg' : 'hello world'}, status=status.HTTP_200_OK)

@api_view(['POST', 'GET'])
def create_fixed_project(req):
    # replace with create fixed project function here
    return Response({'msg' : 'hello world'}, status=status.HTTP_200_OK)

@api_view(['POST', 'GET'])
def search_project(req):
    # replace with search project function here
    return Response({'msg' : 'hello world'}, status=status.HTTP_200_OK)

