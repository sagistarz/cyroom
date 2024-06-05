from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from .models import Question, Answer, Comment
from .forms import CommentForm, AnswerForm

def home(request):
    return render(request, 'home.html')

# class based

class QuestionListView(ListView):
    model = Question
    template_name = 'cyroombase/home.html'
    context_object_name = 'question'
    ordering = ['-upload_time']

class QuestionDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        question = Question.objects.get(pk=pk)
        self.current_question = question

        comment_form = CommentForm()
        comment = Comment.objects.filter(origin_question=question).order_by('-upload_time')
        answer = Answer.objects.filter(origin_question=question).order_by('-upload_time')

        context = {
            'question': question,
            'form': comment_form,
            'comment': comment,
            'answer': answer,
        }

        return render(request, 'cyroombase/question_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        question = Question.objects.get(pk=pk)

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.origin_question = question
            new_comment.save()

        comment_form = CommentForm()

        comment = Comment.objects.filter(origin_question=question).order_by('-upload_time')
        answer = Answer.objects.filter(origin_question=question).order_by('-upload_time')

        context = {
            'question': question,
            'form': comment_form,
            'comment': comment,
            'answer': answer,
        }

        return render(request, 'cyroombase/question_detail.html', context)
    
    def get_upvotes_data(self, *args, **kwargs):
        context = super(QuestionDetailView, self).get_context_data()
        something = get_object_or_404(Question, id=self.kwargs['pk'])
        total_upvotes = something.total_upvotes()
        upvoted = False
        if something.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True

        context['total_upvotes'] = total_upvotes
        context['upvoted'] = upvoted
        return context
    
    def get_downvotes_data(self, *args, **kwargs):
        context = super(QuestionDetailView, self).get_context_data()
        something = get_object_or_404(Question, id=self.kwargs['pk'])
        total_downvotes = something.total_downvotes()
        downvoted = False
        if something.downvotes.filter(id=self.request.user.id).exists():
            downvoted = True

        context['total_downvotes'] = total_downvotes
        context['downvoted'] = downvoted
        return context
    

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'content', 'snippet']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    # success_url = '/my_questions/'
    # success_url = '/question_detail/'

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False
    def get_success_url(self):
        return reverse('cyroombase:cyroombase-questions')


class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ['content', 'snippet']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question_pk'] = self.kwargs['pk']
        context['question'] = get_object_or_404(Question, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.origin_question = get_object_or_404(Question, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('cyroombase:question-detail', args=[self.kwargs['pk']])

class AnswerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Answer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answer'] = get_object_or_404(Answer, pk=self.kwargs['pk'])
        return context

    def test_func(self):
        answer = self.get_object()
        if self.request.user == answer.author:
            return True
        return False
    
    def get_success_url(self):
        answer = get_object_or_404(Answer, pk=self.kwargs['pk'])
        question = get_object_or_404(Question, pk=answer.origin_question.pk)
        return reverse('cyroombase:question-detail', args=[question.pk])

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['question_pk'] = self.kwargs['pk']
        context['question'] = get_object_or_404(Question, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.origin_question = get_object_or_404(Question, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('cyroombase:question-detail', args=[self.kwargs['pk']])

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = get_object_or_404(Comment, pk=self.kwargs['pk'])
        return context

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False
    
    def get_success_url(self):
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        question = get_object_or_404(Question, pk=comment.origin_question.pk)
        return reverse('cyroombase:question-detail', args=[question.pk])

# function based

# def search(request):
#     query = request.GET.get('search')
#     if query:
#         context = {
#             'questions': Question.objects.filter(title__icontains=query),
#             'query': query,
#         }
#         return render(request, 'cyroombase/search.html', context)
    
#     return redirect(reverse('cyroombase:questions'))

def search(request):
    query = request.GET.get('query')

    if query:
        questions = Question.objects.filter(title__icontains=query)
    else:
        questions = []

    context = {
        'questions': questions,
        'query': query
    }
    return render(request, 'cyroombase/search.html', context)

def upvote_view(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.user in question.upvoted_users.all():
        question.upvoted_users.remove(request.user)
        question.upvotes -= 1
    else:
        question.upvoted_users.add(request.user)
        question.upvotes += 1
    question.save()
    return redirect('cyroombase:question-detail', pk=question.pk)  # Redirect to the question detail page

def downvote_view(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.user in question.downvoted_users.all():
        question.downvotes -= 1
        question.downvoted_users.remove(request.user)
    else:
        question.downvotes += 1
        question.downvoted_users.add(request.user)
    question.save()
    return redirect('cyroombase:question-detail', pk=question.pk)  # Redirect to the question detail page


# kalau mau dibuka, harus login dulu

@login_required
def profile(request):
    context = {
        'questions_asked': len(Question.objects.filter(author=request.user)),
        'answers_given': len(Answer.objects.filter(author=request.user)),
        'comments_made': len(Comment.objects.filter(author=request.user)),
    }
    return render(request, 'cyroombase/profile.html', context)