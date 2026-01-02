class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        formatted = ""
        if self.props == None:
            return formatted
        for prop in self.props:
            formatted += f' {prop}="{self.props[prop]}"'
        return formatted
    
    def __repr__(self):
        return(f"HTMLNode(tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props})")
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNodes must have a value")
        if self.tag == None:
            return(self.value)
        return(f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>')
    
    def __repr__(self):
        return(f"HTMLNode(tag = {self.tag}, value = {self.value}, props = {self.props})")