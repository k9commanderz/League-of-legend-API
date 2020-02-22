from Data.League.champion import ChampionBaseStats
import discord.colour


class ChampionEmbed(ChampionBaseStats):

    def __init__(self, champion_name):
        super().__init__(champion_name)
        self.champion_store_details()

    @property
    def embed(self):




        embed = dict(
            color=self.colour,

            title=f"{self.name} {self.title.title()}",
            thumbnail={"url": self.profile_image},
            fields =[
                dict(name="**Champion Info**", value=f":white_small_square:**Price** \n:small_blue_diamond: Blue Essence: {self.blue_essence} \n:small_blue_diamond: Riot Point: {self.riot_point}\n"
                                                     f":white_small_square: **Total Skin**: {self.total_skins}\n"
                                                     f":white_small_square: **Release Date**: {self.release_date}", inline=False),
                dict(name="**Base Statistics**", value=f":white_small_square: Health\n"
                                                       ":white_small_square: Health Regen\n"
                                                       f":white_small_square: {self.energy_type}\n"
                                                       f":white_small_square: {self.energy_type} Regen\n"
                                                       f":white_small_square: Armour\n"
                                                       f":white_small_square: Attack Damage\n"
                                                       f":white_small_square: Attack Speed\n"
                                                       f":white_small_square: Attack Range\n"
                                                       f":white_small_square: Magic Resistance\n"
                                                       f":white_small_square: Movement Speed\n", inline=True),

                dict(name="**\u200b**", value=f":beginner: {self.health}\n"
                                              f":beginner: {self.health_regen}\n"
                                              f":beginner: {self.energy_cost}\n"
                                              f":beginner: {self.energy_regen}\n"
                                              f":beginner: {self.armour}\n"
                                              f":beginner: {self.attack_damage}\n"
                                              f":beginner: {self.attack_speed}\n"
                                              f":beginner: {self.attack_range}\n"
                                              f":beginner: {self.magic_resist}\n"
                                              f":beginner: {self.movement_speed}\n", inline=True),


                dict(name="**Background**", value=f"{self.lore} (BUILT IN FULL BIOGRAPHY in progress)"),

            ],



        )


        return embed

    @property
    def colour(self):

        return int(f"249{self.champion_id}0")

