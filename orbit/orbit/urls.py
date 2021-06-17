from django.urls import path, include

urlpatterns = [
    path('', include('pilot.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
