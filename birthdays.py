'''
Simulating 100000 times for how many peoples can have same birthdays for N people
'''

import datetime, random

def getBirthdays(NumBday):
    #Returns list of random birthdays as date objects 
    birthdays = []
    #we need all birthdays in single year
    startofyear = datetime.date(2020, 1, 1)

    for i in range(NumBday):
        timediff = random.randint(0,365)
        birthdays.append(startofyear + datetime.timedelta(timediff))

    return birthdays

def getMatch(birthdays):
    #returns if same birthday occur more than once
    if len(birthdays) == len(set(birthdays)):
        return None
    for i, birthday1 in enumerate(birthdays):
        for j, birthday2 in enumerate(birthdays[i+1:]):
            if birthday1 == birthday2:
                return birthday1
            
def formatDay(birthdays):
    #Format day into DD MMM format 
    return [birthday.strftime('%b %d') for birthday in birthdays]
    

# MONTHS = ('Jan', 'Feb', "Mar", "Apr", "May", 'June', 'July', 'Aug', 'Sept','Oct', 'Nov','Dec')

#loop till you enter a correct number
while True:
    print('How many Birthdays Should i generate: (Max 100)')
    response = input('>> ')
    if response.isdecimal() and (0< int(response) <= 100):
        numBday = int(response)
        break

print('Here are {} bithdays:'.format(numBday))
birthdays = getBirthdays(numBday)

# print(birthdays)
# #display birthdays right
# for i, birthday in enumerate(birthdays):
#     if i != 0:
#         print(',', end = ' ')
#     month = MONTHS[birthday.month - 1]
#     dateText = '{} {}'.format(month, birthday.day)
#     print(dateText, end=' ')

#display birthdays
formated_day = formatDay(birthdays)
for day in formated_day:
    print(day, end='  ')
print()
print()


#matching the birthday
match = getMatch(birthdays)

#displaying of match
print('In this simulation : ')
if match != None:
    # birthMonth = MONTHS[match.month - 1]
    # dateText2 = '{} {}'.format(birthMonth, match.day)
    matchDay = match.strftime('%b %d')
    print('Multiple people have matched birthday on day {}'.format(matchDay))
else:
    print("There are no matchig birthdays")
print()
print()


#Now Doing this 100_000 times 
print('Generating', numBday, 'bithdays, 100000 times')
input('Press Enter to continue : ')

simMatch = 0
for i in range(100000):
    if i%10000 == 0:
        print(i , 'Simulating run...')
    bday = getBirthdays(numBday)
    if getMatch(bday) != None:
        simMatch += 1
    
print('100000 simulation run done')

probablity = round(simMatch/100000 *100, 2)
print('So there are ', probablity, '% chance that', numBday, 'people, will have same bithdays')
print()

