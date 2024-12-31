import unittest

from extractdata import extract_markdown_images, extract_markdown_links
from vars import *

class TestExtractImage(unittest.TestCase):
    def test_ieq1(self):
        itst1 = extract_markdown_images(mdimage)
        iout1 = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(itst1, iout1)

class TestExtractLink(unittest.TestCase):
    def test_leq1(self):
        ltst1 = extract_markdown_links(mdlink)
        lout1 = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        self.assertEqual(ltst1, lout1)

if __name__ == "__main__":
    unittest.main()
