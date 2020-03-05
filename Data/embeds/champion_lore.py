from Data.League.champion import ChampionLore
import discord.colour


class LoreEmbed(ChampionLore):

    def __init__(self, champion_id):
        super().__init__(champion_id)
        self.page_number = 1

        self.pages_content = {1: '\n\n'.join(self.biography[0:4]),
                              }
        self.pages()

        self.total_pages = len(self.pages_content)

    def pages(self):
        if '\n\n'.join(self.biography[4:8]):
            self.pages_content.update({2: '\n\n'.join(self.biography[4:8])})
            if '\n\n'.join(self.biography[8:]):
                self.pages_content.update({3: '\n\n'.join(self.biography[8:])})
        else:
            pass

    @property
    def embed(self):

        description_page = f"Page {self.page_number} of " if len(self.pages_content) > 1 else ""
        embed = dict(
            color=self.colour,
            title=f"{self.name} {self.title.title()}",
            thumbnail={"url": self.profile_image},
            description=f"**{description_page}{self.name}'s biography**"
                        f"\n\n{self.pages_content[self.page_number]}",

        )
        return embed

    @property
    def colour(self):
        return int(f"249{self.champion_id}{self.page_number}")
