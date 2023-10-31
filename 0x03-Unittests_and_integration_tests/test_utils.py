#!/usr/bin/env python3
"""Unittest: Parameterize unit test, Mock HTTP calls,Parameterize and patch"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """TESTCASE - inherits from unittest.TestCase"""
    """tests the function for the inputs"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """ test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), answer)

    """test that a KeyError is raised for the inputs below"""
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test if a KeyError is raised properly"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
            self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """TESTCASE"""
    """test the function for the inputs below"""
    @parameterized.expand([
        ("http://example.com", {"paylod": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.getjson')
    def test_get_json(self, test_url, test_payload, mock_test):
        """test that utils.get_json returns expected result"""
        mock_get.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """TESTCASE"""
    def test_memoize(self):
        """test if the correct result is returned when a_property is
            called twice, but a_method is called using assert_called_once
        """
        class TestClass:
            """class"""
            def a_method(self):
                """a method"""
                return 42

            @memoize
            def a_property(self):
                """a property"""
                return self.a_method()
        with patch.object(TestClass, "a_method") as mockMethod:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mockMethod.assert_called_once
