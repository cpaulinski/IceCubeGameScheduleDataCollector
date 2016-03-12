import datetime
import sys
sys.path.append('../model/')
sys.path.append('../dao/')

# from nose.tools import *
import unittest
from model.teaminformationdictionaries import CLeagueTeamtoTeamInformationDaoDict, DOneLeagueTeamtoTeamInformationDaoDict
from dao.gameinformationdao import GameInformationDao

class ModelTests(unittest.TestCase):
    def setUp(self):
        # initialize model components to 0 or empty
        CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").numGamesAtLeastEleven = 0
        CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").gamesAtLeastEleven = []

    def tearDown(self):
        print("Entering ModuleTests tearDown")

    def testInitialization(self):
        self.assertEqual(0, CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").numGamesAtLeastEleven)
        self.assertEqual("Ice-o-Topes C", CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").teamName)
        self.assertIsNone(CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes D2"))

    def testIncreasingNumGames(self):
        CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").numGamesAtLeastEleven = CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").numGamesAtLeastEleven + 1
        self.assertEqual(1, CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").numGamesAtLeastEleven)

        IceOTopesTeamDao = CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C")
        IceOTopesTeamDao.numGamesAtLeastEleven = IceOTopesTeamDao.numGamesAtLeastEleven + 1
        self.assertEqual(2, CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").numGamesAtLeastEleven)

        # This doesn't actually work
        IceOTopesNumGamesAtLeastEleven = IceOTopesTeamDao.numGamesAtLeastEleven
        IceOTopesNumGamesAtLeastEleven = IceOTopesNumGamesAtLeastEleven + 1
        self.assertNotEqual(3, CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").numGamesAtLeastEleven)
        self.assertEqual(3, IceOTopesNumGamesAtLeastEleven)

    #@unittest.expectedFailure
    def testAddingGamesAtLeastEleven(self):
        gameID = 0
        homeTeam = "Ice-o-Topes C"
        awayTeam = "Ice-o-Topes"
        gameDate = datetime.datetime(2016,1,16) # may not be a date object in the future
        startTime = datetime.time(11) #may be a time object in the future
        endTime = datetime.time(12,20)
        dayOfWeek = 2

        gameDao = GameInformationDao(homeTeam, awayTeam)
        newGameDao = GameInformationDao(homeTeam, awayTeam, gameID, gameDate, startTime, endTime, dayOfWeek)

#        gamedao = GameInformationDao.initBaseGameInformationDao(self, gameID, homeTeam, awayTeam, gameDate, startTime, endTime, dayOfWeek)
        gamedaoList = [ gameDao ]

        CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").gamesAtLeastElevenList.append(gameDao)
        self.assertListEqual(gamedaoList, CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").gamesAtLeastElevenList)

        IceOTopesGamesAtLeastElevenList = CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").gamesAtLeastElevenList
        IceOTopesGamesAtLeastElevenList.append(gameDao)
        # does assertNotEqual ensure lists are checked correctly?
        self.assertNotEqual(gamedaoList, CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").gamesAtLeastElevenList)

        self.assertEqual(len(CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").gamesAtLeastElevenList), 2)

        for gamesInGameList in CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").gamesAtLeastElevenList:
            self.assertEqual(7,gamesInGameList.dayOfWeek)

        CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").gamesAtLeastElevenList[0].dayOfWeek = 0
        firstGame = CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").gamesAtLeastElevenList[0]
        self.assertNotEqual(7, firstGame.dayOfWeek)
