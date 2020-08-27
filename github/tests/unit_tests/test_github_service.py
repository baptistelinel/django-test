import unittest
from unittest.mock import Mock, ANY

from github.github_service import GithubService
from qwarry.requests_adapter import RequestsAdapter


class TestGithubService(unittest.TestCase):
    def setUp(self) -> None:
        self._requests_adapter = Mock(spec=RequestsAdapter)
        self._github_service = GithubService(self._requests_adapter)

    def test_get_commit_list_success(self):
        self._requests_adapter.http_get.return_value = {
            'status_code':
            200,
            'json': [{
                'sha': 'commit_id_1',
                'commit': {
                    'message': 'This is a commit message',
                    'committer': {
                        'name': 'toto',
                        'date': '25/08/2020'
                    }
                }
            }]
        }
        response = self._github_service.get_commit_list('github_repository')
        self._requests_adapter.http_get(
            '/repos/baptistelinel/github_repository/commits',
            headers={'Authorization': ANY})

        self.assertEqual(response, [{
            'id': 'commit_id_1',
            'committer_name': 'toto',
            'date': '25/08/2020',
            'message': 'This is a commit message'
        }])

    def test_get_commit_list_raise_exception(self):
        self._requests_adapter.http_get.return_value = {
            'status_code': 404,
            'json': 'Something went wrong.'
        }
        with self.assertRaisesRegex(
                Exception,
                'Request status is 404. Commit list seems to not be reachable. Github API returns response : Something went wrong'
        ):
            self._github_service.get_commit_list('github_repository_unknown')
