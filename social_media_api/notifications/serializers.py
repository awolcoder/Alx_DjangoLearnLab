from rest_framework import serializers
from .models import Notification
from posts.models import Post

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source='actor.username')
    target_title = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'actor_username', 'verb', 'target_title', 'is_read', 'timestamp']

    def get_target_title(self, obj):
        if isinstance(obj.target, Post):
            return obj.target.title
        return None
