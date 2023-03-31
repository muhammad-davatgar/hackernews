from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_questions, name='all_questions'),
    path("<int:id>/", views.single_question, name='single_question'),
    path("create/", views.create_question, name="create_question")
]
