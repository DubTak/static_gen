class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag  # string representing HTML tag name
        self.value = value  # string representing value of HTML tag
        self.children = children  # list of HTMLNode objects representing children of this node
        self.props = props  # dict of k-v pairs representing attributes of HTML tag
        """
        An HTMLNode without a tag will just render as raw text
        An HTMLNode without a value will be assumed to have children
        An HTMLNode without children will be assumed to have a value
        An HTMLNode without props simply won't have any attributes
        """
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ''
        else:
            props_html = ''
            for k, v in self.props.items():
                props_html += f' {k}="{v}"'
            return props_html
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'