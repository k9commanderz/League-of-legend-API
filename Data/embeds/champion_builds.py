from Data.League.champion import ChampionBuild
import discord.colour


class ChampionBuildEmbed(ChampionBuild):

    def __init__(self, champion_id):
        super().__init__(champion_id)



    @property
    def embed(self):


        embed = dict(
            color=self.colour,
            title=f"{self.name} {self.title.title()}",
            thumbnail={"url": self.profile_image},
            description = "**Champion build**"

        )
        return embed

    @property
    def colour(self):
        return int(f"249{self.champion_id}9")