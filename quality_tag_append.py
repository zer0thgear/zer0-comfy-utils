class QualityTagAppendNode:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "string_one": ("STRING", {"tooltip": "The first string to be combined", "defaultInput": True}),
                "string_two": ("STRING", {"tooltip": "The second string to be combined", "defaultInput": True}),
                "separator": ("STRING", {"default": ", ", "tooltip": "The separator to use when combining the strings"}),
            }
        }
    @classmethod
    def VALIDATE_INPUTS(self, input_types):
        return True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Combined String",)
    INPUT_IS_LIST = (False)
    OUTPUT_TOOLTIPS = ("The combined strings as a single string",)
    FUNCTION = "combine_strings_with_separator"
    CATEGORY = "text utility"
    DESCRIPTION = "Combines two strings into a single string, separated by a provided separator."
    def combine_strings_with_separator(self, string_one, string_two, separator):
        return (separator.join([string_one, string_two]),)