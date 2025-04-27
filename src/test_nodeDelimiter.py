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

    # ---- Test text_to_textnode function ----
    def test_t2tn_SingleBold(self):
        text1 = "This is some **bold** text"
        split_text1 = text_to_textnode(text1)
        self.assertListEqual(
            [
                TextNode("This is some ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.NORMAL)
            ], split_text1
        )

    def test_t2tn_DoubleBold(self):
        text2 = "This is **bold** text with more **bold text**"
        split_text2 = text_to_textnode(text2)
        self.assertListEqual(
            [
                TextNode('This is ', TextType.NORMAL), 
                TextNode('bold', TextType.BOLD), 
                TextNode(' text with more ', TextType.NORMAL), 
                TextNode('bold text', TextType.BOLD)
            ], split_text2
        )

    def test_t2tn_SingleLink(self):
        text3 = "Text with a single link: [link](somelink.com)"
        split_text3 = text_to_textnode(text3)
        self.assertListEqual(
            [
                TextNode('Text with a single link: ', TextType.NORMAL), 
                TextNode('link', TextType.LINK, 'somelink.com')
            ], split_text3
        )

    def test_t2tn_DoubleLinks(self):
        text4 = "Here we have two links: [link](link1.io) and [link](link2.gov)"
        split_text4 = text_to_textnode(text4)
        self.assertListEqual(
            [
                TextNode('Here we have two links: ', TextType.NORMAL), 
                TextNode('link', TextType.LINK, 'link1.io'), 
                TextNode(' and ', TextType.NORMAL), 
                TextNode('link', TextType.LINK, 'link2.gov')
            ], split_text4
        )

    def test_t2tn_SingleImage(self):
        text5 = "Here we have a single image: ![rando1](https://randomness.io/rando1.jpg)"
        split_text5 = text_to_textnode(text5)
        self.assertListEqual(
            [
                TextNode('Here we have a single image: ', TextType.NORMAL), 
                TextNode('rando1', TextType.IMAGE, 'https://randomness.io/rando1.jpg')
            ], split_text5
        )

    def test_t2tn_DoubleImage(self):
        text6 = "For two images: 1![cute cato](cutecats.org/cutecat1.png) and ![grumpy cato](cutecats.org/grumpy6.png)"
        split_text6 = text_to_textnode(text6)
        self.assertListEqual(
            [
                TextNode('For two images: 1', TextType.NORMAL), 
                TextNode('cute cato', TextType.IMAGE, 'cutecats.org/cutecat1.png'), 
                TextNode(' and ', TextType.NORMAL), 
                TextNode('grumpy cato', TextType.IMAGE, 'cutecats.org/grumpy6.png')
            ], split_text6
        )

    def test_t2tn_markdownMix(self):
        text7 = "This is no **images** _or_ **links** but a mix of `text markdown` in _random order_"
        split_text7 = text_to_textnode(text7)
        self.assertListEqual(
            [
                TextNode('This is no ', TextType.NORMAL), 
                TextNode('images', TextType.BOLD), 
                TextNode(' ', TextType.NORMAL), 
                TextNode('or', TextType.ITALIC), 
                TextNode(' ', TextType.NORMAL), 
                TextNode('links', TextType.BOLD), 
                TextNode(' but a mix of ', TextType.NORMAL), 
                TextNode('text markdown', TextType.CODE), 
                TextNode(' in ', TextType.NORMAL), 
                TextNode('random order', TextType.ITALIC)
            ], split_text7
        )

    def test_text_to_text_node(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        split_text = text_to_textnode(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ], split_text
        )

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