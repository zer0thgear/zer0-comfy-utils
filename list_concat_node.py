class ListConcatNode:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "input_list": ("*", {"tooltip": "The list of strings to concatenate"}),
                "combine_last_three_items": (["FALSE", "TRUE"], {"tooltip": "If TRUE, the last three items in the list will be combined before concatenating, useful for when using LORAs"}),
                "separator": ("STRING", {"default": " BREAK ", "tooltip": "The separator to use when concatenating the list"}),
            }
        }
    @classmethod
    def VALIDATE_INPUTS(self, input_types):
        return True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Concatenated String",)
    OUTPUT_TOOLTIPS = ("The concatenated list as a single string",)
    INPUT_IS_LIST = True
    FUNCTION = "concat_list_with_separator"
    CATEGORY = "text utility"
    def concat_list_with_separator(self, input_list, combine_last_three_items, separator):
        # If combine_last_three_items is TRUE, combine the last three items in the list before concating
        if combine_last_three_items[0] == "TRUE":
            input_list[-3:] = ["".join(input_list[-3:])]
        return (separator[0].join(input_list),)