import sys
sys.path.append('../dao/')

from dao.teaminformationdao import TeamInformationDao
from dao.gameinformationdao import GameInformationDao

CLeagueTeamList = [ "Yaks C",
                    "Ice-o-Topes C",
                    "WT Killer Bees C",
                    "Black Ops",
                    "Ashley's Ruination",
                    "Thompson's Pizza",
                    "Depot Town Stags",
                    "Mott C Men"
]

DOneLeagueTeamList = [ "Ice Men",
                       "St. Anky Beer",
                       "Sasquatch",
                       "Ashley's Hopslam",
                       "Ice-o-Topes",
                       "Cleveland Steamers",
                       "Ice Dogs",
                       "Gates",
                       "Yaks"
]

CLeagueTeamtoTeamInformationDaoDict = { teamName:TeamInformationDao(teamName) for teamName in CLeagueTeamList }
DOneLeagueTeamtoTeamInformationDaoDict = { teamName:TeamInformationDao(teamName) for teamName in DOneLeagueTeamList }

# CLeagueTeamToGamesAtLeastEleven = { teamName:[] for teamName in CLeagueTeamList }
# CLeagueTeamToGamesNotOnTuesdaySaturday = { teamName:[] for teamName in CLeagueTeamList }
# DOneLeagueTeamToGamesAtLeastEleven = { teamName:[] for teamName in DOneLeagueTeamList }
# DOneLeagueTeamToGamesNotOnTuesdaySaturday = { teamName:[] for teamName in DOneLeagueTeamList }