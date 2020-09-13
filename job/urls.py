from django.urls import path

from job.views import OccupationView

urlpatterns = [
    path('', OccupationView.as_view()),
]
