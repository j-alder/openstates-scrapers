import re
from utils import url_xpath
from openstates.scrape import State
from .bills import CABillScraper

from .events import CAEventScraper

settings = dict(SCRAPELIB_RPM=30)


class California(State):
    scrapers = {
        "bills": CABillScraper,
        "events": CAEventScraper,
    }
    legislative_sessions = [
        {
            "classification": "primary",
            "identifier": "19891990",
            "name": "1989-1990 Regular Session",
            "start_date": "1988-12-05",
            "end_date": "1990-11-30",
        },
        {
            "classification": "special",
            "identifier": "19891990 Special Session 1",
            "name": "1989-1990, 1st Special Session",
            "start_date": "1989-11-02",
            "end_date": "1990-09-01",
        },
        {
            "classification": "primary",
            "identifier": "19911992",
            "name": "1991-1992 Regular Session",
            "start_date": "1990-12-03",
            "end_date": "1992-11-30",
        },
        {
            "classification": "special",
            "identifier": "19911992 Special Session 1",
            "name": "1991-1992, 1st Special Session",
            "start_date": "1990-12-03",
            "end_date": "1992-11-30",
        },
        {
            "classification": "special",
            "identifier": "19911992 Special Session 2",
            "name": "1991-1992, 2nd Special Session",
            "start_date": "1992-10-08",
            "end_date": "1992-11-30",
        },
        {
            "classification": "primary",
            "identifier": "19931994",
            "name": "1993-1994 Regular Session",
            "start_date": "1992-12-07",
            "end_date": "1994-11-30",
        },
        {
            "classification": "special",
            "identifier": "19931994 Special Session 1",
            "name": "1993-1994, 1st Special Session",
            "start_date": "1993-01-04",
            "end_date": "1994-08-31",
        },
        {
            "classification": "primary",
            "identifier": "19951996",
            "name": "1995-1996 Regular Session",
            "start_date": "1994-12-05",
            "end_date": "1996-11-30",
        },
        {
            "classification": "special",
            "identifier": "19951996 Special Session 1",
            "name": "1995-1996, 1st Special Session",
            "start_date": "1995-01-19",
            "end_date": "1996-09-01",
        },
        {
            "classification": "special",
            "identifier": "19951996 Special Session 2",
            "name": "1995-1996, 2nd Special Session",
            "start_date": "1995-02-17",
            "end_date": "1996-09-01",
        },
        {
            "classification": "special",
            "identifier": "19951996 Special Session 3",
            "name": "1995-1996, 3rd Special Session",
            "start_date": "1996-01-04",
            "end_date": "1996-03-15",
        },
        {
            "classification": "special",
            "identifier": "19951996 Special Session 4",
            "name": "1995-1996, 4th Special Session",
            "start_date": "1996-02-13",
            "end_date": "1996-03-28",
        },
        {
            "classification": "primary",
            "identifier": "19971998",
            "name": "1997-1998 Regular Session",
            "start_date": "1996-12-02",
            "end_date": "1998-11-30",
        },
        {
            "classification": "special",
            "identifier": "19971998 Special Session 1",
            "name": "1997-1998, 1st Special Session",
            "start_date": "1997-01-14",
            "end_date": "1998-11-30",
        },
        {
            "classification": "primary",
            "identifier": "19992000",
            "name": "1999-2000 Regular Session",
            "start_date": "1998-12-07",
            "end_date": "2000-11-30",
        },
        {
            "classification": "special",
            "identifier": "19992000 Special Session 1",
            "name": "1999-2000, 1st Special Session",
            "start_date": "1999-01-19",
            "end_date": "1999-04-12",
        },
        {
            "classification": "primary",
            "identifier": "20012002",
            "name": "2001-2002 Regular Session",
            "start_date": "2000-12-04",
            "end_date": "2002-11-30",
        },
        {
            "classification": "special",
            "identifier": "20012002 Special Session 1",
            "name": "2001-2002, 1st Special Session",
            "start_date": "2001-01-03",
            "end_date": "2001-05-25",
        },
        {
            "classification": "special",
            "identifier": "20012002 Special Session 2",
            "name": "2001-2002, 2nd Special Session",
            "start_date": "2001-05-14",
            "end_date": "2002-05-10",
        },
        {
            "classification": "special",
            "identifier": "20012002 Special Session 3",
            "name": "2001-2002, 3rd Special Session",
            "start_date": "2002-01-10",
            "end_date": "2002-05-06",
        },
        {
            "classification": "primary",
            "identifier": "20032004",
            "name": "2003-2004 Regular Session",
            "start_date": "2002-12-02",
            "end_date": "2004-11-30",
        },
        {
            "classification": "special",
            "identifier": "20032004 Special Session 1",
            "name": "2003-2004, 1st Special Session",
            "start_date": "2002-12-09",
            "end_date": "2003-08-02",
        },
        {
            "classification": "special",
            "identifier": "20032004 Special Session 2",
            "name": "2003-2004, 2nd Special Session",
            "start_date": "2003-01-23",
            "end_date": "2003-02-20",
        },
        {
            "classification": "special",
            "identifier": "20032004 Special Session 3",
            "name": "2003-2004, 3rd Special Session",
            "start_date": "2003-11-18",
            "end_date": "2004-01-16",
        },
        {
            "classification": "special",
            "identifier": "20032004 Special Session 4",
            "name": "2003-2004, 4th Special Session",
            "start_date": "2003-11-18",
            "end_date": "2004-11-30",
        },
        {
            "classification": "special",
            "identifier": "20032004 Special Session 5",
            "name": "2003-2004, 5th Special Session",
            "start_date": "2003-11-18",
            "end_date": "2004-11-30",
        },
        {
            "classification": "primary",
            "identifier": "20052006",
            "name": "2005-2006 Regular Session",
            "start_date": "2004-12-06",
            "end_date": "2006-11-30",
            "active": True,
        },
        {
            "classification": "special",
            "identifier": "20052006 Special Session 1",
            "name": "2005-2006, 1st Special Session",
            "start_date": "2005-01-06",
            "end_date": "2005-10-11",
        },
        {
            "classification": "special",
            "identifier": "20052006 Special Session 2",
            "name": "2005-2006, 2nd Special Session",
            "start_date": "2006-06-27",
            "end_date": "2006-11-30",
        },
        {
            "classification": "primary",
            "identifier": "20072008",
            "name": "2007-2008 Regular Session",
            "start_date": "2006-12-04",
            "end_date": "2008-11-30",
        },
        {
            "classification": "special",
            "identifier": "20072008 Special Session 1",
            "name": "2007-2008, 1st Special Session",
            "start_date": "2007-09-11",
            "end_date": "2008-11-30",
        },
        {
            "classification": "special",
            "identifier": "20072008 Special Session 2",
            "name": "2007-2008, 2nd Special Session",
            "start_date": "2007-09-11",
            "end_date": "2008-11-30",
        },
        {
            "classification": "special",
            "identifier": "20072008 Special Session 3",
            "name": "2007-2008, 3rd Special Session",
            "start_date": "2008-01-14",
            "end_date": "2008-11-30",
        },
        {
            "classification": "special",
            "identifier": "20072008 Special Session 4",
            "name": "2007-2008, 4th Special Session",
            "start_date": "2008-11-06",
            "end_date": "2008-11-30",
        },
        {
            "classification": "primary",
            "identifier": "20092010",
            "name": "2009-2010 Regular Session",
            "start_date": "2008-12-01",
            "end_date": "2010-11-30",
        },
        {
            "classification": "special",
            "identifier": "20092010 Special Session 1",
            "name": "2009-2010, 1st Special Session",
            "start_date": "2008-12-02",
            "end_date": "2009-01-06",
        },
        {
            "classification": "special",
            "identifier": "20092010 Special Session 2",
            "name": "2009-2010, 2nd Special Session",
            "start_date": "2008-12-02",
            "end_date": "2009-02-24",
        },
        {
            "classification": "special",
            "identifier": "20092010 Special Session 3",
            "name": "2009-2010, 3rd Special Session",
            "start_date": "2009-01-05",
            "end_date": "2009-11-05",
        },
        {
            "classification": "special",
            "identifier": "20092010 Special Session 4",
            "name": "2009-2010, 4th Special Session",
            "start_date": "2009-07-02",
            "end_date": "2009-07-29",
        },
        {
            "classification": "special",
            "identifier": "20092010 Special Session 5",
            "name": "2009-2010, 5th Special Session",
            "start_date": "2009-08-27",
            "end_date": "2010-01-13",
        },
        {
            "classification": "special",
            "identifier": "20092010 Special Session 6",
            "name": "2009-2010, 6th Special Session",
            "start_date": "2009-10-14",
            "end_date": "2010-11-30",
        },
        {
            "classification": "special",
            "identifier": "20092010 Special Session 7",
            "name": "2009-2010, 7th Special Session",
            "start_date": "2009-10-14",
            "end_date": "2009-11-12",
        },
        {
            "classification": "special",
            "identifier": "20092010 Special Session 8",
            "name": "2009-2010, 8th Special Session",
            "start_date": "2010-01-11",
            "end_date": "2010-03-25",
        },
        {
            "classification": "primary",
            "identifier": "20112012",
            "name": "2011-2012 Regular Session",
            "start_date": "2010-12-06",
            "end_date": "2012-11-30",
        },
        {
            "classification": "special",
            "identifier": "20112012 Special Session 1",
            "name": "2011-2012, 1st Special Session",
            "start_date": "2010-12-06",
            "end_date": "2011-10-03",
        },
        {
            "classification": "primary",
            "identifier": "20132014",
            "name": "2013-2014 Regular Session",
            "start_date": "2012-12-03",
            "end_date": "2014-11-30",
        },
        {
            "classification": "special",
            "identifier": "20132014 Special Session 1",
            "name": "2013-2014, 1st Special Session",
            "start_date": "2013-01-28",
            "end_date": "2013-08-05",
        },
        {
            "classification": "special",
            "identifier": "20132014 Special Session 2",
            "name": "2013-2014, 2nd Special Session",
            "start_date": "2014-04-24",
            "end_date": "2014-11-30",
        },
        {
            "_scraped_name": "2015-2016",
            "classification": "primary",
            "identifier": "20152016",
            "name": "2015-2016 Regular Session",
            "start_date": "2015-01-01",
            "end_date": "2016-11-30",
        },
        {
            "classification": "special",
            "identifier": "20152016 Special Session 1",
            "name": "2015-2016, 1st Special Session",
            "start_date": "2015-06-19",
            "end_date": "2016-08-31",
        },
        {
            "classification": "special",
            "identifier": "20152016 Special Session 2",
            "name": "2015-2016, 2nd Special Session",
            "start_date": "2015-06-19",
            "end_date": "2016-05-04",
        },
        {
            "_scraped_name": "2017-2018",
            "classification": "primary",
            "identifier": "20172018",
            "name": "2017-2018 Regular Session",
            "start_date": "2016-12-05",
            "end_date": "2018-11-30",
        },
        {
            "_scraped_name": "2019-2020",
            "classification": "primary",
            "identifier": "20192020",
            "name": "2019-2020 Regular Session",
            "start_date": "2018-12-03",
            "end_date": "2020-12-31",
        },
        {
            "_scraped_name": "2021-2022",
            "classification": "primary",
            "identifier": "20212022",
            "name": "2021-2022 Regular Session",
            "start_date": "2020-12-07",
            "end_date": "2021-12-31",
            "active": True,
        },
    ]
    ignored_scraped_sessions = [
        "2013-2014",
        "2011-2012",
        "2009-2010",
        "2007-2008",
        "2005-2006",
        "2003-2004",
        "2001-2002",
        "1999-2000",
        "1997-1998",
        "1995-1996",
        "1993-1994",
    ]

    def get_session_list(self):
        sessions = url_xpath(
            "http://www.leginfo.ca.gov/bilinfo.html",
            "//select[@name='sess']/option/text()",
        )
        return [re.findall(r"\(.*\)", session)[0][1:-1] for session in sessions]
