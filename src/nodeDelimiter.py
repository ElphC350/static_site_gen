from textnode import *

htm = {
    "normal": None,
    "bold": "**",
    "italic": "*",
    "code": "`",
    "link": "[link]",
    "image": "!["
}

def split_nodes_delimiter(old_nodes, delimiter, text_type):    
    final_nodes = []
    for each in old_nodes:
        if each.text_type != TextType.NORMAL:
            final_nodes.append(each)
            continue
        temp_nodes = []
        split_txt = each.text.split(delimiter)
        st_len = len(split_txt)

        if st_len % 2 == 0:
            raise Exception("Invalid markdown syntax")

        for i in range(st_len):
            temp_nodes.append(split_txt[i])
            print(temp_nodes)

'''
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
'''

txt_normal = "This is plain text"
txt_code = "This is text with a `code block` word"
txt_bold = "This is text with a **bold** word"
txt_italic = "This is text with an *italicized* word"
txt_link = "[link](https://imgur.com)"
txt_image = "![alt text](url/of/image.jpg)"
txt_bad = "This is missing **a matching delimiter"
txt_start = "**This** is bold at the beggining"

tst_node = TextNode(txt_bold, TextType.NORMAL)
tst = split_nodes_delimiter([tst_node], "**", TextType.BOLD)

start_node = TextNode(txt_start, TextType.NORMAL)
tst_start = split_nodes_delimiter([start_node], "**", TextType.BOLD)