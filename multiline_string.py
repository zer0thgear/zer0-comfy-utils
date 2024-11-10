class MultilineStringNode:
    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "input_string": ("STRING", {"default": "", "multiline": True}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Output",)
    OUTPUT_TOOLTIPS = ("The multiline string",)
    INPUT_IS_LIST = True
    FUNCTION = "return_string"
    CATEGORY = "text utility"
    def return_string(self, input_string):
        return (input_string[0],)