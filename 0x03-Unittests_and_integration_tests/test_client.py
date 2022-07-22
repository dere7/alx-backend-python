#!/usr/bin/env python3
"""tests client module"""
import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """tests GithubOrgClient"""

    def setUp(self):
        """initialization"""
        self.payload = TEST_PAYLOAD[0][0]
        self.public_repos = TEST_PAYLOAD[0][1]
        self.public_repos_name = TEST_PAYLOAD[0][2]

    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json', return_value={})
    def test_org(self, org_name, mock_get_json):
        """tests org method of GithubOrgClient"""
        client = GithubOrgClient(org_name)
        client.org
        org_url = GithubOrgClient.ORG_URL.format(org=org_name)
        mock_get_json.assert_called_once_with(org_url)

    def test_public_repos_url(self):
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = self.payload
            client = GithubOrgClient('google')
            self.assertEqual(self.payload['repos_url'],
                             client._public_repos_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """tests public_repos method"""
        mock_get_json.return_value = self.public_repos
        client = GithubOrgClient('google')
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value=self.payload['repos_url']):
            self.assertEqual(client.public_repos(), self.public_repos_name)

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """tests has_license"""
        self.assertEqual(GithubOrgClient.has_license(
            repo, license_key), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """integration test GithubOrgClient"""

    def setUp(self):
        """setups a patcher"""
        self.patcher = patch('requests.get')
        mock_get = self.patcher.start()

        def get_mock_requests(url: str) -> MagicMock:
            mock = MagicMock()
            if (url == "https://api.github.com/orgs/google"):
                mock.json.return_value = self.org_payload
            else:
                mock.json.return_value = self.repos_payload
            return mock
        mock_get.side_effect = get_mock_requests

    def tearDown(self):
        """stops a patcher"""
        self.patcher.stop()

    def test_public_repos(self):
        """integration tests public repos"""
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(), self.expected_repos)
