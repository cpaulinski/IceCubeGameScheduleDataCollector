class TeamInformationDao():
    def initBaseTeamInformationDao(self,  teamID,  teamName,  numTotalGames,  numGamesAtLeastEleven,  gamesAtLeastEleven,  numGamesNotOnTuesdayOrSaturday,  gamesNotOnTuesdayOrSaturday):
        self.teamID = teamID
        self.teamName = teamName
        self.numTotalGames = numTotalGames
        self.numGamesAtLeastEleven = numGamesAtLeastEleven
        self.gamesAtLeastEleven = gamesAtLeastEleven
        self.numGamesNotOnTuesdayOrSaturday = numGamesNotOnTuesdayOrSaturday
        self.gamesNotOnTuesdayOrSaturday = gamesNotOnTuesdayOrSaturday

    def __init__(self, teamName):
        TeamInformationDao.initBaseTeamInformationDao(self, 0, teamName, 0, 0, [], 0, [])