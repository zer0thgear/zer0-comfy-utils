from .multiline_string import MultilineStringNode
from .list_combine_node import ListCombineNode

NODE_CLASS_MAPPINGS = {
    "List Combine Node (zer0)": ListCombineNode,
    "Multiline String Node (zer0)": MultilineStringNode,
}

__all__ = ["NODE_CLASS_MAPPINGS"]