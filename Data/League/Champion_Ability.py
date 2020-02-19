from Data.League.Champions import Champion, version
from Data.Tools.Description_parser import Parser
from Data.Tools.Description_parser import removed_html


class Champion_ability(Champion):
    ability_coding = {"q": 0,
                      "w": 1,
                      "e": 2,
                      "r": 3,
                      "p": "passive"}
    __ability_gif = "https://storage.googleapis.com/champion_abilities"
    __ability_url = f"https://ddragon.leagueoflegends.com/cdn/{version}/img/spell/"
    __passive_url = f"https://ddragon.leagueoflegends.com/cdn/{version}/img/passive/"

    def __init__(self, champion_name, skill):
        super().__init__(champion_name)
        self.skill = skill.lower()
        if not self.ability_status:
            self.chosen_ability = self.ability_coding[self.skill]
            self.__champion_ability()


    @property
    def ability_status(self):
        return self.skill not in self.ability_coding

    def __champion_ability(self):
        if self.chosen_ability != 'passive':
            self.ability = self.champion_skills('spells')[self.chosen_ability]
            self.ability_name = self.ability['name']
            self.ability_cool_down = self.__ability_CD_Cost(self.ability['cooldownBurn'])
            self.ability_cost = self.__ability_CD_Cost(self.ability['costBurn'])
            self.ability_url = f"{self.__ability_url}{self.ability['image']['full']}"
        else:
            self.ability = self.champion_skills(self.chosen_ability)
            self.ability_name = self.ability['name']
            self.ability_url = f"{self.__passive_url}{self.ability['image']['full']}"

    @property
    def ability_gif(self):
        return f"{self.__ability_gif}/{self.key}_{self.skill.upper()}.gif"

    @property
    def ability_description(self):
        return removed_html(self.ability['description'])

    @property
    def ability_tooltip(self):
        """
        Removing unecessary details in the tool tip
        """
        if self.chosen_ability == 'passive':
            return False
        tooltip = removed_html(self.ability['tooltip'])
        effect = self.ability['effect']
        attributes = self.ability['vars']
        parsed = Parser(tooltip, effect, attributes)
        return parsed.new_description()

    def __ability_CD_Cost(self, ability):
        """
               Champion ability cool Down
               as well as Cost
        """
        if self.chosen_ability == 'passive':
            return False
        split_cool_down = ability.split('/')
        cool_down_stats = [f'Rank {stage}: {seconds}' if len(split_cool_down) > 1 else f'All rank: {seconds}' for
                           stage, seconds in enumerate(split_cool_down, 1)]
        return '\n'.join(cool_down_stats)

    @property
    def ability_range(self):
        """
        Ability Range
        """
        if self.chosen_ability == 'passive':
            return False
        split_ability_range = self.ability['rangeBurn'].split('/')
        ability__range = [f"Melee" if int(range) == 0 else range for range in split_ability_range]

        ability__range = '\n'.join(ability__range)

        try:
            if int(ability__range) == 1:
                ability__range = 'No Range'
        except ValueError:
            pass


        return ability__range
