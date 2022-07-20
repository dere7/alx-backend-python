#!/usr/bin/env python3
"""contains tests for utils module"""
from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import MagicMock
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    # Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """Tests utils module function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any):
        """tests access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        """tests access_nested_map function with exception"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        exception = cm.exception
        self.assertTrue(str(exception) not in path)


class TestGetJson(unittest.TestCase):
    """tests getJson methods"""

    def get_request(self, mock, payload):
        """gets request result"""
        mock.json.return_value = payload
        return mock

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @unittest.mock.patch("utils.requests")
    def test_get_json(self, test_url: str,
                      test_payload: Dict, mock_request: MagicMock):
        """tests get_json method from utils"""
        mock_request.get.side_effect = self.get_request(
            mock_request, test_payload)
        get_json(test_url)
        mock_request.get.assert_called_once_with(test_url)
        self.assertEqual(mock_request.json.return_value, test_payload)


class TestMemoize(unittest.TestCase):
    """tests memoize function"""

    def test_memoize(self):
        """tests memoize function"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
