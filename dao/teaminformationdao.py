class TeamInformationDao():
    teamID = 0
    teamName = ""
    numTotalGames = 0
    numGamesAtLeastEleven = 0
    gamesAtLeastEleven = []
    numGamesNotOnTuesdayOrSaturday = 0
    gamesNotOnTuesdayOrSaturday = []
    
    def init(self,  teamID,  teamName,  numTotalGames,  numGamesAtLeastEleven,  gamesAtLeastEleven,  numGamesNotOnTuesdayOrSaturday,  gamesNotOnTuesdayOrSaturday):
        self.teamID = teamID
        self.teamName = teamName
        self.numTotalGames = numTotalGames
        self.numGamesAtLeastEleven = numGamesAtLeastEleven
        self.gamesAtLeastEleven = gamesAtLeastEleven
        self.numGamesNotOnTuesdayOrSaturday = numGamesNotOnTuesdayOrSaturday
        self.gamesNotOnTuesdayOrSaturday = gamesNotOnTuesdayOrSaturday
