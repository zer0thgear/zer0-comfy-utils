class ListConcatNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_list": ("*", {}),
                "combine_last_three_items": (["FALSE", "TRUE"], {}),
                "separator": ("STRING", {"default": " BREAK "}),
            }
        }
    @classmethod
    def VALIDATE_INPUTS(cls, input_types):
        return True
    RETURN_TYPES = ("STRING",)
    INPUT_IS_LIST = True
    FUNCTION = "concat_list_with_separator"
    CATEGORY = "text utility"
    def concat_list_with_separator(self, input_list, combine_last_three_items, separator):
        # If combine_last_three_items is TRUE, combine the last three items in the list before concating
        if combine_last_three_items[0] == "TRUE":
            input_list[-3:] = ["".join(input_list[-3:])]
        return (separator[0].join(input_list),)