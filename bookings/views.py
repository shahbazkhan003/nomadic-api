from rest_framework import viewsets
from .models import Schedule
from .serializers import ScheduleSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
