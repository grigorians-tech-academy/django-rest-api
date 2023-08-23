from rest_framework import serializers

from main.models import Project, Task
from main.serializers.project import ProjectSerializer
from main.serializers.user import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    project_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        user = self.context["request"].user
        project_id = validated_data.pop("project_id", None)
        if project_id:
            project = Project.objects.get(id=project_id)
            return Task.objects.create(
                owner=user, project=project, **validated_data
            )
        return Task.objects.create(owner=user, **validated_data)

    class Meta:
        model = Task
        fields = "__all__"
