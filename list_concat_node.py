class ListConcatNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_list": ("*", {}),
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
    def concat_list_with_separator(self, input_list, separator):
        return (separator[0].join(input_list),)