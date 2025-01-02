import unittest

from textnode import TextNode, TextType, text_node_to_html_node

# Pre-written list for testing   
tests = [
    TextNode("some basic beach text", TextType.NORMAL),
    TextNode("some basic beach text", TextType.BOLD),
    TextNode("some basic beach text", TextType.ITALIC),
    TextNode("some basic beach text", TextType.CODE),
    TextNode("some basic beach text", TextType.LINK, "https://alink.com"),
    TextNode("some basic beach text", TextType.IMAGE, "https://picture.img")
]

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
        node5 = TextNode("More text for testing", TextType.LINK, None)
        node6 = TextNode("More text for testing", TextType.LINK)
        self.assertEqual(node5, node6)

    def test_eq4(self):
        node7 = TextNode("RHYSAND IS THE MOST HANDSOME HIGHLORD", TextType.BOLD)
        node8 = TextNode("RHYSAND IS THE MOST HANDSOME HIGHLORD", TextType.BOLD)
        self.assertEqual(node7, node8)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = tests[0]
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.TAG, node.text_type.value)
        self.assertEqual(html_node.VALUE, node.text)
    def test_italic(self):
        node = tests[2]
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.TAG, node.text_type.value)
        self.assertEqual(html_node.VALUE, node.text)
    def test_link(self):
        node = tests[4]
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.TAG, node.text_type.value)
        self.assertEqual(html_node.VALUE, node.text)
        self.assertEqual(
            html_node.PROPS,
            {"href": node.url}
        )
    def test_image(self):
        node = tests[5]
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.TAG, node.text_type.value)
        self.assertEqual(html_node.VALUE, "")
        self.assertEqual(
            html_node.PROPS,
            {"src": node.url, "alt": node.text}
        )

if __name__ == "__main__":
    unittest.main()