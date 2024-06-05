from django.urls import path
from . import views
from .views import QuestionListView, QuestionDetailView, QuestionCreateView, QuestionDeleteView, AnswerCreateView, AnswerDeleteView, CommentCreateView, CommentDeleteView, search, upvote_view, downvote_view

app_name = 'cyroombase'

urlpatterns = [
    path('', QuestionListView.as_view(), name='cyroombase-questions'),
    path('questions/', QuestionListView.as_view(), name='cyroombase-questions'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('questions/new/', QuestionCreateView.as_view(), name='question-create'),
    path('questions/<int:pk>/delete/', QuestionDeleteView.as_view(), name='question-delete'),
    path('questions/<int:pk>/answer/', AnswerCreateView.as_view(), name='answer-create'),
    path('questions/answer/<int:pk>/delete/', AnswerDeleteView.as_view(), name='answer-delete'),
    path('questions/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('questions/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search, name='search'),
    path('questions/<int:pk>/upvote/', upvote_view, name='upvote'),
    path('questions/<int:pk>/downvote/', downvote_view, name='downvote'),
]
