from django.urls import include, re_path, path
from .apiviews  import PollList, PollDetail

urlpatterns = [
    path('polls/', PollList.as_view(), name='polls_list'),
    path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
]