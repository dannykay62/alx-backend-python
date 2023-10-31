#!/usr/bin/env python3
"""implement the test_org method"""
"""Parametrize, mock property, patch decorator, Integration test, fixtures"""
import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


class TestGithubOrgClient(unittest.TestCase):
    """test that GithubOrgClient.org returns the correct value."""
    @parameterized.expand([
        ("google")
        ("abc")
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """test for GithubOrgClient return the right value"""
        test_client = GithubOrgClient(org_name)
        test_return = test_client.org
        self.assertEqual(test_return, mock_get.return_value)
        mock_get.assert_called_once

    def test_public_repos_url(self):
        """ unit-test GithubOrgClient._public_repos_url"""
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value={"repos_url": "holberton"}) as mock_get:
            test_json = {"repos_url": "holberton"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            mock_get.assert_called_once

    def test_public_repos_url(self):
        """Use patch as a context manager to mock"""
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value={"repos_url": "holberton"}) as mock_get:
            test_json = {"repos_url": "holberton"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(test_return,
                             mock_get.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "holberton"}])
    def test_public_repos(self, mock_get):
        """Use @patch as a decorator to mock get_json and make
            it return a payload of your choice
        """
        with patch.object(GithubOrgClient,
                          "_public_repo_url",
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pub:
            test_client = GithubOrgClient("holberton")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["holberton"])
            mock_get.assert_called_once
            mock_pub.assert_called_once

        """test the functions with inputs"""
        @parameterized.expand([
            ({"license": {"key": "my_license"}}, "my_license", True)
            ({"license": {"key": "other_license"}}, "my_license", False)
        ])
        def test_has_license(self, repo, license_key, expected_return):
            """to unit-test GithubOrgClient.has_license"""
            test_client = GithubOrgClient("holberton")
            test_return = test_client.has_license(repo, license_key)
            self.assertEqual(expected_return, test_return)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """implement the setUpClass and
    tearDownClass
    to return example payloads found in the
    fixtures"""
    def setUpClass(cls):
        """part of unittest API
        """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """ It is part of the unittest.TestCase API
        method to stop the patcher """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ method to test GithubOrgClient.public_repos """
        test_class = GithubOrgClient("holberton")
        assert True

    def test_public_repos_with_license(self):
        """ method to test the public_repos with the argument license """
        test_class = GithubOrgClient("holberton")
        assert True
