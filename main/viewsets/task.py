from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from main.models import Task
from main.serializers.task import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["project_id", "completed"]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(owner=user)
