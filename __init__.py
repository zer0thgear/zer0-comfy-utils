"""
@author: zer0gear
@title: zer0gear's Comfy Utilities
@nickname: zer0gear Comfy Utils
@description: Dubiously useful nodes that I've made for my own use.
"""

from .multiline_string import MultilineStringNode
from .list_combine_node import ListCombineNode
from .prompt_optimization_node import PromptOptimizationNode
from .tavern_utils.read_tavern_card import ReadTavernCardNode
from .tavern_utils.write_tavern_card import WriteTavernCardNode

NODE_CLASS_MAPPINGS = {
    "List Combine Node (zer0)": ListCombineNode,
    "Multiline String Node (zer0)": MultilineStringNode,
    "Prompt Minimizer And Splitter Node (zer0)": PromptOptimizationNode,
    "Tavern Card Info Node (zer0)": ReadTavernCardNode,
    "Tavern Card Creation Node (zer0)": WriteTavernCardNode,
}

__all__ = ["NODE_CLASS_MAPPINGS"]