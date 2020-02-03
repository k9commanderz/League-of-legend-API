import discord
from discord.ext import commands
# from discord.ext.commands import CommandError
from Data.League.Summoner import Summoner

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
        """
        $summoner <Server|EUW> <Username>
        """
        user = " ".join(args)
        summoner = Summoner(user)
        summoner_name, summoner_icon, summoner_level = summoner.get_account_profile()[0]
        total_champion, champions = summoner.summoners_mastery()
        summoners_rank = summoner.get_SR_Solo_ranked()

        embed = discord.Embed(
            title=f"{summoner_name.title()} |\\Level {summoner_level}/|",
            colour=2470660,
        )

        embed.set_footer(text="header")
        embed.set_thumbnail(url=summoner_icon)
        embed.add_field(name='**Summoner Stats**',
                        value=f":crossed_swords: Total Summoners Rift Games: **{summoner.rift_games}**"
                              f"\n:crossed_swords: Total Howling Abyss Games: **{summoner.aram_games}**"
                              f"\n:crossed_swords: Total Co-op Games:  **{summoner.coop_games}**\n",
                        inline=False)

        if not champions:  # check if the user has any masteries champions that this is for new accounts created
            embed.add_field(name="**Champion Masteries**",
                            value="Champion masteries not found"
                            ,
                            inline=True)
        else:
            first_champ, *other_champ = champions
            """
            Getting the top 3 masteries champions and return their name, level and points easier to add to embed
            instead of using index
            """

            f_name, f_level, f_point, f_last_played = first_champ
            if not other_champ:
                print("there are no more champions")
            else:
                second_champ, *third = other_champ
                s_name, s_level, s_point, s_last_played = second_champ
                if not third:
                    print("summoner does not have third champ")
                else:
                    t_name, t_level, t_point, t_last_played = third[0]

            embed.add_field(name="**Champion Masteries**",
                            value=f"|:white_small_square: **{f_name}**\n"
                                  f"|:white_small_square:** {'No Champion' if not second_champ else s_name}**\n"
                                  f"|:white_small_square:** {'No Champion' if not third else t_name}**\n"
                            ,
                            inline=True)

            embed.add_field(name="\u200b", value=f":beginner: Level {f_level}\n"
                                                 f":beginner: Level {'0' if not third else s_level}\n"
                                                 f":beginner: Level {'0' if not third else t_level}", inline=True)

            embed.add_field(name="\u200b", value=f":white_small_square:Points {f_point}\n"
                                                 f":white_small_square:Points {'0' if not third else s_point}\n"
                                                 f":white_small_square:Points {'None' if not third else t_point} ",
                            inline=True)

            if summoners_rank == "Unranked Summoner rift":
                embed.add_field(name="**Ranked Summary**", value="**Unranked**", inline=True)
            else:
                rank, promotion, win_rate = summoners_rank
                rank_mode, rank_title, rank_level, win, loss = rank
                win_percent, total_rank = win_rate
                rank_title = " ".join((rank_title.title(), rank_level))

                if len(promotion) <= 2:
                    league_point = f"|:white_small_square:**League Point:** {promotion}"
                elif int(promotion) > 100:
                    league_point = f"|:white_small_square:**League Point:** {promotion}"
                else:
                    league_point = f"|:white_small_square:**Promotion Series**\n{promotion['progress']} "

                embed.add_field(name="**Ranked Summary**",
                                value=f"|:white_small_square:**{rank_title}**\n"
                                      f"|:white_small_square:**Win** {win} \n"
                                      f"|:white_small_square:**Lost** {loss}\n"
                                      f"|:white_small_square:**Win Percentage** {win_percent}\n"
                                      f"{league_point}",
                                inline=True)

            if summoner.active == "No Active Game":
                embed.add_field(name="**:video_game: Game Status Summary**",
                                value="No Active Game",
                                inline=True)
            else:
                team, map_name, game_mode, summoner_spell, champion, game_length = summoner.active
                embed.add_field(name="**:video_game: Game Status Summary**",
                                value=f"[{game_mode.title()}](https://www.nomadfoods.com/wp-content/uploads/2018/08/placeholder-1-e1533569576673-960x960.png)\n"
                                      f"**Map**: {map_name}\n"
                                      f"**Team**: {team}\n"
                                      f"**Champion:** {champion}\n"
                                      f"**Spells:** {'/'.join(summoner_spell)}\n"
                                      f"**Game Time:** {game_length}",
                                inline=True)
        await ctx.channel.send(embed=embed)
    # else:
    #     await message.channel.send("Please type $league [<server|EUW>] [<Username>]")


bot.add_cog(League_bot(bot))

bot.run("")
