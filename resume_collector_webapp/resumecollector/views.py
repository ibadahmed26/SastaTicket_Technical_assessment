from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer, ResumeSerializer
from rest_framework import viewsets
from .models import ResumeModel
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


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


class ResumeData(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ResumeSerializer
    filter_backends = [SearchFilter]
    search_fields = ["skill", "experience"]

    def get_queryset(self):
        resumes = ResumeModel.objects.all()
        return resumes
