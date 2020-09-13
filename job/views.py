from django.views.generic import ListView

from job.models import Occupation


class OccupationView(ListView):
    model = Occupation


