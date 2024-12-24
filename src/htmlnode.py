class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.TAG = tag
        self.VALUE = value
        self.CHILDREN = children
        self.PROPS = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return f"{self.PROPS.value}"
    
    def __repr__(self):
        return f"HTMLNode({self.TAG}, {self.VALUE}, {self.CHILDREN}, {self.PROPS})"