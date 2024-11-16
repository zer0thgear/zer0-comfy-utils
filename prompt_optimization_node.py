import tiktoken


class PromptOptimizationNode:
    # Based fairly heavily on the tiktoken tokenizer from mnemic nodes
    @classmethod
    def INPUT_TYPES(self):
        encoders = ["gpt-4o", "gpt-4", "gpt-3.5-turbo", "o200k_base", "cl100k_base", "p50k_base", "r50k_base"]
        return {
            "required": {
                "input_string": ("STRING", {"default": "", "multiline": True}),
                "encoding_type": (encoders, {"default": "gpt-4o", "tooltip": "The encoding type to use for tokenization"}),
            },
            "optional": {
                "token_count": ("INT", {"default": 75, "min": 1, "tooltip": "The maximum prompt length before needing to be broken"}),
                "separator": ("STRING", {"default": " BREAK ", "tooltip": "The separator to use when chunking the prompt"})
            }
        }
    RETURN_TYPES = ("STRING", "STRING", "INT", "INT",)
    RETURN_NAMES = ("Optimized Prompt", "Chunked Prompt", "Token Count (Unoptimized)", "Token Count (Optimized)",)
    OUTPUT_TOOLTIPS = ("The prompt after stripping whitespace", "The prompt after stripping whitespace and splitting", "The token count of the unoptimized prompt", "The token count of the optimized prompt",)
    OUTPUT_IS_LIST = (False, False, False, False,)
    OUTPUT_NODE = True
    FUNCTION = "return_string"
    CATEGORY = "text utility"
    DESCRIPTION = "A node that optimizes whitespace in a prompt and optionally chunks the prompt tag-wise by token count with a specified prompt separator."
    def return_string(self, input_string, encoding_type, token_count=None, separator=None):
        try:
            if encoding_type in ["gpt-4o", "gpt-4", "gpt-3.5-turbo"]:
                tokenizer = tiktoken.encoding_for_model(encoding_type)
            else:
                tokenizer = tiktoken.get_encoding(encoding_type)
        except Exception as e:
            return (str(e), -1, -1,)
        pre_optimized_token_count = len(tokenizer.encode(input_string))
        split_prompt = list(map(lambda s: s.strip(),input_string.split(",")))
        optimized_prompt = ",".join(split_prompt)
        optimized_token_count = len(tokenizer.encode(optimized_prompt))
        final_chunked_prompt = ""
        if token_count is not None:
            tag_token_counts = list(map(lambda s: len(tokenizer.encode(f"{s},")), split_prompt))
            current_token_count = 0
            chunked_prompts = []
            current_chunk = []
            for i in range(len(split_prompt)):
                if current_token_count + tag_token_counts[i] < token_count:
                    current_chunk.append(split_prompt[i])
                    current_token_count += tag_token_counts[i]
                else:
                    chunked_prompts.append(",".join(current_chunk))
                    current_chunk = [split_prompt[i]]
                    current_token_count = tag_token_counts[i]
                if i == len(split_prompt) - 1:
                    chunked_prompts.append(",".join(current_chunk))
            final_chunked_prompt = f",{separator}".join(chunked_prompts)
        return (optimized_prompt, final_chunked_prompt, pre_optimized_token_count, optimized_token_count,)