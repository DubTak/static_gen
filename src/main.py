from textnode import TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode

def main():
    test_node = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    print(test_node)

    test_html_node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
    print(test_html_node)
    print(f'Testing .props_to_html: {test_html_node.props_to_html()}')

    test_leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(test_leaf_node)
    print(f'Testing .to_html(): {test_leaf_node.to_html()}')

    test_parent_node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
    print(test_parent_node)
    print(f'Testing .to_html(): {test_parent_node.to_html()}')



main()