import datetime

class GameInformationDao():
    gameID = ""
    homeTeam = ""
    awayTeam = ""
    gameDate = datetime.date(0)
    startTime = datetime.time(0, 0)
    endTime = datetime.time(0, 0)
    dayOfWeek = 0
    
    def init(self,  gameID,  homeTeam,  awayTeam,  gameDate,  startTime,  endTime,  dayOfWeek):
        self.gameId = gameID
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.gameDate = gameDate
        self.startTime = gameDate
        self.endTime = gameDate
        self.dayOfWeek = dayOfWeek
        
