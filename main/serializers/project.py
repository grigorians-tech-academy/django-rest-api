from rest_framework import serializers

from main.models import Project
from main.serializers.user import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    def create(self, validated_data):
        user = self.context["request"].user
        return Project.objects.create(owner=user, **validated_data)

    class Meta:
        model = Project
        fields = ["owner", "name"]
