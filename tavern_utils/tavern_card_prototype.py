class TavernCard:
    def __init__(self, card_info=None):
        self.name = card_info["name"] if card_info and "name" in card_info else ""
        self.description = card_info["description"] if card_info and "description" in card_info else ""
        self.personality = card_info["personality"] if card_info and "personality" in card_info else ""
        self.scenario = card_info["scenario"] if card_info and "scenario" in card_info else ""
        self.first_mes = card_info["first_mes"] if card_info and "first_mes" in card_info else ""
        self.mes_example = card_info["mes_example"] if card_info and "mes_example" in card_info else ""
        self.creator_notes = card_info["creator_notes"] if card_info and "creator_notes" in card_info else ""
        self.system_prompt = card_info["system_prompt"] if card_info and "system_prompt" in card_info else ""
        self.post_history_instructions = card_info["post_history_instructions"] if card_info and "post_history_instructions" in card_info else ""
        self.alternate_greetings = card_info["alternate_greetings"] if card_info and "alternate_greetings" in card_info else []
        self.character_book = card_info["character_book"] if card_info and "character_book" in card_info else {"name": "", "entries": []}
        self.tags = card_info["tags"] if card_info and "tags" in card_info else ""
        self.creator = card_info["creator"] if card_info and "creator" in card_info else ""
        self.character_version = card_info["character_version"] if card_info and "character_version" in card_info else ""
        self.extensions = card_info["extensions"] if card_info and "extensions" in card_info else ""

    def __repr__(self):
        return f"""name: {self.name},
description: {self.description},
personality: {self.personality},
scenario: {self.scenario},
first_mes: {self.first_mes},
mes_example: {self.mes_example},
creator_notes: {self.creator_notes},
system_prompt: {self.system_prompt},
post_history_instructions: {self.post_history_instructions},
alternate_greetings: {self.alternate_greetings},
character_book: {self.character_book},
tags: {self.tags},
creator: {self.creator},
character_version: {self.character_version},
extensions: {self.extensions}
"""

    def return_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "personality": self.personality,
            "scenario": self.scenario,
            "first_mes": self.first_mes,
            "mes_example": self.mes_example,
            "creator_notes": self.creator_notes,
            "system_prompt": self.system_prompt,
            "post_history_instructions": self.post_history_instructions,
            "alternate_greetings": self.alternate_greetings,
            "character_book": self.character_book,
            "tags": self.tags,
            "creator": self.creator,
            "character_version": self.character_version,
            "extensions": self.extensions
        }

    def return_basic_tuple(self):
        return (self.name, self.description, self.personality, self.scenario, self.first_mes, self.mes_example, self.creator_notes, self.creator, self.character_version)

    def return_full_tuple(self):
        return (self.name, self.description, self.personality, self.scenario, self.first_mes, self.mes_example, self.creator_notes, self.system_prompt, self.post_history_instructions, self.alternate_greetings, self.character_book, self.tags, self.creator, self.character_version, self.extensions)
    
def returnBasicOutputTypes():
    return ("STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "STRING")

def returnReadableBasicTupleNames():
    return ("Card Name", "Card Description", "Personality", "Scenario", "First Message", "Message Examples", "Creator Notes", "Author", "Version")