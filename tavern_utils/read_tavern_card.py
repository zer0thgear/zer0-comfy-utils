import base64
import json
import os

from PIL import Image

import folder_paths
import node_helpers

from .tavern_card_prototype import returnBasicOutputTypes, returnReadableBasicTupleNames, TavernCard

class ReadTavernCardNode:
    @classmethod
    def INPUT_TYPES(self):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f)) and f.endswith(".png")]
        return {
            "required": {
                "image": (sorted(files), {"image_upload": True}),
            },
        }
    RETURN_TYPES = returnBasicOutputTypes()
    RETURN_NAMES = returnReadableBasicTupleNames()
    OUTPUT_TOOLTIPS = ("Card info in the form of strings.",)
    INPUT_IS_LIST = True
    FUNCTION = "return_card_info"
    CATEGORY = "utility"
    DESCRIPTION = "Returns tavern card metadata."
    def return_card_info(self, image):
        image_path = folder_paths.get_annotated_filepath(image[0])
        img = node_helpers.pillow(Image.open, image_path)
        card_info = json.loads(base64.b64decode(img.text["chara"]))["data"]
        parsed_card = TavernCard(card_info)
        #prompt_json = json.loads(img.text["prompt"])
        return parsed_card.return_basic_tuple() #(list(prompt_json.values()),)