from django.shortcuts import render

from github.github_service import GithubService


class GithubViews:
    def __init__(self, github_service: GithubService):
        self._github_service = github_service

    def commit_list(self, request):
        if request.POST and request.POST['repository_name']:
            try:
                commit_list = self._github_service.get_commit_list(request.POST['repository_name'])
                context = {'commit_list': commit_list}
                return render(request, 'github/commit_list.html', context)
            except Exception:
                context = {'error': 'Github project not found.'}
                return render(request, 'github/repository_form.html', context)
        else:
            return render(request, 'github/repository_form.html')
