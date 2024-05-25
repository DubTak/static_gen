from textnode import TextNode
from htmlnode import HTMLNode

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


main()