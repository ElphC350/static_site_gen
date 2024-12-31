from textnode import *

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
            if split_txt[i] == "":
                continue
            if i % 2 == 0:
                temp_nodes.append(TextNode(split_txt[i], TextType.NORMAL))
            else:
                temp_nodes.append(TextNode(split_txt[i], text_type))
        final_nodes.extend(temp_nodes)
    return final_nodes

# Pre-written vars for testing
txt_normal = "This is plain text"
txt_code = "This is text with a `code block` word"
txt_bold = "This is text with a **bold** word"
txt_italic = "This is text with an *italicized* word"
txt_link = "[link](https://imgur.com)"
txt_image = "![alt text](url/of/image.jpg)"
txt_bad = "This is missing **a matching delimiter"
txt_start = "**This** is bold at the beggining"