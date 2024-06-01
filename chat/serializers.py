from rest_framework import serializers


class ChatSerializer(serializers.Serializer):
    session_id = serializers.IntegerField()
    user = serializers.CharField(max_length=100)
    message = serializers.CharField()
