# Generated by Django 4.2 on 2023-06-02 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyroombase', '0002_question_downvotes_question_upvotes'),
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
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
    ]
