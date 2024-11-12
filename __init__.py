"""
@author: zer0gear
@title: zer0gear's Comfy Utilities
@nickname: zer0gear Comfy Utils
@description: Dubiously useful nodes that I've made for my own use.
"""

from .multiline_string import MultilineStringNode
from .list_combine_node import ListCombineNode

NODE_CLASS_MAPPINGS = {
    "List Combine Node (zer0)": ListCombineNode,
    "Multiline String Node (zer0)": MultilineStringNode,
}

__all__ = ["NODE_CLASS_MAPPINGS"]