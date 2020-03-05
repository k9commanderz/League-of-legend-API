from discord.ext import commands
import discord
from Data.embeds.champion_lore import LoreEmbed
from Data.embeds.champion import ChampionEmbed
from Data.embeds.champion_builds import ChampionBuildEmbed
from Data.League.champion import championData


class Reactions(commands.Cog):
    emojis = ['\N{open book}', '\N{shield}']

    def __init__(self, bot):
        self.bot = bot
        self.book_navigation = ['\N{black left-pointing triangle}',
                                '\N{black right-pointing triangle}',
                                ]

        self.reaction = None

    def book(self, champion_id):
        pass


    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        users = await reaction.users().flatten()

        self.reaction = reaction

        def exact_id_from_colour(colour):
            # page number champion id
            return int(str(reaction.message.embeds[0].colour.value)[-1]), \
                   str(reaction.message.embeds[0].colour.value)[3:][:-1]

        if user != self.bot.user and self.bot.user in users:

            # champion id stored in the red
            page_number, champion_id = exact_id_from_colour(reaction.message.embeds[0].colour)

            lore = LoreEmbed(champion_id)



            # ▶
            # ◀

            if reaction.emoji == "▶" and page_number < lore.total_pages:


                lore.page_number = page_number + 1

                embed = discord.Embed.from_dict(lore.embed)

                message = await reaction.message.edit(embed=embed)

                await reaction.remove(user)
            else:
                await reaction.remove(user)

            if reaction.emoji == "◀" and page_number != 1:

                lore.page_number = page_number - 1

                embed = discord.Embed.from_dict(lore.embed)

                message = await reaction.message.edit(embed=embed)

                await reaction.remove(user)
            else:
                await reaction.remove(user)



            if reaction.emoji == "📖":



                await reaction.remove(user)



                embed = discord.Embed.from_dict(lore.embed)

                message = await reaction.message.edit(embed=embed)

                # check the number of pages the lore book has if it's greater than 1 then add navigator
                if len(lore.pages_content) > 1:
                    [await reaction.message.add_reaction(emoji) for emoji in self.book_navigation]
                    await reaction.message.add_reaction('\N{shield}')
                else:
                    await reaction.message.add_reaction('\N{shield}')

                await reaction.message.remove_reaction(reaction.emoji, self.bot.user)

            elif reaction.emoji == "🛡":

                champion_name_id = champion_data[champion_id]['id'].lower()

                await reaction.remove(user)

                champions = ChampionEmbed(champion_name_id)

                embed = discord.Embed.from_dict(champions.embed)

                message = await reaction.message.edit(embed=embed)
                await reaction.message.add_reaction('\N{open book}')
                [await reaction.message.remove_reaction(emoji, self.bot.user) for emoji in self.book_navigation]
                await reaction.message.remove_reaction(reaction.emoji, self.bot.user)


            elif reaction.emoji == "⚔" and page_number != 9:

                page_number = str(reaction.message.embeds[0].colour.value)[-1]
                test = str(reaction.message.embeds[0].colour.value)[3:][:-1]

                build = ChampionBuildEmbed(champion_id)

                embed = discord.Embed.from_dict(build.embed)
                await reaction.remove(user)
                message = await reaction.message.edit(embed=embed)
                [await reaction.message.remove_reaction(emoji, self.bot.user) for emoji in self.book_navigation]
                [await reaction.message.add_reaction(emoji) for emoji in self.emojis]

            elif reaction.emoji == "⚔" and page_number == 9:
                await reaction.remove(user)


            elif reaction.emoji == "🗑":
                await reaction.remove(user)
                await reaction.message.delete()


