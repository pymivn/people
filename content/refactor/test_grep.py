import unittest

import lib


class TestGrep(unittest.TestCase):
    def test_case_sensitive(self):
        res = lib.search(
            "duct",
            """Rust:
safe, fast, productive.
Pick three.
Duct tape.""".splitlines(),
        )
        self.assertEqual(list(res), ["safe, fast, productive."])

    def test_case_insensitive(self):
        res = lib.search_case_insensitive(
            "rUsT",
            """Rust:
safe, fast, productive.
Pick three.
Trust me.""".splitlines(),
        )
        self.assertEqual(list(res), ["Rust:", "Trust me."])
