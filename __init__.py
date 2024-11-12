from .multiline_string import MultilineStringNode
from .list_concat_node import ListConcatNode

NODE_CLASS_MAPPINGS = {
    "List Concat Node (zer0)": ListConcatNode,
    "Multiline String Node (zer0)": MultilineStringNode,
}

__all__ = ["NODE_CLASS_MAPPINGS"]