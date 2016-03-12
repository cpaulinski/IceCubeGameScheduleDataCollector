import datetime

class GameInformationDao():
    def __init__(self,  homeTeam,  awayTeam,  gameID=0, gameDate=datetime.date(2016,1,16),
                                   startTime=datetime.time(0, 0),  endTime=datetime.time(0, 0),  dayOfWeek=7):
        self.gameId = gameID
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        self.gameDate = gameDate
        self.startTime = startTime
        self.endTime = endTime
        self.dayOfWeek = dayOfWeek