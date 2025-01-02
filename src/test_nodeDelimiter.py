import unittest

from nodeDelimiter import *

class TestNodeDelimiter(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.NORMAL
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.NORMAL),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.NORMAL
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.NORMAL),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL),
            ],
            new_nodes,
        )

    # ---- Test split_node LINKS ----
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and here is some text after",
            TextType.NORMAL
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.NORMAL), 
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"), 
                TextNode(" and ", TextType.NORMAL), 
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"), 
                TextNode(" and here is some text after", TextType.NORMAL)
            ], new_nodes
        )

    def test_split_link_single(self):
        node = TextNode("[to inf](www.andbeyond.cosmos)", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("to inf", TextType.LINK, "www.andbeyond.cosmos")
            ], new_nodes
        )

    def test_split_links_only(self):
        node = TextNode("[nsfw1](http://thefourthchan.rip)[nsfw2](mydiscord.gg)", TextType.NORMAL)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("nsfw1", TextType.LINK, "http://thefourthchan.rip"),
                TextNode("nsfw2", TextType.LINK, "mydiscord.gg")
            ], new_nodes
        )

    # ---- Test split_node IMAGES ----
    def test_split_node_images(self):
        node = TextNode(
            "This is text with an image of ![boot dev](https://www.boot.dev) and ![a cat](https://www.cat.jpg) and here is some text after",
            TextType.NORMAL
        )
        new_node = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an image of ", TextType.NORMAL), 
                TextNode("boot dev", TextType.IMAGE, "https://www.boot.dev"), 
                TextNode(" and ", TextType.NORMAL), 
                TextNode("a cat", TextType.IMAGE, "https://www.cat.jpg"), 
                TextNode(" and here is some text after", TextType.NORMAL)
            ], new_node
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images_only(self):
        node2 = TextNode(
            "![image1](https://www.example1.COM/IMAGE1.PNG)![image2](https://www.example2.COM/IMAGE2.PNG)",
            TextType.NORMAL,
        )
        new_nodes2 = split_nodes_image([node2])
        self.assertListEqual(
            [
                TextNode("image1", TextType.IMAGE , "https://www.example1.COM/IMAGE1.PNG"), 
                TextNode("image2", TextType.IMAGE, "https://www.example2.COM/IMAGE2.PNG")
             ], new_nodes2
        )

if __name__ == "__main__":
    unittest.main()