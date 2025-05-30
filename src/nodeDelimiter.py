from textnode import *
from extractdata import *

# SPLIT TEXT NODES BASED ON TEXT DELIMITER INPUT TO SPECIFIED TEXTYPE
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

# SPLIT TEXT NODES WITH MARKDOWN IMAGES
def split_nodes_image(old_nodes):
    final_nodes = []
    for each in old_nodes:
        if each.text_type != TextType.NORMAL:
            final_nodes.append(each)
            continue
        node_txt = each.text
        extract_links = extract_markdown_images(node_txt)

        if len(extract_links) == 0:
            final_nodes.append(each)
            continue

        temp_nodes = []
        for data in extract_links:
            atxt, link = data

            if len(temp_nodes) > 0 and temp_nodes[0] != '':
                split_txt = temp_nodes[0].split(f"![{atxt}]({link})", 1)
                temp_nodes = [split_txt.pop()]

                if split_txt[0] == '':
                    final_nodes.append(TextNode(f"{atxt}", TextType.IMAGE, f"{link}"))
                    continue

                final_nodes.append(TextNode(split_txt[0], TextType.NORMAL))
                final_nodes.append(TextNode(f"{atxt}", TextType.IMAGE, f"{link}"))
                continue

            split_txt = node_txt.split(f"![{atxt}]({link})", 1)
            temp_nodes = [split_txt.pop()]

            if split_txt[0] == '':
                final_nodes.append(TextNode(f"{atxt}", TextType.IMAGE, f"{link}"))
                continue

            final_nodes.append(TextNode(split_txt[0], TextType.NORMAL))
            final_nodes.append(TextNode(f"{atxt}", TextType.IMAGE, f"{link}"))

        if len(temp_nodes) > 0 and temp_nodes[0] != '':
            final_nodes.append(TextNode(f"{temp_nodes[0]}", TextType.NORMAL))

    return final_nodes

# SPLIT TEXT NODES WITH MARKDOWN LINKS
def split_nodes_link(old_nodes):
    final_nodes = []
    for each in old_nodes:
        for each in old_nodes:
            if each.text_type != TextType.NORMAL:
                final_nodes.append(each)
                continue
        node_txt = each.text
        extract_links = extract_markdown_links(node_txt)

        if len(extract_links) == 0:
            final_nodes.append(each)
            continue

        temp_nodes = []
        for data in extract_links:
            atxt, link = data

            if len(temp_nodes) > 0 and temp_nodes[0] != '':
                split_txt = temp_nodes[0].split(f"[{atxt}]({link})", 1)
                temp_nodes = [split_txt.pop()]

                if split_txt[0] == '':
                    final_nodes.append(TextNode(f"{atxt}", TextType.LINK, f"{link}"))
                    continue

                final_nodes.append(TextNode(split_txt[0], TextType.NORMAL))
                final_nodes.append(TextNode(f"{atxt}", TextType.LINK, f"{link}"))
                continue

            split_txt = node_txt.split(f"[{atxt}]({link})", 1)
            temp_nodes = [split_txt.pop()]

            if split_txt[0] == '':
                final_nodes.append(TextNode(f"{atxt}", TextType.LINK, f"{link}"))
                continue

            final_nodes.append(TextNode(split_txt[0], TextType.NORMAL))
            final_nodes.append(TextNode(f"{atxt}", TextType.LINK, f"{link}"))

        if len(temp_nodes) > 0 and temp_nodes[0] != '':
            final_nodes.append(TextNode(f"{temp_nodes[0]}", TextType.NORMAL))

    return final_nodes

# COMBINE ALL SPLITTING FUNCTIONS TO SPLIT AN INPUT WITH MULTIPLE NODE TYPES INTO A LIST OF THEIR RESPECTIVE TEXTNODES
def text_to_textnode(text):
    to_node = [TextNode(text, TextType.NORMAL)]
    node_list= []

    link_split = split_nodes_link(to_node)
    image_split = split_nodes_image(link_split)
    bold_split = split_nodes_delimiter(image_split, mdBold, TextType.BOLD)
    italic_split = split_nodes_delimiter(bold_split, mdItalic, TextType.ITALIC)
    code_split = split_nodes_delimiter(italic_split, mdCode, TextType.CODE)

    node_list.extend(code_split)

    return node_list

# INPUT A RAW MARKDOWN STRING AND RETURN A LIST OF "BLOCK" STRINGS
def markdown_to_blocks(markdown):
    split_md = markdown.split('\n\n')
    strip_mdls = []
    for ea in split_md:
        if ea == '':
            continue
        strip_mdls.append(ea.strip())
    return strip_mdls

# TAKES A SINGLE BLOCK OF MARKDOWN TEXT AND RETURNS THE BlockType
def block_to_block_type(md_txt):
    split_txt = list(map(lambda x: x.strip(), md_txt.split("\n")))

    # Check if HEADING
    if check_if_heading(md_txt):
        return BlockType.H.value
    # Check if CODE
    if md_txt.startswith("```") and md_txt.endswith("```"):
        return BlockType.C.value
    # Check if QUOTE
    if all(line.startswith(">") for line in split_txt):
        return BlockType.Q.value
    # Check if UOL
    if all(line.startswith("- ") for line in split_txt):
        return BlockType.UOL.value
    # Check if OL
    if all(split_txt[i].startswith(f"{i+1}. ") for i in range(len(split_txt))):
        return BlockType.OL.value
    # Else PARAGRAPH
    return BlockType.P.value