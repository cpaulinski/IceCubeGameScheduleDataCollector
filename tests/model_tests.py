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

        gamedao = GameInformationDao()

#        gamedao = GameInformationDao.initBaseGameInformationDao(self, gameID, homeTeam, awayTeam, gameDate, startTime, endTime, dayOfWeek)
        gamedaoList = [ gamedao ]

        CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").gamesAtLeastEleven.append(gamedao)
        self.assertListEqual(gamedaoList, CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").gamesAtLeastEleven)

        IceOTopesGamesAtLeastElevenList = CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").gamesAtLeastEleven
        IceOTopesGamesAtLeastElevenList.append(gamedao)
        # does assertNotEqual ensure lists are checked correctly?
        self.assertNotEqual(gamedaoList, CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").gamesAtLeastEleven)

        CLeagueTeamtoTeamInformationDaoDict.get("Ice-o-Topes C").gamesAtLeastEleven[0].dayOfWeek = 0

