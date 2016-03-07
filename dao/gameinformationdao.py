import datetime

class GameInformationDao():
    def initBaseGameInformationDao(self, gameID,  homeTeam,  awayTeam,  gameDate,  startTime,  endTime,  dayOfWeek):
        self.gameId = gameID
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.gameDate = gameDate
        self.startTime = gameDate
        self.endTime = gameDate
        self.dayOfWeek = dayOfWeek
        
    def __init__(self):

        self.gameID = ""
        self.homeTeam = ""
        self.awayTeam = ""
        self.gameDate = datetime.date(2016,1,16)
        self.startTime = datetime.time(0, 0)
        self.endTime = datetime.time(0, 0)
        self.dayOfWeek = 0