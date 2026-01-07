import unittest

from texttotextnodes import text_to_textnodes

class TestTextToTextNode(unittest.TestCase):
    def test_no_errors(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        print(text_to_textnodes(text))

if __name__ == "__main__":
    unittest.main()