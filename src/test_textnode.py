import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node3 = TextNode("Some Text", TextType.ITALIC)
        node4 = TextNode("Some Text", TextType.ITALIC)
        self.assertEqual(node3, node4)

    def test_eq3(self):
        node5 = TextNode("More text for testing", TextType.LINKS, None)
        node6 = TextNode("More text for testing", TextType.LINKS)
        self.assertEqual(node5, node6)

    def test_eq4(self):
        node7 = TextNode("RHYSAND IS THE MOST HANDSOME HIGHLORD", TextType.BOLD)
        node8 = TextNode("RHYSAND IS THE MOST HANDSOME HIGHLORD", TextType.BOLD)
        self.assertEqual(node7, node8)

if __name__ == "__main__":
    unittest.main()