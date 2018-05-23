from django.http import Http404
from .models import Student
from restapp.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        users = Student.objects.all()
        serializer = UserSerializer(users, many=True)
        #return Response(serializer.data)
        return render(request, 'restapp/userlist.html', {'users': serializer.data})

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if not serializer.initial_data['username'].isdigit():
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve particular user, update or delete a user instance.
    """
    @staticmethod
    def get_objectusr(urlpat):
        try:
            return Student.objects.get(username=urlpat)
        except Student.DoesNotExist:
            raise Http404

    @staticmethod
    def get_objectid(urlpat):
        try:
            return Student.objects.get(pk=urlpat)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, urlpat, format=None):
        print(urlpat)
        if urlpat.isdigit():
            user = self.get_objectid(urlpat)
        else:
            user = self.get_objectusr(urlpat)
        user = UserSerializer(user)
        return Response(user.data)

    def put(self, request, urlpat, format=None):
        user = self.get_objectid(urlpat)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, urlpat, format=None):
        user = self.get_objectid(urlpat)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
