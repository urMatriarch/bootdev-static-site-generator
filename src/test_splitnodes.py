import unittest

from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNode(unittest.TestCase):
    def test_split_bold(self):
        testCase = [
            TextNode("This is a **bold** text **node**.", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(testCase, "**", TextType.BOLD)
        self.assertEqual("bold", new_nodes[1].text_type.value)
        self.assertEqual("bold", new_nodes[3].text_type.value)

    def test_split_at_end(self):
        testCase = [
            TextNode("This is a **bold**", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(testCase, "**", TextType.BOLD)
        self.assertEqual("bold", new_nodes[1].text_type.value)
        
    def test_split_italic(self):
        testCase = [
            TextNode("This is an _italic_ text node.", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(testCase, "_", TextType.ITALIC)
        self.assertEqual("italic", new_nodes[1].text_type.value)

    def test_split_code(self):
        testCase = [
            TextNode("this is a `code` text node.", TextType.TEXT)
        ]
        new_nodes = split_nodes_delimiter(testCase, "`", TextType.CODE)
        self.assertEqual("code", new_nodes[1].text_type.value)

    def test_multiple_nodes(self):
        testCase = [
            TextNode("This is a **bold** text node.", TextType.TEXT),
            TextNode("This is another bold text node.", TextType.BOLD),
            TextNode("This is a **third** text **node**.", TextType.TEXT),
            TextNode("This is an _italic_ text node.", TextType.TEXT)
        ]
        new_nodes_bold = split_nodes_delimiter(testCase, "**", TextType.BOLD)
        new_nodes_italic = split_nodes_delimiter(testCase, "_", TextType.ITALIC)
        new_nodes_full = split_nodes_delimiter(new_nodes_bold, "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes_bold), 10)
        self.assertEqual(len(new_nodes_italic), 6)
        self.assertEqual(len(new_nodes_full), 12)

if __name__ == "__main__":
    unittest.main()