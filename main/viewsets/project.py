from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from main.models import Project
from main.serializers.project import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(owner=user)
