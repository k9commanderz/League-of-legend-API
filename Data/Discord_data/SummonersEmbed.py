from Data.League.Summoner import Summoner, servers


class Summoner_embed(Summoner):

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
            colour=2470660,
            footer=dict(text="header"),
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
            first_champ, *other_champ = self.champions
            """
            Getting the top 3 masteries champions and return their name, level and points easier to add to embed
            instead of using index
            """
            f_name, self.f_level, self.f_point, self.f_last_played = first_champ

            if not other_champ:
                print("there are no more champions")
            else:
                self.second_champ, *third = other_champ
                s_name, self.s_level, self.s_point, s_last_played = self.second_champ
                self.third_champ = third
                if not self.third_champ:
                    print("summoner does not have third champ")
                else:
                    t_name, self.t_level, self.t_point, self.t_last_played = self.third_champ[0]

                mastery_field = dict(name="**Champion Masteries**",
                                     value=f"|:white_small_square: **{f_name}**\n"
                                           f"|:white_small_square:** {'No Champion' if not self.second_champ else s_name}**\n"
                                           f"|:white_small_square:** {'No Champion' if not self.third_champ else t_name}**\n"
                                     ,
                                     inline=True)

                self.embed['fields'].append(mastery_field)

    def __champion_level_embed(self):

        champion_level = dict(name="\u200b", value=f":beginner: Level {self.f_level}\n"
                                                   f":beginner: Level {'0' if not self.second_champ else self.s_level}\n"
                                                   f":beginner: Level {'0' if not self.third_champ else self.t_level}",
                              inline=True)

        self.embed['fields'].append(champion_level)

    def __champion_points_embed(self):

        f_point = f"{self.f_point:02,}" if self.f_point >= 1000 else self.f_point
        s_point = "0" if not self.second_champ else f"{self.s_point:02,}" if self.s_point >= 1000 else self.s_point
        t_point = "0" if not self.third_champ else f"{self.t_point:02,}" if self.t_point >= 1000 else self.t_point

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

            if len(promotion) <= 2:
                league_point = f"|:white_small_square:**League Point:** {promotion}"
            elif int(promotion) > 100:
                league_point = f"|:white_small_square:**League Point:** {promotion}"
            else:
                league_point = f"|:white_small_square:**Promotion Series**\n{promotion['progress']} "

            rank = dict(name="**Ranked Summary**",
                        value=f"|:white_small_square:**{rank_title}**\n"
                              f"|:white_small_square:**Win** {win} \n"
                              f"|:white_small_square:**Lost** {loss}\n"
                              f"|:white_small_square:**Win Percentage** {win_percent}\n"
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
                                f"**Game Time:** {game_length if '-1' not in game_length  else 'Game loading'}",
                          inline=True)
            self.embed['fields'].append(active)
