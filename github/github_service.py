import os

from dotenv import load_dotenv

from qwarry.requests_adapter import RequestsAdapter


class GithubService:
    def __init__(self, requests_adapter: RequestsAdapter):
        self._requests_adapter = requests_adapter
        load_dotenv()

    def get_commit_list(self, repository_name: str) -> list:
        commits = []
        headers = {'Authorization': 'token %s' % os.getenv('API_KEY')}
        response = self._requests_adapter.http_get(
            f'/repos/baptistelinel/{repository_name}/commits', headers=headers)
        if response['status_code'] != 200:
            raise Exception(
                f"Request status is {response['status_code']}. Commit list seems to not be reachable. Github API returns response{response['json']}"
            )
        for raw_commit in response['json']:
            commit = {
                'id': raw_commit['sha'],
                'committer_name': raw_commit['commit']['committer']['name'],
                'date': raw_commit['commit']['committer']['date'],
                'message': raw_commit['commit']['message']
            }
            commits.append(commit)
        return commits
