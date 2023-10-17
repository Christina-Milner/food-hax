
# Class def for the dishes
# ings = ingredients, currently unused as I don't have time to actually add them to the dishes
# Dishes info lives in a csv file

class Dish:
    def __init__(self, number, name, cuisine, wine, ings):
        self.number = number
        self.name = name
        self.cuisine = cuisine
        self.wine = wine
        self.ings = ings

class Day:
    def __init__(self, fullName, shortName):
        self.fullName = fullName
        self.shortName = shortName
        self.dish = None


dishes = list()
# ingrs = dict() 

weekFull = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']
weekShort = ['tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'mon']
days = []

def lushes(x):
    if x == 'r':
        print('You have chosen red wine.\n')
        for dish in dishes:
            if dish.wine in ['Red', 'Either']:
                print(dish.number, dish.name, dish.wine)
    if x == 'w':
        print('You have chosen white wine.\n')
        for dish in dishes:
            if dish.wine in ['White', 'Either']:
                print(dish.number, dish.name, dish.wine)


def loadDishes():
    cnt = 0
    fhand = open('food.csv')
    for line in fhand:
        cnt += 1
        line = line.rstrip()
        line = line.split(',')
        stuff = [x for x in line[3].split(';')]
        dishes.append(Dish(cnt, line[0], line[1], line[2], stuff))
    fhand.close()

def printCurrent():
    for day in days:
        try:
            print('{}: {}, {}'.format(day.fullName, day.dish.name, day.dish.wine))
        except:
            print('{}: No food info yet.'.format(day.fullName))

def getChoice():
    choice = input('1 for the full list of dishes\n2 to choose by wine type\n3 to see the current list\n')
    if choice == '1':
        for dish in dishes:
            print(dish.number, dish.name)
    if choice == '2':
        booze = input('Red or white? ')
        if booze.lower() == 'white' or booze.lower() == 'w':
            lushes('w')

        elif booze.lower() == 'red' or booze.lower() == 'r':
            lushes('r')
        else:
            print('That\'s not a valid wine.')
    if choice == '3':
        printCurrent()
        getChoice()

## Main program loop

print('Welcome to Christina\'s food hax!')
loadDishes()
print('There are {} dishes to choose from.\n'.format(len(dishes)))
start = input('What day to start from? (mon, tue, wed, thu, fri, sat, sun - default Tuesday)\n')
num_days = input('How many days?\nDefault 7.')
if num_days:
    try:
        num_days = int(num_days)
    except:
        num_days = 7
else:
    num_days = 7
if start.lower() in weekShort:
    start = weekShort.index(start.lower())
else:
    start = 0

end = start + num_days

while start < end:
    days.append(Day(weekFull[start % len(weekFull)], weekShort[start % len(weekShort)]))
    start += 1


for day in days:
    dinner = None
    booze = None
    print('What do we want to eat on {}?\n'.format(day.fullName))
    getChoice()
    while dinner is None:
        ask = input('Enter your meal choice for {} by its number.\n'.format(day.fullName))
        try:
            dinner = int(ask)
            for dish in dishes:
                if dish.number == dinner:
                    day.dish = dish
                    #for x in dish.ings:
                        #ingrs[x] = ingrs.get(x, 0) + 1
                    if not 'Other' in dish.name:
                        dishes.remove(dish)
        except:
            print('That doesn\'t seem to be a valid number.')
printCurrent()


""" q = input('\nWould you like to see the list of ingredients required?\n')
if q.lower() == 'y' or q.lower() == 'yes':
    print('Ingredients required:')
    for (ing, amount) in ingrs.items():
        print(ing, 'x', amount)
 """
""" fr = input('Kebabs on Friday as usual?\n\'Y\' for yes or anything else for no.\n')
if fr.lower() == 'y':
    kebabs = next((item for item in dishes if item.name == "Kebabs"), None)
        if dish.name == 'Kebabs':
            #for x in dish.ings:
                #ingrs[x] = ingrs.get(x, 0) + 1
            days['Friday'] = dish  # Rethink the days array, need to be able to access them directly by name
            week.remove('Friday')
            dishes.remove(dish) """

""" if 'Saturday' not in days:
    sat = input('Poutine on Saturday as usual?\n\'Y\' for yes or anything else for no.\n')
    if sat.lower() == 'y':
        for dish in dishes:
            if dish.name == 'Poutine':
                #for x in dish.ings:
                    #ingrs[x] = ingrs.get(x, 0) + 1
                days['Saturday'] = dish
                week.remove('Saturday')
                dishes.remove(dish) """
