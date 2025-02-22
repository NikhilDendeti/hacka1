from django.contrib.auth.models import User
from django.db import models

class GameProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="game_progress")
    level = models.CharField(max_length=20, default="mild_level1")  # Tracks current level
    score = models.IntegerField(default=0)
    attempts = models.IntegerField(default=0)  # Number of tries for a level
    unlocked_next = models.BooleanField(default=False)  # Has the next level unlocked?

    def __str__(self):
        return f"{self.user.username} - {self.level} - Score: {self.score}"


class GameLevel(models.Model):
    LEVEL_CHOICES = [
        ("mild_level1", "Mild Level 1"),
        ("mild_level2", "Mild Level 2"),
        ("mild_level3", "Mild Level 3"),
        ("moderate_level1", "Moderate Level 1"),
        ("moderate_level2", "Moderate Level 2"),
        ("moderate_level3", "Moderate Level 3"),
        ("severe_level1", "Severe Level 1"),
        ("severe_level2", "Severe Level 2"),
        ("severe_level3", "Severe Level 3"),
    ]
    name = models.CharField(max_length=50, choices=LEVEL_CHOICES, unique=True)

    def __str__(self):
        return self.name


class UserGameResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="game_results")
    level = models.ForeignKey(GameLevel, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    attempts = models.IntegerField(default=0)  # Number of tries for this level
    unlocked_next = models.BooleanField(default=False)  # If user has unlocked next level

    def __str__(self):
        return f"{self.user.username} - {self.level.name} - Score: {self.score}"