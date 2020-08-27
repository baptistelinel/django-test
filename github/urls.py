from django.urls import path

from qwarry.requests_adapter import RequestsAdapter
from .github_service import GithubService
from .views import GithubViews

github_service = GithubService(RequestsAdapter())
github_view = GithubViews(github_service)

app_name = 'github'
urlpatterns = [
    path('commits',
         github_view.commit_list,
         name='commit_list'),
]
