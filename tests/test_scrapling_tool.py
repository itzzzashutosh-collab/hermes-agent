import unittest
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tools.scrapling_tool import scrapling_scrape, _check_scrapling_reqs

class TestScraplingTool(unittest.TestCase):
    def test_scrapling_available(self):
        self.assertTrue(_check_scrapling_reqs(), "Scrapling package must be importable in environment")

    def test_scrape_valid_url(self):
        res_str = scrapling_scrape("https://httpbin.org/html", css_selector="h1")
        res = json.loads(res_str)
        self.assertEqual(res["status"], "SUCCESS")
        self.assertEqual(res["http_status"], 200)
        self.assertTrue(len(res["selected_elements"]) > 0)
        self.assertIn("Moby-Dick", res["selected_elements"][0])

    def test_empty_url_error(self):
        res_str = scrapling_scrape("")
        res = json.loads(res_str)
        self.assertIn("error", res)

if __name__ == "__main__":
    unittest.main()
