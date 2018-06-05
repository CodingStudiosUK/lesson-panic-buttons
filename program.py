#!/usr/bin/env python
import csv, time

class Period:
    def __init__(self, t):
        self.time = t

class PeriodConstant(Period):
    continue

class PeriodVariable(Period):
    continue

WEEK_1 = 0
WEEK_2 = 5

#times = [905, 1020]
#timeNames = {times[0]: "Morning", times[1]: ""}

def getTime(week):
    curtime = time.localtime(time.time())
    return [curtime[6]+week, int(str(curtime[3]).zfill(2)+str(curtime[4]).zfill(2))]

def loadTimetable():
    data = []
    file = list(csv.reader(open('timetable.csv', 'r')))
    for row in file[1:]:
        data.append(row)
    return data

def getLesson(time, table):
    lesson = ""
    if time[0] > 4+WEEK_2:
        lesson = "WEEKEND"
    else:
        lessons = []
        for i in range(len(table)):
            lessons.append(table[i][time[0]])
        dayTime = time[1]
        """for i in range(len(times)):
            if timesNames[times[i]] == "":
                print(lessons[i])
            else:
                print(timesNames[times[i]])"""

        if dayTime < 905:
            lesson = "Morning"
        elif dayTime < 1020:
            lesson = lessons[0]
        elif dayTime < 1035:
            lesson = "First Break"
        elif dayTime < 1150:
            lesson = lessons[1]
        elif dayTime < 1210:
            lesson = "Second Break"
        elif dayTime < 1325:
            lesson = lessons[2]
        elif dayTime < 1425:
            lesson = "Lunch"
        elif dayTime < 1540:
            lesson = lessons[3]
        else:
            lesson = "Evening"
    return lesson

print("\""+getLesson(getTime(WEEK_2),loadTimetable())+"\"")
