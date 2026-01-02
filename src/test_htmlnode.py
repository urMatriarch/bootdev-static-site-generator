import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    #Leaf Tests
    def test_leaf(self):
        node = LeafNode("tag", "value", "props")
        self.assertIsNone(node.children)
        self.assertEqual(str(node), "LeafNode(tag = tag, value = value, props = props)")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "Hello!")
        self.assertEqual(node.to_html(), "Hello!")

    #Parent Tests
    def test_parent(self):
        node = ParentNode("tag", "children", "props")
        self.assertIsNone(node.value)
        self.assertEqual(str(node), "ParentNode(tag = tag, children = children, props = props)")

    def test_parent_to_html_p(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        self.assertEqual(str(node.to_html()), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_to_html_with_grandchildren(self):
        grandchild = LeafNode("b", "grandchild")
        child = ParentNode("div", [grandchild])
        parent = ParentNode("span", [child], {"href": "https://www.google.com"})
        self.assertEqual(
            parent.to_html(),
            '<span href="https://www.google.com"><div><b>grandchild</b></div></span>'
        )


if __name__ == "__main__":
    unittest.main()