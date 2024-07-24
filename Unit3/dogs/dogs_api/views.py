from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Dog,Breed
from .serializers import DogSerializer, BreedSerializer


class BreedDetail(viewsets.ViewSet):
    """GET, PUT or DELETE a breed instance."""

    def retrieve(self, request, pk=None):
        breed_instance = get_object_or_404(Breed, pk=pk)
        serializer = BreedSerializer(breed_instance)
        return Response(serializer.data)

    def update(self, request, pk=None):
        breed_instance = get_object_or_404(Breed, pk=pk)

        serializer = BreedSerializer(breed_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        breed = get_object_or_404(Breed, pk=pk)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedList(viewsets.ViewSet):
    """GET all breeds, POST breed"""
    def list(self, request):
        queryset = Breed.objects.all()
        serializer = BreedSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(APIView):
    """GET, PUT or DELETE a dog instance."""
    def get(self, request, pk=None):
        dog_instance = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog_instance)
        return Response(serializer.data)

    def put(self, request, pk=None):
        dog_instance = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        dog_instance = get_object_or_404(Dog, pk=pk)
        dog_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DogDetailList(APIView):
    """GET all dogs, POST dog"""
    def get(self, request):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

