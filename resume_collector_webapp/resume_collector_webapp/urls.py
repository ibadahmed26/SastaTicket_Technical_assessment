from django.contrib import admin
from django.urls import path, include
from resumecollector import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("resumes", views.ResumeData, basename="resumes_list")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("api/signup/", views.RegisterUser.as_view(), name="signup"),
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path("api/reference/", views.ReferenceData.as_view(), name="get_reference"),
]
