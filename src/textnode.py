from enum import Enum
from vars import *
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL = None
    BOLD = "b"
    ITALIC = "i"
    CODE = "code"
    LINK = "a"
    IMAGE = "img"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (
            self.text == other.text
            and self.text_type.value == other.text_type.value
            and self.url == other.url
            ):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):

    match(text_node.text_type):
        case TextType.NORMAL | TextType.BOLD | TextType.ITALIC | TextType.CODE:
            return LeafNode(text_node.text_type.value, text_node.text)
        case TextType.LINK:
            return LeafNode(TextType.LINK.value, text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(TextType.IMAGE.value, "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("[text_type] must be a valid TextType")

# Pre-written list for testing   
tests = [
    TextNode("some basic beach text", TextType.NORMAL),
    TextNode("some basic beach text", TextType.BOLD),
    TextNode("some basic beach text", TextType.ITALIC),
    TextNode("some basic beach text", TextType.CODE),
    TextNode("some basic beach text", TextType.LINK, "https://alink.com"),
    TextNode("some basic beach text", TextType.IMAGE, "https://picture.img")
]