import discord
from discord.ext import commands
# from discord.ext.commands import CommandError
from Data.Discord_data.SummonersEmbed import Summoner_embed, servers
import time

bot = commands.Bot(command_prefix='$')



class League_bot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.server = None

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
        start = time.time()
        """
        $summoner <Server> <Username>

        retrieve summoner profile their level, top 3 masteries and quick
        summary if they are in game o rnot and their rank

        """
        user = " ".join(args)

        if server.upper() not in servers:
            return await ctx.channel.send(
                "Please input server followed by summoner name\n$summoner <Server|EUW> <Username>\n"
                f"Servers available: [{','.join([p_holder for p_holder in servers])}]")
        elif not user:
            return await ctx.channel.send("Please input summoner name")

        summoner_embed = Summoner_embed(server, user)

        if not summoner_embed.account_status:
            return await ctx.channel.send("Summoner not found")

        embed = discord.Embed.from_dict(summoner_embed.get_embed())

        await ctx.channel.send(embed=embed)


if __name__ == "__main__":
    bot.add_cog(League_bot(bot))
    bot.run("")
