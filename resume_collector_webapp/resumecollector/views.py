from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer


class RegisterUser(APIView):
    def post(self, request):
        payload = request.data
        serialized = UserSerializer(data=payload)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(
            {'success': True,
             'msg': 'User Signed up'},
            status=status.HTTP_201_CREATED
        )
