from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status #list of standard http codes when sending responses from an api
from rest_framework import viewsets

from profiles_api import serializers #tell api view what data to expect when making a put / post /patch request

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,formal=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'Uses HTTP method as function(get,post,patch,put,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!' , 'an_apiview' : an_apiview})

    def post(self,request):
        """Create a hello message with our name """
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response ({'message' : message})
        else :
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None): #do a put with the ID of the url that you are updating
        """Handle updating an object"""
        return Response ({'method' : 'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method' : 'PATCH'})

    def delete(self,request,pk=None):
        return Response({'method' : 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        """Return a hello message"""
        a_viewset=[
            'Uses HTTP method as function(get,post,patch,put,delete)',
            'Is similar to a traditional django view',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello!' , 'a_viewset' : a_viewset})

    def create(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response ({'message' : message})
        else :
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None): #do a put with the ID of the url that you are updating
        """Handle getting an object by its ID"""
        return Response ({'HTTP-method' : 'GET'})

    def update(self,request,pk=None): #do a put with the ID of the url that you are updating
        """Handle updating an object"""
        return Response ({'HTTP-method' : 'PUT'})

    def partial_update(self,request,pk=None): #do a put with the ID of the url that you are updating
        """Handle updating part of an object"""
        return Response ({'HTTP-method' : 'PATCH'})

    def destroy(self,request,pk=None): #do a put with the ID of the url that you are updating
        """Handle removing an object"""
        return Response ({'HTTP-method' : 'DELETE'})
