from htmlnode import HTMLNode

from textnode import TextNode, TextType

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