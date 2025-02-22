from rest_framework import serializers
from game.models import GameProgress

class GameProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameProgress
        fields = ["user", "level", "score", "attempts", "unlocked_next"]
