class ListCombineNode:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "input_list": ("*", {"tooltip": "The list of strings to concatenate"}),
                "combine_last_x_items": ("INT", {"default": 1, "min": 1, "max": 999, "tooltip": "If greater than 1, the last X items in the list will be combined before concatenating. Useful for correcting unnecessary separators."}),
                "separator": ("STRING", {"default": " BREAK ", "tooltip": "The separator to use when concatenating the list"}),
            }
        }
    @classmethod
    def VALIDATE_INPUTS(self, input_types):
        return True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Combined String",)
    OUTPUT_TOOLTIPS = ("The combined list as a single string",)
    INPUT_IS_LIST = True
    FUNCTION = "concat_list_with_separator"
    CATEGORY = "text utility"
    DESCRIPTION = "Combines a list of strings into a single string, separated by a provided separator."
    def combine_list_with_separator(self, input_list, combine_last_x_items, separator):
        # If combine_last_x_items is greater than 1, combine the last X items in the list
        if combine_last_x_items[0] > 1:
            input_list[-combine_last_x_items[0]:] = ["".join(input_list[-combine_last_x_items[0]:])]
        return (separator[0].join(input_list),)