from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from pilot import views

urlpatterns = [
    path('pilot/', views.pilot_list),
    path('pilot/<int:pk>/', views.pilot_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
