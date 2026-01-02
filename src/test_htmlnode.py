import unittest

from htmlnode import HTMLNode, LeafNode

class TestTextNode(unittest.TestCase):
    def test_propstohtml(self):
        testCase = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=testCase)
        self.assertEqual(' href="https://www.google.com" target="_blank"', node.props_to_html())

    def test_repr(self):
        node = HTMLNode("beans", "boop", ['beans', 'boop'], {'beans':'boop'})
        self.assertEqual("HTMLNode(tag = beans, value = boop, children = ['beans', 'boop'], props = {'beans': 'boop'})", str(node))

    def test_leaf(self):
        node = LeafNode("tag", "value", "props")
        self.assertIsNone(node.children)
        self.assertEqual(str(node), "HTMLNode(tag = tag, value = value, props = props)")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "Hello!")
        self.assertEqual(node.to_html(), "Hello!")


if __name__ == "__main__":
    unittest.main()