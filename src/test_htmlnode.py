import unittest

from htmlnode import *
from vars import *

class TestHTMLNode(unittest.TestCase):
    def test_heq1(self):
        node1 = HTMLNode("a", "Here be some text to render")
        node2 = HTMLNode("a", "Here be some text to render")
        self.assertEqual(node1, node2)

    def test_heq2(self):
        node1 = HTMLNode(t_a, v_1, None, None)
        node2 = HTMLNode(t_a, v_1, None, None)
        chkProp1 = node1.props_to_html()
        chkProp2 = node2.props_to_html()
        self.assertEqual(chkProp1, chkProp2)

    def test_heq3(self):
        node3 = HTMLNode(t_a, v_1, c_1, p_1)
        node4 = HTMLNode(t_a, v_1, c_1, p_1)
        self.assertEqual(node3, node4)

    def test_heq4(self):
        node5 = HTMLNode(t_h1, v_2, c_2, p_2)
        node6 = HTMLNode(t_h1, v_2, c_2, p_2)
        self.assertEqual(node5, node6)

class TestLeafNode(unittest.TestCase):
    def test_Leq1(self):
        Lnode1 = LeafNode(t_a, v_1)
        Lnode2 = LeafNode(t_a, v_1)
        self.assertEqual(Lnode1, Lnode2)

    def test_Leq2(self):
        Lnode3 = LeafNode(t_h1, v_2, p_2)
        Lnode4 = LeafNode(t_h1, v_2, p_2)
        self.assertEqual(Lnode3, Lnode4)

    def test_Leq3(self):
        Lnode5 = LeafNode(t_a, v_2, p_2)
        Lnode6 = LeafNode(t_a, v_2, p_2)
        self.assertEqual(Lnode5, Lnode6)

class TestParentNode(unittest.TestCase):
    def test_Peq1(self):
        Pnode1 = ParentNode(t_a, lnodes, p_1)
        Pnode2 = ParentNode(t_a, lnodes, p_1)
        self.assertEqual(Pnode1, Pnode2)

    def test_Peq2(self):
        Pnode3 = ParentNode(t_a, pnodes, p_2)
        Pnode4 = ParentNode(t_a, pnodes, p_2)
        self.assertEqual(Pnode3, Pnode4)

    def test_Peq3(self):
        Pnode5 = ParentNode(t_h1, [])
        Pnode6 = ParentNode(t_h1, [])
        self.assertEqual(Pnode5, Pnode6)

if __name__ == "__main__":
    unittest.main()