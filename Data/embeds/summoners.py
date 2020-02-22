from Data.League.Summoner import Summoner, servers


class SummonerEmbed(Summoner):

    def __init__(self, server, user):
        self.user = user
        self.server = servers[server.upper()]
        super().__init__(self.user, self.server)
        self.embed = None

    def __accounts(self):

        self.summoner_name, self.summoner_icon, self.summoner_level = self.get_account_profile()[0]
        self.total_champion, self.champions = self.summoners_mastery()
        self.summoners_rank = self.get_SR_Solo_ranked()

    def get_embed(self):
        """

        :return:
        """
        self.__accounts()

        self.embed = dict(
            title=f"{self.summoner_name.title()} |\\Level {self.summoner_level}/|",
            color=2470660,
            footer=dict(text="Place Holder"),
            thumbnail=dict(url=self.summoner_icon),

        )
        self.__total_games_embed()
        self.__champion_embed()
        self.__champion_level_embed()
        self.__champion_points_embed()
        self.__rank_embed()
        self.__game_summary()

        return self.embed

    def __total_games_embed(self):
        """
        total games field
        :return:
        """
        fields = [dict(name='**Summoner Stats**',
                       value=f":crossed_swords: Total Summoners Rift Games: **{self.rift_games}**"
                             f"\n:crossed_swords: Total Howling Abyss Games: **{self.aram_games}**"
                             f"\n:crossed_swords: Total Co-op Games:  **{self.coop_games}**\n",
                       inline=False

                       )

                  ]

        self.embed['fields'] = fields

    def __champion_embed(self):

        if not self.champions:  # check if the user has any masteries champions that this is for new accounts created
            mastery_field = dict(name="**Champion Masteries**",
                                 value="Champion masteries not found",
                                 inline=True)
            self.embed['fields'].append(mastery_field)
        else:
            first_champ, *other_champ = self.champions.items()
            """
            Getting the top 3 masteries champions and return their name, level and points easier to add to embed
            instead of using index
            """
            self.first_name = first_champ[0]
            self.first_level, self.first_point, self.first_last_played = first_champ[1]

            if not other_champ:
                print("there are no more champions")
            else:
                self.second_champ, *self.third_champ = other_champ
                self.second_name = self.second_champ[0]
                self.second_level, self.second_point, second_last_played = self.second_champ[1]

                if not self.third_champ:
                    print("summoner does not have third champ")
                else:
                    self.third_champ= self.third_champ[0]
                    self.third_name = self.third_champ[0]
                    self.third_level, self.third_point, self.third_last_played = self.third_champ[1]

                mastery_field = dict(name="**Champion Masteries**",
                                     value=f"|:white_small_square: **{self.first_name}**\n"
                                           f"|:white_small_square:** {'No Champion' if not self.second_champ else self.second_name}**\n"
                                           f"|:white_small_square:** {'No Champion' if not self.third_champ else self.third_name}**\n"
                                     ,
                                     inline=True)

                self.embed['fields'].append(mastery_field)

    def __champion_level_embed(self):

        champion_level = dict(name="\u200b", value=f":beginner: Level {self.first_level}\n"
                                                   f":beginner: Level {'0' if not self.second_champ else self.second_level}\n"
                                                   f":beginner: Level {'0' if not self.third_champ else self.third_level}",
                              inline=True)

        self.embed['fields'].append(champion_level)

    def __champion_points_embed(self):

        f_point = f"{self.first_point:02,}" if self.first_point >= 1000 else self.first_point
        s_point = "0" if not self.second_champ else f"{self.second_point:02,}" if self.second_point >= 1000 else self.second_point
        t_point = "0" if not self.third_champ else f"{self.third_point:02,}" if self.third_point >= 1000 else self.third_point

        champion_points = dict(name="\u200b", value=f":white_small_square:Points {f_point}\n"
                                                    f":white_small_square:Points {s_point}\n"
                                                    f":white_small_square:Points {t_point} ",
                               inline=True)

        self.embed['fields'].append(champion_points)

    def __rank_embed(self):

        if self.summoners_rank == "Unranked Summoner rift":

            rank = dict(name="**Ranked Summary**", value="**Unranked**", inline=True)

            self.embed['fields'].append(rank)

        else:
            rank, promotion, win_rate = self.summoners_rank
            rank_mode, rank_title, rank_level, win, loss = rank
            win_percent, total_rank = win_rate
            rank_title = " ".join((rank_title.title(), rank_level))
            total_games = win + loss

            if type(promotion) == dict:
                p_win, p_loss, target, p_games = promotion['wins'], promotion['losses'], promotion['target'], len(
                    promotion['progress'])
                league_point = f"|:white_small_square:**Promotion Series**\n" \
                               f"|:small_blue_diamond: **Win: **{p_win}\n|:small_blue_diamond: **Loss:** {p_loss}\n|:small_blue_diamond: **Target:** {target}\n|:small_blue_diamond: **Games:** {p_games}"
            else:
                if len(promotion) <= 2:
                    league_point = f"|:white_small_square:**League Point:** {promotion}"
                elif int(promotion) > 100:
                    league_point = f"|:white_small_square:**League Point:** {promotion}"

            rank = dict(name="**Ranked Summary**",
                        value=f"|:white_small_square:**{rank_title}**\n"
                              f"|:white_small_square:**Win** {win} \n"
                              f"|:white_small_square:**Lost** {loss}\n"
                              f"|:white_small_square:**Win Percentage** {win_percent}%\n"
                              f"{league_point}\n"
                              f"|:white_small_square:**Total Games** {total_games}",
                        inline=True)
            self.embed['fields'].append(rank)

    def __game_summary(self):

        if self.active == "No Active Game":
            active = dict(name="**:video_game: Game Status Summary**",
                          value="No Active Game",
                          inline=True)
            self.embed['fields'].append(active)
        else:
            team, map_name, game_mode, summoner_spell, champion, game_length = self.active
            active = dict(name="**:video_game: Game Status Summary**",
                          value=f"[{game_mode.title()}](https://www.nomadfoods.com/wp-content/uploads/2018/08/placeholder-1-e1533569576673-960x960.png)\n"
                                f"**Map**: {map_name}\n"
                                f"**Team**: {team}\n"
                                f"**Champion:** {champion}\n"
                                f"**Spells:** {'/'.join(summoner_spell)}\n"
                                f"**Game Time:** {game_length if '-1' not in game_length else 'Game loading'}",
                          inline=True)
            self.embed['fields'].append(active)
