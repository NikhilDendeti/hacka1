# Generated by Django 5.1.6 on 2025-02-22 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dyslexia_assessment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dyslexiatestresult',
            old_name='ai_severity_score',
            new_name='final_severity_score',
        ),
    ]
