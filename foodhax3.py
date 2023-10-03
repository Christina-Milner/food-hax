
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

for i in range(len(weekFull)):
    days.append(Day(weekFull[i], weekShort[i]))


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


## Main program loop

print('Welcome to Christina\'s food hax!')
loadDishes()
print('There are {} dishes to choose from.\n'.format(len(dishes)))
# TODO: 1. Finish this part (any day start and end) 2. Make week arrays less stupid (just use  one and add food info to each day) 3. Outsource printing of week schedule
# to separate function so it can be called at any time while picking out the food 4. (Stretch) option to edit the existing dishes while still in the loop
start = input('What day to start from? (mon, tue, wed, thu, fri, sat, sun - default Tuesday)')
if not start or start not in weekShort:
    start = 0
end = input('What day to end at? (mon, tue, wed, thu, fri, sat, sun - default Monday)')
if not end or end not in weekShort:
    end = 6
days = days[start:].append(days[0:start]) #Figure out how to make chosen end work

fr = input('Kebabs on Friday as usual?\n\'Y\' for yes or anything else for no.\n')
if fr.lower() == 'y':
    kebabs = next((item for item in dishes if item.name == "Kebabs"), None)
        if dish.name == 'Kebabs':
            #for x in dish.ings:
                #ingrs[x] = ingrs.get(x, 0) + 1
            days['Friday'] = dish  # Rethink the days array, need to be able to access them directly by name
            week.remove('Friday')
            dishes.remove(dish)

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
# Poutine is cancelled for now

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


while week:
    booze = None
    dinner = None
    day = week[0]
    print('What do we want to eat on {}?\n'.format(day))
    choice = input('1 for the full list of dishes\n2 to choose by wine type ')
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
    while dinner is None:
        ask = input('Enter your meal choice for {} by its number.\n'.format(day))
        try:
            dinner = int(ask)
            for dish in dishes:
                if dish.number == dinner:
                    days[day] = dish
                    #for x in dish.ings:
                        #ingrs[x] = ingrs.get(x, 0) + 1
                    week.remove(day)
                    if not 'Other' in dish.name:
                        dishes.remove(dish)
        except:
            print('That doesn\'t seem to be a valid number.')

#print(days)
for day in week2:
    food = days[day]
    print('{}: {}, {}'.format(day, food.name, food.wine))
""" q = input('\nWould you like to see the list of ingredients required?\n')
if q.lower() == 'y' or q.lower() == 'yes':
    print('Ingredients required:')
    for (ing, amount) in ingrs.items():
        print(ing, 'x', amount)
 """
