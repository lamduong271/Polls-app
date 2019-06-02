
from django.urls import path
from . import views
app_name = "polls"
urlpatterns = [
    path('questions/detail/<int:question_id>', views.detailView, name="detail-view"),
    path('', views.index),
    path('questions/', views.viewList, name="questions-list"),
    path('questions/detail/vote/<int:question_id>', views.vote, name="vote"),
]
