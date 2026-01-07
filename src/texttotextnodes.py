from textnode import TextType, TextNode

from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    text_nodes = []
    node = [TextNode(text, TextType.TEXT)]
    text_nodes.extend(
        split_nodes_link(
            split_nodes_image(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        split_nodes_delimiter(node, "**", TextType.BOLD), "_", TextType.ITALIC
                    ), "`", TextType.CODE
                )
            )
        )
    )

    return text_nodes