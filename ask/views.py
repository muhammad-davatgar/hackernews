from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from . import models
from .forms import QuestionForm, AnswerForm
# Create your views here.


def all_questions(request):
    data = {"questions": models.Question.objects.all()}
    return render(request, 'all_questions.html', data)


def create_question(request) -> HttpResponse:
    if request.method == "GET":
        form = QuestionForm()
        return render(request, "create_question.html", {"form": form})
    elif request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("all_questions")
    else:
        return HttpResponseNotAllowed(["POST", "GET"])


def single_question(request, id) -> HttpResponse:
    if request.method == "GET":
        question = get_object_or_404(models.Question, pk=id)
        answers = models.Answer.objects.order_by("created_at")
        form = AnswerForm()
        return render(request, "single_question.html", {"question": question, "answers": answers, "form": form})
    elif request.method == "POST":
        try:
            reply = models.Answer()
            if request.POST.get('reply') == '0':
                reply = None
            else:
                try:
                    reply = models.Answer.objects.get(pk=id)
                except models.Answer.DoesNotExist:
                    messages.success(request, 'invalid form')
                    return HttpResponseBadRequest()

            text = request.POST['text']
            question = get_object_or_404(models.Question, pk=id)
            answer = models.Answer(text=text, question=question, reply=reply)
            answer.save()
            return redirect(f'/ask/{id}/')
        except KeyError:
            messages.error(request, 'invalid form')
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(["POST", "GET"])
