#!/usr/bin/env python3
"""tests client module"""
import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


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
                   return_value=self.payload['repos_url']) as mock_public_repo:
            self.assertEqual(client.public_repos(), self.public_repos_name)
            mock_get_json.assert_called_once()
            mock_public_repo.assert_called_once()

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

    @classmethod
    def setUp(cls):
        """setups a patcher"""
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDown(cls):
        """stops a patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """integration tests public repos"""
        assert True

    def test_has_license(self):
        """tests has_license method"""
        assert True
