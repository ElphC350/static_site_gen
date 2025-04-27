import unittest

from nodeDelimiter import *

class TestSingleFunction(unittest.TestCase):
    # ---- TEST block_to_block_type FUNCTION ----
    def test_b2bt_heading(self):
        txt1 = "### This is a Lvl3 Heading."
        res1 = block_to_block_type(txt1)
        self.assertEqual(res1, "heading")

    def test_b2bt_code(self):
        txt2 = "```This is a code block```"
        res2 = block_to_block_type(txt2)
        self.assertEqual(res2, "code")

    def test_b2bt_quote_single(self):
        txt3 = "> A single quote block"
        res3 = block_to_block_type(txt3)
        self.assertEqual(res3, "quote")

    def test_b2bt_quote_double(self):
        txt4 = "> This block has one quote\n> and two quotes"
        res4 = block_to_block_type(txt4)
        self.assertEqual(res4, "quote")

    def test_b2bt_quote_misquote(self):
        txt5 = "> A quote block\n with a misquoted line"
        res5 = block_to_block_type(txt5)
        self.assertEqual(res5, "paragraph")

    def test_b2bt_unordered_list(self):
        txt6 = "- A short \n- unordered \n- list"
        res6 = block_to_block_type(txt6)
        self.assertEqual(res6, "unordered_list")

    def test_b2bt_ordered_list(self):
        txt7 = "1. Thing one\n2. Thing two\n3. Thing three"
        res7 = block_to_block_type(txt7)
        self.assertEqual(res7, "ordered_list")

    def test_b2bt_ordered_list_nonSeq(self):
        txt8 = "1. Non-sequential\n3. ordered list"
        res8 = block_to_block_type(txt8)
        self.assertEqual(res8, "paragraph")

if __name__ == "__main__":
    unittest.main()