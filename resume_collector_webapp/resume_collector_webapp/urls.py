from django.contrib import admin
from django.urls import path
from resumecollector import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/signup/", views.RegisterUser.as_view(), name="signup"),
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]
