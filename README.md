# League-of-legend-API-Discord
The aim for the bot is to retrieve Match History Details, champion details and summoner details and many more to come
 
**CURRENTLY WORK IN SOME FEATURES HAVE NOT BEEN ADDED OR MAY INCLUDE BUGS**

**IN PROCESS OF MOVING CLASSES AROUND TO MATCH THE IS-A AND HAS-A**

Update on refactoring
* Spectator class has been removed from summoner class
* match history currently been removed from summoner class
* variables have been renamed to make it readable and have a meaning
* methods have been renamed same as above 
* match history should now be easier to read, and using threading for faster gathering total games
* map module has been renamed to leaguemap, Map class from leaguemap has been removed using 2 functions
* mapinfo json has been replaced where's the  mapid is the key 
* queue ID has been reformed where the queue id is the key
**the reason the refactoring is not reflecting the commit is due to codes being removed left and right rendering it not working for now**





**Features to add:**

Champions profile 
*	Champion builds
*	Champion Skins

Summoner’s Match History
*	Their current Win percentage for their last 10 Games
*	Summoner’s best lane/champions 
*	Summoner’s game status full

API Wrapper
*	Download latest Json for champions (script for downloading json is near completion)
*	Auto Upload newly champion ability gif (script for downloading video and converting to gif completed)
*	League of legend Patch notes
*	Continues checks on the rate limiter to provide back off timer after reaching rate limit



**Features already in place:**
*	Champions ability with details as well as gif preview
*	Summoner’s summary Profile 
*	Total games from last 2 years
*	Champion masteries returns their top 3
*	Summoner’s Ranked summary
*	In game summary (will provide full game in the above Summoner’s game status)


Champion Builds but would require permission from OP.GG or other site for those data etc or will proceed with creating script to gather matchistory and update an SQL databse with it

![profile](https://i.imgur.com/fnHSfOS.png)
![profile](https://i.imgur.com/Wh55An0.png)

![](https://i.imgur.com/S5MOVpg.gif)

**Champion Build is in progress**
![](https://i.imgur.com/MaRRM20.gif)

