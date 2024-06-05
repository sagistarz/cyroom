# Generated by Django 4.2 on 2023-06-02 18:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cyroombase', '0003_remove_question_downvotes_remove_question_upvotes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='downvotes',
        ),
        migrations.RemoveField(
            model_name='question',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='question',
            name='downvotes',
            field=models.ManyToManyField(related_name='down_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='upvotes',
            field=models.ManyToManyField(related_name='up_post', to=settings.AUTH_USER_MODEL),
        ),
    ]