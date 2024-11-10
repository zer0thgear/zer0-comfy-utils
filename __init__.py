from .multiline_string import MultilineStringNode
from .list_concat_node import ListConcatNode

NODE_CLASS_MAPPINGS = {
    "List Concat Node": ListConcatNode,
    "Multiline String Node": MultilineStringNode,
}

__all__ = ["NODE_CLASS_MAPPINGS"]