import datetime as dt


def get_time_interval(case_study):
    starttime, endtime, cr = None, None, None
    # set up - latitude minimum difference.
    if case_study == "cr1625":
        starttime = dt.datetime(year=1975, month=2, day=19)
        endtime = dt.datetime(year=1975, month=3, day=18)
        cr = "1625"

    elif case_study == "cr1629":
        starttime = dt.datetime(year=1975, month=6, day=8)
        endtime = dt.datetime(year=1975, month=7, day=5)
        cr = "1629"

    elif case_study == "cr1633":
        starttime = dt.datetime(year=1975, month=9, day=25)
        endtime = dt.datetime(year=1975, month=10, day=22)
        cr = "1633"

    elif case_study == "cr1634":
        starttime = dt.datetime(year=1975, month=10, day=22)
        endtime = dt.datetime(year=1975, month=11, day=18)
        cr = "1634"

    elif case_study == "cr1639":
        starttime = dt.datetime(year=1976, month=3, day=6)
        endtime = dt.datetime(year=1976, month=4, day=3)
        cr = "1639"

    elif case_study == "cr1642":
        starttime = dt.datetime(year=1976, month=5, day=27)
        endtime = dt.datetime(year=1976, month=6, day=23)
        cr = "1642"

    elif case_study == "cr1647":
        starttime = dt.datetime(year=1976, month=10, day=10)
        endtime = dt.datetime(year=1976, month=11, day=7)
        cr = "1647"

    elif case_study == "cr1653":
        starttime = dt.datetime(year=1977, month=3, day=23)
        endtime = dt.datetime(year=1977, month=4, day=20)
        cr = "1653"

    elif case_study == "cr1654":
        starttime = dt.datetime(year=1977, month=4, day=20)
        endtime = dt.datetime(year=1977, month=5, day=17)
        cr = "1654"

    elif case_study == "cr1655":
        starttime = dt.datetime(year=1977, month=5, day=17)
        endtime = dt.datetime(year=1977, month=6, day=13)
        cr = "1655"

    elif case_study == "cr1656":
        starttime = dt.datetime(year=1977, month=6, day=13)
        endtime = dt.datetime(year=1977, month=7, day=10)
        cr = "1656"

    elif case_study == "cr1660":
        starttime = dt.datetime(year=1977, month=9, day=30)
        endtime = dt.datetime(year=1977, month=10, day=27)
        cr = "1660"

    elif case_study == "cr1661":
        starttime = dt.datetime(year=1977, month=10, day=27)
        endtime = dt.datetime(year=1977, month=11, day=24)
        cr = "1661"

    elif case_study == "cr1662":
        starttime = dt.datetime(year=1977, month=11, day=24)
        endtime = dt.datetime(year=1977, month=12, day=21)
        cr = "1662"

    elif case_study == "cr1666":
        starttime = dt.datetime(year=1978, month=3, day=13)
        endtime = dt.datetime(year=1978, month=4, day=9)
        cr = "1666"

    elif case_study == "cr1667":
        starttime = dt.datetime(year=1978, month=4, day=9)
        endtime = dt.datetime(year=1978, month=5, day=6)
        cr = "1667"

    elif case_study == "cr1669":
        starttime = dt.datetime(year=1978, month=6, day=3)
        endtime = dt.datetime(year=1978, month=6, day=30)
        cr = "1669"

    elif case_study == "cr1674":
        starttime = dt.datetime(year=1978, month=10, day=11)
        endtime = dt.datetime(year=1978, month=11, day=13)
        cr = "1674"

    elif case_study == "cr1675":
        starttime = dt.datetime(year=1978, month=11, day=13)
        endtime = dt.datetime(year=1978, month=12, day=10)
        cr = "1675"

    elif case_study == "cr1680":
        starttime = dt.datetime(year=1979, month=3, day=30)
        endtime = dt.datetime(year=1979, month=4, day=26)
        cr = "1680"

    elif case_study == "cr1684":
        starttime = dt.datetime(year=1979, month=7, day=17)
        endtime = dt.datetime(year=1979, month=8, day=13)
        cr = "1684"

    elif case_study == "cr1681":
        starttime = dt.datetime(year=1979, month=4, day=26)
        endtime = dt.datetime(year=1979, month=5, day=23)
        cr = "1681"

    elif case_study == "cr1688":
        starttime = dt.datetime(year=1979, month=11, day=3)
        endtime = dt.datetime(year=1979, month=11, day=30)
        cr = "1688"

    elif case_study == "cr1694":
        starttime = dt.datetime(year=1980, month=4, day=15)
        endtime = dt.datetime(year=1980, month=5, day=12)
        cr = "1694"

    elif case_study == "cr1695":
        starttime = dt.datetime(year=1980, month=5, day=12)
        endtime = dt.datetime(year=1980, month=6, day=8)
        cr = "1695"

    elif case_study == "cr1697":
        starttime = dt.datetime(year=1980, month=7, day=5)
        endtime = dt.datetime(year=1980, month=8, day=1)
        cr = "1697"

    elif case_study == "cr1702":
        starttime = dt.datetime(year=1980, month=11, day=19)
        endtime = dt.datetime(year=1980, month=12, day=16)
        cr = "1702"

    elif case_study == "cr1707":
        starttime = dt.datetime(year=1981, month=4, day=4)
        endtime = dt.datetime(year=1981, month=5, day=1)
        cr = "1707"

    elif case_study == "cr1709":
        starttime = dt.datetime(year=1981, month=5, day=29)
        endtime = dt.datetime(year=1981, month=6, day=25)
        cr = "1709"

    elif case_study == "cr1710":
        starttime = dt.datetime(year=1981, month=6, day=25)
        endtime = dt.datetime(year=1981, month=7, day=22)
        cr = "1710"

    elif case_study == "cr1716":
        starttime = dt.datetime(year=1981, month=12, day=5)
        endtime = dt.datetime(year=1982, month=1, day=2)
        cr = "1716"

    elif case_study == "cr1721":
        starttime = dt.datetime(year=1982, month=4, day=21)
        endtime = dt.datetime(year=1982, month=5, day=18)
        cr = "1721"

    elif case_study == "cr1723":
        starttime = dt.datetime(year=1982, month=6, day=14)
        endtime = dt.datetime(year=1982, month=7, day=12)
        cr = "1723"

    elif case_study == "cr1724":
        starttime = dt.datetime(year=1982, month=7, day=12)
        endtime = dt.datetime(year=1982, month=8, day=8)
        cr = "1724"

    elif case_study == "cr1730":
        starttime = dt.datetime(year=1982, month=12, day=22)
        endtime = dt.datetime(year=1983, month=1, day=19)
        cr = "1730"

    elif case_study == "cr1735":
        starttime = dt.datetime(year=1983, month=5, day=8)
        endtime = dt.datetime(year=1983, month=6, day=4)
        cr = "1735"

    elif case_study == "cr1736":
        starttime = dt.datetime(year=1983, month=6, day=4)
        endtime = dt.datetime(year=1983, month=7, day=1)
        cr = "1736"

    elif case_study == "cr1737":
        starttime = dt.datetime(year=1983, month=7, day=1)
        endtime = dt.datetime(year=1983, month=7, day=29)
        cr = "1737"

    elif case_study == "cr1738":
        starttime = dt.datetime(year=1983, month=7, day=29)
        endtime = dt.datetime(year=1983, month=8, day=25)
        cr = "1738"

    elif case_study == "cr1835":
        starttime = dt.datetime(year=1990, month=10, day=25)
        endtime = dt.datetime(year=1990, month=11, day=21)
        cr = "1835"

    elif case_study == "cr1836":
        starttime = dt.datetime(year=1990, month=11, day=21)
        endtime = dt.datetime(year=1990, month=12, day=19)
        cr = "1836"

    elif case_study == "cr1841":
        starttime = dt.datetime(year=1991, month=4, day=7)
        endtime = dt.datetime(year=1991, month=5, day=4)
        cr = "1841"

    elif case_study == "cr1852":
        starttime = dt.datetime(year=1992, month=2, day=1)
        endtime = dt.datetime(year=1992, month=2, day=28)
        cr = "1852"

    elif case_study == "cr1853":
        starttime = dt.datetime(year=1992, month=2, day=28)
        endtime = dt.datetime(year=1992, month=3, day=27)
        cr = "1853"

    elif case_study == "cr1865":
        starttime = dt.datetime(year=1993, month=1, day=21)
        endtime = dt.datetime(year=1993, month=2, day=17)
        cr = "1865"

    elif case_study == "cr1915":
        starttime = dt.datetime(year=1996, month=10, day=15)
        endtime = dt.datetime(year=1996, month=11, day=11)
        cr = "1915"

    elif case_study == "cr1925":
        starttime = dt.datetime(year=1997, month=7, day=15)
        endtime = dt.datetime(year=1997, month=8, day=11)
        cr = "1925"

    elif case_study == "cr1930":
        starttime = dt.datetime(year=1997, month=11, day=28)
        endtime = dt.datetime(year=1997, month=12, day=26)
        cr = "1930"

    elif case_study == "cr1933":
        starttime = dt.datetime(year=1998, month=2, day=18)
        endtime = dt.datetime(year=1998, month=3, day=18)
        cr = "1933"

    elif case_study == "cr1934":
        starttime = dt.datetime(year=1998, month=3, day=18)
        endtime = dt.datetime(year=1998, month=4, day=14)
        cr = "1934"

    elif case_study == "cr1936":
        starttime = dt.datetime(year=1998, month=5, day=11)
        endtime = dt.datetime(year=1998, month=6, day=7)
        cr = "1936"

    elif case_study == "cr1946":
        starttime = dt.datetime(year=1999, month=2, day=8)
        endtime = dt.datetime(year=1999, month=3, day=7)
        cr = "1946"

    elif case_study == "cr1976":
        starttime = dt.datetime(year=2001, month=5, day=6)
        endtime = dt.datetime(year=2001, month=6, day=2)
        cr = "1976"

    elif case_study == "cr2008":
        starttime = dt.datetime(year=2003, month=9, day=26)
        endtime = dt.datetime(year=2003, month=10, day=23)
        cr = "2008"

    elif case_study == "cr2016":
        starttime = dt.datetime(year=2004, month=5, day=1)
        endtime = dt.datetime(year=2004, month=5, day=28)
        cr = "2016"

    elif case_study == "cr2026":
        starttime = dt.datetime(year=2005, month=1, day=29)
        endtime = dt.datetime(year=2005, month=2, day=25)
        cr = "2026"

    elif case_study == "cr2039":
        starttime = dt.datetime(year=2006, month=1, day=18)
        endtime = dt.datetime(year=2006, month=2, day=15)
        cr = "2039"

    elif case_study == "cr2059":
        starttime = dt.datetime(year=2007, month=7, day=18)
        endtime = dt.datetime(year=2007, month=8, day=14)
        cr = "2059"

    elif case_study == "cr2060":
        starttime = dt.datetime(year=2007, month=8, day=14)
        endtime = dt.datetime(year=2007, month=9, day=10)
        cr = "2060"

    elif case_study == "cr2209":
        # Carrington Rotation 2209
        # Min lat 01 (2018-10-16)
        # 2018 Sep 29	2018 Oct 26
        starttime = dt.datetime(year=2018, month=9, day=29)
        endtime = dt.datetime(year=2018, month=10, day=26)
        cr = "2209"

    elif case_study == "cr2210":
        # Carrington Rotation 2210
        # 2018 Oct 26	2018 Nov 23
        # Min lat 02 (2018-11-22)
        # Encounter 1 date: 2018-11-06. Distance from the center of the sun: 0.17 au (35.6 RS)
        starttime = dt.datetime(year=2018, month=10, day=26)
        endtime = dt.datetime(year=2018, month=11, day=23)
        cr = "2210"

    elif case_study == "cr2211":
        # Carrington Rotation 2211
        # 2018 Nov 23	2018 Dec 20
        starttime = dt.datetime(year=2018, month=11, day=23)
        endtime = dt.datetime(year=2018, month=12, day=20)
        cr = "2211"

    elif case_study == "cr2215":
        # Carrington Rotation 2215
        # Min lat 03 (2019-04-05)
        # 2019 Mar 12	2019 Apr 08
        # Encounter 2 date: 2019-04-04. Distance from the center of the sun: 0.17 au (35.6 RS)
        starttime = dt.datetime(year=2019, month=3, day=12)
        endtime = dt.datetime(year=2019, month=4, day=8)
        cr = "2215"

    elif case_study == "cr2219":
        # Carrington Rotation 2219
        # Min lat 04 (2019-07-12)
        # 2019 Jun 29	2019 Jul 26
        starttime = dt.datetime(year=2019, month=6, day=29)
        endtime = dt.datetime(year=2019, month=7, day=26)
        cr = "2219"

    elif case_study == "cr2221":
        # Carrington Rotation 2221
        # 2019 Aug 22	2019 Sep 19
        # Encounter 3 date: 2019-09-01. Distance from the center of the sun: 0.17 au (35.6 RS)
        starttime = dt.datetime(year=2019, month=8, day=22)
        endtime = dt.datetime(year=2019, month=9, day=19)
        cr = "2221"

    elif case_study == "cr2223":
        # Carrington Rotation 2223
        # 2019 Oct 16	2019 Nov 12
        # Min 05 (2019-11-05)
        starttime = dt.datetime(year=2019, month=10, day=16)
        endtime = dt.datetime(year=2019, month=11, day=12)
        cr = "2223"

    elif case_study == "cr2226":
        # todo: PSP VR DATA IS NOT AVAILABLE.
        # Carrington Rotation 2226
        # 2020 Jan 06	2020 Feb 02
        # Encounter 4 date: 2020-01-29. Distance from the center of the sun: 0.13 au (27.8 RS)
        starttime = dt.datetime(year=2020, month=1, day=6)
        endtime = dt.datetime(year=2020, month=2, day=2)
        cr = "2226"

    elif case_study == "cr2231":
        # Carrington Rotation 2231
        # 2020 May 21	2020 Jun 18
        # Encounter 5 date: 2020-06-07. Distance from the center of the sun: 0.13 au (27.8 RS)
        starttime = dt.datetime(year=2020, month=5, day=21)
        endtime = dt.datetime(year=2020, month=6, day=18)
        cr = "2231"

    elif case_study == "cr2232":
        # Carrington Rotation 2232 (Solo aligned with Earth)
        # 2020 Jun 18 to 2020 Jul 15
        starttime = dt.datetime(year=2020, month=6, day=18)
        endtime = dt.datetime(year=2020, month=7, day=15)
        cr = "2232"

    elif case_study == "cr2233":
        # Carrington Rotation 2233 (Solo available data)
        # 2020 Jul 15 to 2020 Aug 11
        starttime = dt.datetime(year=2020, month=7, day=15)
        endtime = dt.datetime(year=2020, month=8, day=11)
        cr = "2233"

    elif case_study == "cr2234":
        # Carrington Rotation 2234 (Solo available data)
        # 2020 Aug 11 to 2020 Sep 07
        starttime = dt.datetime(year=2020, month=8, day=11)
        endtime = dt.datetime(year=2020, month=9, day=7)
        cr = "2234"

    elif case_study == "cr2235":
        # todo: PSP VR DATA IS NOT AVAILABLE.
        # Carrington Rotation 2235
        # 2020 Sep 07	2020 Oct 05
        # Encounter 6 date: 2020-09-27. Distance from the center of the sun: 0.09 au (20.3 RS)
        starttime = dt.datetime(year=2020, month=9, day=7)
        endtime = dt.datetime(year=2020, month=10, day=5)
        cr = "2235"

    elif case_study == "cr2236":
        # Carrington Rotation 2236
        # 2020 Oct 05 to 2020 Nov 01
        starttime = dt.datetime(year=2020, month=10, day=5)
        endtime = dt.datetime(year=2020, month=11, day=1)
        cr = "2236"

    elif case_study == "cr2238":
        # Carrington Rotation 2238
        # 2020 Nov 28 to 2020 Dec 25
        starttime = dt.datetime(year=2020, month=11, day=28)
        endtime = dt.datetime(year=2020, month=12, day=25)
        cr = "2238"

    elif case_study == "cr2239":
        # todo: PSP VR DATA IS NOT AVAILABLE.
        # Carrington Rotation 2239
        # 2020 Dec 25	2021 Jan 22
        # Encounter 7 date: 2021-01-17. Distance from the center of the sun: 0.09 au (20.3 RS)
        starttime = dt.datetime(year=2020, month=12, day=25)
        endtime = dt.datetime(year=2021, month=1, day=22)
        cr = "2239"

    return starttime, endtime, cr