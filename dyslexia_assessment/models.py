from django.db import models
from django.conf import settings  # Use AUTH_USER_MODEL

class DyslexiaTestResult(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Best practice: Allows custom user models
        on_delete=models.CASCADE,  # Delete results if user is deleted
        related_name="dyslexia_results",  # Allows reverse access (user.dyslexia_results.all())
    )
    word_confusion_score = models.FloatField()
    reading_speed = models.FloatField()
    letter_confusion_score = models.FloatField()
    final_severity_score = models.FloatField()
    severity = models.CharField(
        max_length=10,
        choices=[('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe')]
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.severity} - {self.timestamp}"
