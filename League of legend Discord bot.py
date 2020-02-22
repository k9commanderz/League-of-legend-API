import discord
from discord.ext import commands
# from discord.ext.commands import CommandError
from Data.League.reaction_page import Reactions
from Data.embeds.ability_embed import AbilityEmbed
from Data.embeds.champion import ChampionEmbed
from Data.embeds.summoners import SummonerEmbed, servers

bot = commands.Bot(command_prefix='$')


class League_bot(commands.Cog):
    emojis = ['\N{wastebasket}','\N{crossed swords}','\N{open book}']

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'We have logged in as {self.bot.user}\n')



    # @commands.Cog.listener()
    # async def on_command_error(self, ctx, error):
    #     """
    #     Stop raising error for commands bugs to much
    #     """
    #     if isinstance(error, CommandError):
    #         return
    #     raise error

    @commands.command()
    async def summoner(self, ctx, server, *args):

        user = " ".join(args)

        if server.upper() not in servers:
            return await ctx.channel.send(
                "Please input server followed by summoner name\n$summoner <Server|EUW> <Username>\n"
                f"Servers available: [{','.join([p_holder for p_holder in servers])}]")
        elif not user:
            return await ctx.channel.send("Please input summoner name")

        summoner_embed = SummonerEmbed(server, user)

        if not summoner_embed.account_status:
            return await ctx.channel.send("Summoner not found")

        embed = discord.Embed.from_dict(summoner_embed.get_embed())

        await ctx.channel.send(embed=embed)

    @commands.command()
    async def ability(self, ctx, champion, ability):

        ability = AbilityEmbed(champion, ability)

        embed = discord.Embed.from_dict(ability.embed)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def champion(self, ctx, champion):

        champions = ChampionEmbed(champion)

        embed = discord.Embed.from_dict(champions.embed)

        champion_message = await ctx.channel.send(embed=embed)

        [await champion_message.add_reaction(emoji) for emoji in self.emojis]


if __name__ == "__main__":
    bot.add_cog(League_bot(bot))
    bot.add_cog(Reactions(bot))
    bot.run("")
