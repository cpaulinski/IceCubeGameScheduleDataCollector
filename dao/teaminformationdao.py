class TeamInformationDao():
    def __init__(self,  teamName,  teamID=0,  numTotalGames=0,  numGamesAtLeastEleven=0,  gamesAtLeastElevenList=[],
                 numGamesNotOnTuesdayOrSaturday=0, gamesNotOnTuesdayOrSaturdayList=[]):
        self.teamID = teamID
        self.teamName = teamName
        self.numTotalGames = numTotalGames
        self.numGamesAtLeastEleven = numGamesAtLeastEleven
        self.gamesAtLeastElevenList = gamesAtLeastElevenList
        self.numGamesNotOnTuesdayOrSaturday = numGamesNotOnTuesdayOrSaturday
        self.gamesNotOnTuesdayOrSaturdayList = gamesNotOnTuesdayOrSaturdayList