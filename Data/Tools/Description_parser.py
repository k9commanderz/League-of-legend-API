import re


def removed_html(word):
    return re.sub('<.*?>', '', word)


class Parser:

    def __init__(self, description, *args):
        self.description = removed_html(description)  # removes html tags
        self.asset = args

    def new_description(self):
        self.__effects()
        self.__key_attributes()
        self.__polish()
        return self.description

    def __polish(self):
        self.description = re.sub("[(]?[+]?{{\s\w\d\s}}[)]?", '', self.description)
        self.description = re.sub("{{.+?}}", '', self.description)
        return self.description

    def keyword_effects(self):
        return re.findall(r"[a-z]\d", self.description, re.IGNORECASE)

    def __effects(self):
        """
        Get a dictonary of the effects for the given data

        replacing their values with according to their key value

        """

        key_words = self.keyword_effects()

        effect, _ = self.asset
        effects = {f"e{key}": value[0] for key, value in enumerate(effect) if value is not None}

        for key in key_words:
            if key in effects:
                self.description = self.description.replace(f"{{{{ {key} }}}}", str(effects[key]))

    def __key_attributes(self):
        """
                Get a dictonary of the effects for the given data

                replacing their values with according to their key value

                """

        _, attributes = self.asset
        attributes = {key['key']: key['coeff'] for key in attributes}
        for attribute, value in attributes.items():
            if type(value) is list:
                value = f"{int(value[0] * 100)}%"
                self.description = self.description.replace(f"{{{{ {attribute} }}}}", value)
            else:
                value = f"{int(value * 100)}%"
                self.description = self.description.replace(f"{{{{ {attribute} }}}}", value)
