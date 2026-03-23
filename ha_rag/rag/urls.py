from django.urls import path
from .views import upload_pdf, ask_question

urlpatterns = [
    path("upload/", upload_pdf),
    path("ask/", ask_question),
]