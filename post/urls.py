from django.urls import path
from . import views


urlpatterns = [
    path('ask/', views.all_questions, name='all_questions'),
    path("ask/<int:id>/", views.single_question, name='single_question'),
    path("ask/create/", views.create_question, name="create_question")
]
