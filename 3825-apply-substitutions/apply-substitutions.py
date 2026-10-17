class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        map = {key:val for key, val in replacements}

        while '%' in text:
            text_list = []
            keys = text.split("%")
            for key in keys:
                if key in map:
                    text_list.append(map[key])
                else:
                    text_list.append(key)
            text = "".join(text_list)
        return text
