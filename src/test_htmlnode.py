import unittest

from htmlnode import *

tag1 = "a"
tag2 = "h1"
val1 = "Here be some text to render"
val2 = "Here is some text to render"
chld1 = []
chld2 = []
prop1 = {
    "href": "https://somesite.dev/",
    "target": "_blank"
}
prop2 = {
    "href": "https://www.somesite.dev/",
    "target": "_blank"
}


class TestHTMLNode(unittest.TestCase):
    def test_heq1(self):
        node1 = HTMLNode("a", "Here be some text to render")
        node2 = HTMLNode("a", "Here be some text to render")
        self.assertEqual(node1, node2)

    def test_heq2(self):
        node1 = HTMLNode(tag1, val1, None, None)
        node2 = HTMLNode(tag1, val1, None, None)
        chkProp1 = node1.props_to_html()
        chkProp2 = node2.props_to_html()
        self.assertEqual(chkProp1, chkProp2)

    def test_heq3(self):
        node3 = HTMLNode(tag1, val1, chld1, prop1)
        node4 = HTMLNode(tag1, val1, chld1, prop1)
        self.assertEqual(node3, node4)

    def test_heq4(self):
        node5 = HTMLNode(tag2, val2, chld2, prop2)
        node6 = HTMLNode(tag2, val2, chld2, prop2)
        self.assertEqual(node5, node6)

    def test_Leq1(self):
        Lnode1 = LeafNode(tag1, val1)
        Lnode2 = LeafNode(tag1, val1)
        self.assertEqual(Lnode1, Lnode2)

    def test_Leq2(self):
        Lnode3 = LeafNode(tag2, val2, prop2)
        Lnode4 = LeafNode(tag2, val2, prop2)
        self.assertEqual(Lnode3, Lnode4)

    def test_Leq3(self):
        Lnode5 = LeafNode(tag1, val2, prop2)
        Lnode6 = LeafNode(tag1, val2, prop2)
        self.assertEqual(Lnode5, Lnode6)

if __name__ == "__main__":
    unittest.main()