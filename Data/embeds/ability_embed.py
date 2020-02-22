from Data.League.champion_ability import Champion_ability


class AbilityEmbed(Champion_ability):

    def __init__(self, champion_name, ability):
        super().__init__(champion_name, ability)

    @property
    def embed(self):

        embed = dict(
            title=f"{self.ability_name}",
            color=2470660,
            author={"name": f"{self.champion_name} {self.title.title()}",
                    "url": f"{self.profile_image}",
                    "icon_url": f"{self.profile_image}",
                    },


            footer = dict(
            text=f"The tooltip may be missing some information. Please refer to the respective champion's wiki page for further info."),
            thumbnail = {"url": self.ability_url},
            description = self.ability_description,
            image = {"url": self.ability_gif}
        )

        if self.chosen_ability == 'passive':
            pass

        else:
            embed['fields'] = [dict(name=":hourglass:**Cool Down**", value=self.ability_cool_down, inline=True),
                               dict(name=f"**Cost ({'Health' if self.energy_type == 'None' else self.energy_type})**",
                                    value=self.ability_cost, inline=True),
                               dict(name="**Target Range**", value=self.ability_range, inline=True),
                               ]

            if len(self.ability_tooltip) == 0:
                pass
            else:
                embed['fields'].append(dict(name="__**TOOL TIP**__", value=self.ability_tooltip, inline=False))

        return embed

