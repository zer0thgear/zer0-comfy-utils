import base64
import json
import os

import numpy as np
from PIL import Image
from PIL.PngImagePlugin import PngInfo

import folder_paths

from .tavern_card_prototype import TavernCard

class WriteTavernCardNode:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.compress_level = 4

    @classmethod
    def INPUT_TYPES(self):
        return {
            "required": {
                "image": ("IMAGE", {"tooltip": "The image to be displayed on the tavern card."}),
                "filename": ("STRING", {"default": "tavern_card", "tooltip": "The filename to save the tavern card as."}),
                "card_name": ("STRING", {"default": "",}),
                "card_description": ("STRING", {"default": "", "multiline": True}),
                "personality": ("STRING", {"default": "",}),
                "scenario": ("STRING", {"default": "",}),
                "first_message": ("STRING", {"default": "", "multiline": True}),
                "message_examples": ("STRING", {"default": "", "multiline": True}),
                "creator_notes": ("STRING", {"default": "", "multiline": True}),
                "author": ("STRING", {"default": "",}),
                "version": ("STRING", {"default": "",}),
            }
        }
    RETURN_TYPES = ()
    FUNCTION = "create_tavern_card"
    CATEGORY = "utility"
    OUTPUT_NODE = True
    DESCRIPTION = "Saves a created tavern card as a PNG."
    def create_tavern_card(self, image, filename, card_name, card_description, personality, scenario, first_message, message_examples, creator_notes, author, version):
        full_output_folder, filename, _, subfolder, _ = folder_paths.get_save_image_path(filename, self.output_dir, image[0].shape[1], image[0].shape[0])
        i = 255. * image[0].cpu().numpy()
        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

        card_info = {
            "name": card_name,
            "description": card_description,
            "personality": personality,
            "scenario": scenario,
            "first_mes": first_message,
            "mes_example": message_examples,
            "creator_notes": creator_notes,
            "creator": author,
            "character_version": version,
        }

        card = TavernCard(card_info)
        metadata = PngInfo()
        metadata.add_text("chara", base64.b64encode(json.dumps({"data": card.return_dict()}).encode("ascii")))
        file = f"{filename}.png"
        img.save(os.path.join(full_output_folder, file), pnginfo=metadata, compress_level=self.compress_level)
        return {"ui": {"images": [{"filename": file, "subfolder": subfolder, "type": self.type}]}}