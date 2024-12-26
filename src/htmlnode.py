class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.TAG = tag
        self.VALUE = value
        self.CHILDREN = children
        self.PROPS = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        txt_rend = ""
        if (self.PROPS == None or len(self.PROPS) == 0):
            return txt_rend
        for each in self.PROPS:
            txt_rend = txt_rend + f' {each}="{self.PROPS[each]}"'
        return txt_rend
    
    def __eq__(self, other):
        return (self.TAG == other.TAG and self.VALUE == other.VALUE and self.CHILDREN == other.CHILDREN and self.PROPS == other.PROPS)
    
    def __repr__(self):
        return f"HTMLNode({self.TAG}, {self.VALUE}, {self.CHILDREN}, {self.PROPS})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
        
        if hasattr(self, 'children') and len(self.CHILDREN) > 0:
            raise ValueError("LeafNode instances do not allow for children")
        
        if self.VALUE == None:
            raise ValueError("LeafNode instance requires [value] attribute that is a string. e.g: ''")
        
    def to_html(self):
        if self.TAG == None:
            return f"{self.VALUE}"
        if self.PROPS == None:
            return f"<{self.TAG}>{self.VALUE}</{self.TAG}>"
        return f"<{self.TAG}{self.props_to_html()}>{self.VALUE}</{self.TAG}>"