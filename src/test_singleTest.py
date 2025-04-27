import unittest

from nodeDelimiter import *

class TestSingleFunction(unittest.TestCase):
    # ---- Test markdown_to_blocks function ----
    def test_md2b_1(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_md2b_2(self):
        md2 = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
    """
        blocks2 = markdown_to_blocks(md2)
        self.assertEqual(
            blocks2,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
            ]
        )

    def test_md2b_xnewlines(self):
        md3 = """
This is a simple block




With excessive newlines
    """
        blocks3 = markdown_to_blocks(md3)
        self.assertEqual(
            blocks3,
            [
                "This is a simple block",
                "With excessive newlines"
            ]
        )

    def test_md2b_onlyNewlines(self):
        md4 = """



"""
        blocks4 = markdown_to_blocks(md4)
        self.assertEqual(
            blocks4, []
        )

if __name__ == "__main__":
    unittest.main()