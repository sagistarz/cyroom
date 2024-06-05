# Generated by Django 4.2 on 2023-06-02 18:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cyroombase', '0006_question_upvoted_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='downvoted_users',
            field=models.ManyToManyField(related_name='downvoted_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]