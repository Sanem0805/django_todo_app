from rest_framework import serializers

from .models import ToDo

class ToDoSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    is_complited = serializers.BooleanField(required=False)
    created_at = serializers.ReadOnlyField()
    deadline = serializers.DateTimeField()

class UpdateToDoSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    deadline = serializers.DateTimeField(required=False)
    complited = serializers.BooleanField(required=False)

    def update(self, instance: ToDo, validated_data: dict) -> ToDo:
        print(validated_data)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        # instance.title = validated_data.get('title', instance.title)
        # instance.deadline = validated_data.get('deadline', instance.deadline)
        # instance.complited = validated_data.get('complited', instance.complited)
        instance.save()
        return instance