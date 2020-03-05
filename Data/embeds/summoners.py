from Data.League.summoner import Summoner, servers


class SummonerEmbed(Summoner):

    def __init__(self, server, user):
        super().__init__(user, servers[server.upper()])

        self.embed = None

    def getEmbed(self):
        """

        :return:
        """

        self.embed = dict(
            title=f"{self.name.title()} |\\Level {self.level}/|",
            color=2470660,
            footer=dict(text="Place Holder"),
            thumbnail=dict(url=self.profileIcon),

        )
        self.__totalGamesEmbed()
        self.__championMasteryEmbed()
        self.__rankEmbed()
        self.__spectateInfo()

        return self.embed

    def __totalGamesEmbed(self):

        updateTotalGames = self.match.updateTotalGames()

        fields = [dict(name='**Summoner Stats**',
                       value=f":crossed_swords: Total Summoners Rift Games: **{self.match.totalRiftGames}**"
                             f"\n:crossed_swords: Total Howling Abyss Games: **{self.match.totalAramGames}**"
                             f"\n:crossed_swords: Total Co-op Games:  **{self.match.totalCoopGames}**\n",
                       inline=False

                       )

                  ]

        self.embed['fields'] = fields

    def __championMasteryEmbed(self):

        championMastery = self.championMastery()

        if not self.championMastery():  # check if the user has any masteries champions that this is for new accounts created
            mastery_field = dict(name="**Champion Masteries**", value="Champion masteries not found", inline=True)
            self.embed['fields'].append(mastery_field)
        else:

            championLevel, championPoints = list(zip(*championMastery.values()))

            championNames = "\n".join(["|:white_small_square: " + name for name in championMastery.keys()])
            championLevel = "\n".join([f":beginner: Level {level} " for level in championLevel])
            championPoints = "\n".join([f":white_small_square:Points {point:02,}" for point in championPoints])

            championNameField = dict(name="**Champion Masteries**", value=f"**{championNames}**", inline=True)
            championLevelField = dict(name="\u200b", value=championLevel, inline=True)
            championPointsField = dict(name="\u200b", value=championPoints, inline=True)

            self.embed['fields'].append(championNameField)
            self.embed['fields'].append(championLevelField)
            self.embed['fields'].append(championPointsField)

    def __rankEmbed(self):

        summonersRank = self.rankedSolo()


        if not summonersRank:
            rank = dict(name="**Ranked Summary**", value="**Unranked**", inline=True)
            self.embed['fields'].append(rank)
        else:

            league_point = f"|:white_small_square:**League Point:** {summonersRank['promotion']}"

            # checking if the summoner is currently in their promotion series
            if type(summonersRank['promotion']) == dict:

                league_point = f"|:white_small_square:**Promotion Series**\n" \
                               f"|:small_blue_diamond: **Win: **{summonersRank['promotion']['wins']}\n" \
                               f"|:small_blue_diamond: **Loss:** {summonersRank['promotion']['losses']}\n" \
                               f"|:small_blue_diamond: **Target:** {summonersRank['promotion']['target']}\n" \
                               f"|:small_blue_diamond: **Games:** {len(summonersRank['promotion']['progress'])}"

            rank = dict(name="**Ranked Summary**",
                        value=f"|:white_small_square:**{summonersRank['rankTier']}**\n"
                              f"|:white_small_square:**Win** {summonersRank['won']} \n"
                              f"|:white_small_square:**Loss** {summonersRank['loss']}\n"
                              f"|:white_small_square:**Win Percentage** {summonersRank['winPercentage']}\n"
                              f"{league_point}\n"
                              f"|:white_small_square:**Total Games** {summonersRank['totalRankGames']}",
                        inline=True)

            self.embed['fields'].append(rank)

    def __spectateInfo(self):

        spectate = self.spectate.spectateGame

        if spectate == "No Active Game":
            notInAGame = dict(name="**:video_game: Game Status Summary**", value="No Active Game", inline=True)
            self.embed['fields'].append(notInAGame)
        else:
            participantInfo = self.spectate.participants[self.id]
            mapName, gameMode = self.spectate.gameMode

            active = dict(name="**:video_game: Game Status Summary**",
                          value=f"[{gameMode}](https://www.nomadfoods.com/wp-content/uploads/2018/08/placeholder-1-e1533569576673-960x960.png)\n"
                                f"**Map**: {mapName}\n"
                                f"**Team**: {participantInfo[4]}\n"
                                f"**Champion:** {participantInfo[1]}\n"
                                f"**Spells:** {participantInfo[2]}/{participantInfo[3]}\n"
                                f"**Game Time:** {self.spectate.gameLength if '-1' not in self.spectate.gameLength else 'Game loading'}",
                          inline=True)
            self.embed['fields'].append(active)
