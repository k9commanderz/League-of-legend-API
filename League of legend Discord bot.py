import discord
from discord.ext import commands
#from discord.ext.commands import CommandError
from threading import Thread
from Summoner import Summoner

bot = commands.Bot(command_prefix='$')


class League_bot(commands.Cog):

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
    async def summoner(self, ctx, server, user):
        summoner = Summoner(user)
        summoner_name, summoner_icon, summoner_level = summoner.get_account_profile()[0]
        first_champ, second_champ, third_champ = summoner.summoners_mastery()[1]

        # summoner_rank, rank_promo, win_percentage = summoner.get_SR_Solo_ranked()
        #
        # win, lose = summoner_rank[3:]
        #summoner_rank = f"{summoner_rank[1]} {summoner_rank[2]}"

        embed = discord.Embed(
            title=f"{summoner_name.title()} |\\Level {summoner_level}/|",
            colour=2470660,
        )
        embed.set_footer(text="header")
        embed.set_thumbnail(url=summoner_icon)
        embed.add_field(name='**Summoner Stats**',
                        value=f":crossed_swords: Total Summoners Rift Games: **{summoner.getMatchHistoryRift()}**\n:crossed_swords: Total Howling "
                              f"Abyss Games: **{summoner.getMatchHistoryARAM()}**\n:crossed_swords: Total Co-op Games:  **Place Holder**\n", inline=False)
        embed.add_field(name="**Champion Masteries**",
                        value=f"|:white_small_square: {first_champ[0]}:beginner: Level{first_champ[1]} -  {first_champ[2]:02,} Points \n|:white_small_square:"
                              f" {second_champ[0]}:beginner:Level {second_champ[1]}-  {second_champ[2]:02,} Points\n|:white_small_square: {third_champ[0]}:beginner:Level {third_champ[1]} -  {third_champ[2]:02,} Points ",
                        inline=False)
        # embed.add_field(name="**Ranked Summary**",
        #                 value=f"|:white_small_square:**{summoner_rank.title()}**\n|:white_small_square:**Win:** {win} \n|:white_small_square:**Lost:** {lose}\n|:white_small_square:**Win Percentage:** {win_percentage[0]}%\n|:white_small_square:**League Point:** {rank_promo} / 100",
        #                 inline=True)
        embed.add_field(name="**Game Status Summary**",
                        value="place holder",
                        inline=True)
        await ctx.channel.send(embed=embed)
    # else:
    #     await message.channel.send("Please type $league [<server|EUW>] [<Username>]")


bot.add_cog(League_bot(bot))

bot.run("")
