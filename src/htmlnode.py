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
        raise NotImplementedError('to_html method not implemented')
    
    def props_to_html(self):
        if self.props is None:
            return ''
        else:
            props_html = ''
            for k, v in self.props.items():
                props_html += f' {k}="{v}"'
            return props_html
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError('Invalid HTML: no value')
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('Invalid HTML: no tag')
        if self.children is None:
            raise ValueError('Invalid HTML: no children')
        children_html = ''
        for child in self.children:
            children_html += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'
    
    def __repr__(self):
        return f'ParentNode({self.tag}, children: {self.children}, {self.props})'