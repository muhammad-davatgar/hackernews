from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from . import models
from .forms import PostForm, CommentForm
# Create your views here.


def all_questions(request):
    data = {"questions": models.Post.objects.all()}
    return render(request, 'all_questions.html', data)


def create_question(request) -> HttpResponse:
    if request.method == "GET":
        form = PostForm()
        return render(request, "create_question.html", {"form": form})
    elif request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("all_questions")
    else:
        return HttpResponseNotAllowed(["POST", "GET"])


def single_question(request, id) -> HttpResponse:
    if request.method == "GET":
        question = get_object_or_404(models.Post, pk=id)
        answers = models.Comment.objects.order_by("created_at")
        form = CommentForm()
        return render(request, "single_question.html", {"question": question, "answers": answers, "form": form})
    elif request.method == "POST":
        try:
            reply = models.Comment()
            if request.POST.get('reply') == '0':
                reply = None
                print("here")
            else:
                print("three")
                try:
                    reply = models.Comment.objects.get(
                        pk=request.POST['reply'])
                except (KeyError, models.Comment.DoesNotExist):
                    messages.error(request, 'invalid form')
                    return HttpResponseBadRequest()

            text = request.POST['text']
            question = get_object_or_404(models.Post, pk=id)
            answer = models.Comment(text=text, question=question, reply=reply)
            answer.save()
            return redirect(f'/post/ask/{id}/')
        except KeyError:
            messages.error(request, 'invalid form')
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(["POST", "GET"])
