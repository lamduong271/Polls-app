
from django.urls import path
from . import views
urlpatterns = [
    path('detail/<int:question_id>', views.detailView, name="detail-view"),
    path('', views.index),
    path('questions/', views.viewList, name="questions-list"),
]
