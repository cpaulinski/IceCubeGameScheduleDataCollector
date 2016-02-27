import urllib.request
from icalendar import Calendar #, Event
#from dateutil.parser import parse
#import datetime
from datetime import timezone
#import icalendar

class WebcalReader():
    
    def addGameAtLeastElevenToTeam(self):
        print ("placeholder")
        
    def addGameNotOnTuesdaySaturdayToTeam(self):
        print ("placeholder")
    
#    def ts2str(ts):
##        '''Convert a UTC timestamp into a UTC datetime, then format it to a string'''
#        dt = datetime.utcfromtimestamp(ts)      # Convert a UTC timestamp to a naive datetime object
#        dt = dt.replace(tzinfo=pytz.utc)        # Convert naive datetime to non-naive
#        return dt.strftime('%Y-%m-%d %H:%M:%S.%f%z')
    
    print("Hello World from webcalreader.py webCalReader!")
    #real link is webcal://<link> but we need to change this to http so that urllib can read it
    webcalUrl = "webcal://cdn.goalline.ca/subscribe_ical_league_team.php?cal=1c7fa-201601-201604-41040-510366-1721&1"
    httpUrl = webcalUrl.replace("webcal",  "http")
    req = urllib.request.urlopen(httpUrl)
    data = req.read()

    cal = Calendar.from_ical(data)
    numEvents = 0

#ends early for some reason when running
    for event in cal.walk('VEVENT'):
        print ("inside event")
        numEvents += 1
        startDate = (event.get('DTSTART'))
        endDate = (event.get('DTEND'))
        summary = event.get('SUMMARY')
        eventUID = event.get('UID')
        
        startDateDT = startDate.dt
        
#        convert timezone to local timezone for day of the week
        startDate.dt = startDate.dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
        
        #Return the day of the week as an integer, where Monday is 0 and Sunday is 6.
        dayOfWeek = startDate.dt.weekday()
        print ("day of week: ",  dayOfWeek)
        
#        parse(date.dt)
        
        teamsStr = summary.replace(" - Regular Season GAME ",  "")
        awayTeam = teamsStr.split(" @ ")[0]
        homeTeam = teamsStr.split(" @ ")[1]

        print (startDate.dt)
        print (startDate.dt.time())
        
#        printing date.to_ical gets more results than print date.dt,  but still not all of them consistently
#        print (date.to_ical())
        
        print (summary)
        
        print (eventUID.to_ical())

#    for component in cal.walk():
#        numEvents += 1
#        if (component.name == "VEVENT"):
#            date = event.get('dstart')
#            print (date.to_ical())

    

    print ("number of events: %d" %  numEvents)
    
    
