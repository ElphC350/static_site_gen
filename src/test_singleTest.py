import unittest

from nodeDelimiter import *

class TestSingleFunction(unittest.TestCase):
    # ---- Test text_to_textnode function ----
    def test_SingleBold(self):
        text1 = "This is some **bold** text"
        split_text1 = text_to_textnode(text1)
        self.assertListEqual(
            [
                TextNode("This is some ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.NORMAL)
            ], split_text1
        )

    def test_DoubleBold(self):
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

    def test_SingleLink(self):
        text3 = "Text with a single link: [link](somelink.com)"
        split_text3 = text_to_textnode(text3)
        self.assertListEqual(
            [
                TextNode('Text with a single link: ', TextType.NORMAL), 
                TextNode('link', TextType.LINK, 'somelink.com')
            ], split_text3
        )

    def test_DoubleLinks(self):
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

    def test_SingleImage(self):
        text5 = "Here we have a single image: ![rando1](https://randomness.io/rando1.jpg)"
        split_text5 = text_to_textnode(text5)
        self.assertListEqual(
            [
                TextNode('Here we have a single image: ', TextType.NORMAL), 
                TextNode('rando1', TextType.IMAGE, 'https://randomness.io/rando1.jpg')
            ], split_text5
        )

    def test_DoubleImage(self):
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

    def test_markdownMix(self):
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

if __name__ == "__main__":
    unittest.main()