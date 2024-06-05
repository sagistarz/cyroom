# from django.db import models
# from django.urls import reverse
# from django.utils import timezone
# from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField

# class Question(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=256)
#     content = models.TextField(default=None, blank=True, null=True)
#     snippet = models.TextField(default=None, blank=True, null=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#     # upvotes = models.IntegerField(default=0)
#     # downvotes = models.IntegerField(default=0)   
    
#     def __str__(self):
#         return self.title

#     def __str__(self):
#         return f'{self.user.username} - Question'
    
#     def get_absolute_url(self):
#         return reverse('cyroombase:question-detail', kwargs={'pk':self.pk})
    
#     def upvote(self):
#         upvotes += 1
#         self.save()
    
#     def downvote(self):
#         downvotes += 1
#         self.save()

# class Answer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question_origin = models.ForeignKey(Question, on_delete=models.CASCADE)
#     content = models.TextField()
#     snippet = models.TextField(default=None, blank=True, null=True)
#     upload_time = models.DateTimeField(default=timezone.now)

#     def get_absolute_url(self):
#         return reverse('cyroombase:question-detail', kwargs={'pk': self.pk})

# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question_origin = models.ForeignKey(Question, on_delete=models.CASCADE)
#     content = models.TextField()
#     upload_time = models.DateTimeField(default=timezone.now)

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    snippet = models.TextField(default=None, blank=True, null=True)
    upvotes = models.IntegerField(default=0)
    upvoted_users = models.ManyToManyField(User, related_name='upvoted_questions')
    downvotes = models.IntegerField(default=0)
    downvoted_users = models.ManyToManyField(User, related_name='downvoted_questions')
    upload_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cyroombase:cyroombase-questions')
    
    def upvote(self):
        upvotes += 1
        self.save()
    
    def downvote(self):
        downvotes += 1
        self.save()

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    origin_question = models.ForeignKey(Question, on_delete=models.CASCADE, default='DEFAULT')
    content = models.TextField()
    snippet = models.TextField(default=None, blank=True, null=True)
    upload_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.origin_question.title, self.origin_question.author)
    
    def get_absolute_url(self):
        return reverse('cyroombase:question-detail', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    origin_question = models.ForeignKey(Question, on_delete=models.CASCADE, default='DEFAULT')
    content = models.TextField()
    upload_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.origin_question.title, self.origin_question.author)
    
    def get_absolute_url(self):
        return reverse('cyroombase:question-detail', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)