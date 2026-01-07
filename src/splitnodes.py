from htmlnode import HTMLNode

from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type.value != "text":
            new_nodes.append(node)
        else:    
            sub_nodes = node.text.split(delimiter)
            if len(sub_nodes) % 2 == 0:
                raise Exception("Improper markdown syntax. Be sure to enclose text in diliniators!")
            nodes_to_push = []
            for i in range(len(sub_nodes)):
                if i % 2 == 0:
                    new_node = TextNode(sub_nodes[i], TextType.TEXT)
                    nodes_to_push.append(new_node)
                else:
                    new_node = TextNode(sub_nodes[i], text_type)
                    nodes_to_push.append(new_node)
            new_nodes.extend(nodes_to_push)
            

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type.value != "text":
            new_nodes.append(node)
        else:
            sub_nodes = []
            matches = extract_markdown_images(node.text)
            if len(matches) == 0:
                pass
            else:
                for image in matches:
                    sections = node.text.split(f"![{image[0]}]({image[1]})", 1)
                    node.text = sections[1]
                    sub_nodes.append(TextNode(sections[0], TextType.TEXT))
                    sub_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                    sub_nodes.append(node)

            new_nodes.extend(sub_nodes)

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type.value != "text":
            new_nodes.append(node)
        else:
            sub_nodes = []
            matches = extract_markdown_links(node.text)
            if len(matches) == 0:
                pass
            else:
                for link in matches:
                    sections = node.text.split(f"[{link[0]}]({link[1]})", 1)
                    node.text = sections[1]
                    sub_nodes.append(TextNode(sections[0], TextType.TEXT))
                    sub_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                sub_nodes.append(node)

            new_nodes.extend(sub_nodes)
    return new_nodes