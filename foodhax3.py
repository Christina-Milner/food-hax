class Dish:
    def __init__(self, number, name, cuisine, wine, ings):
        self.number = number
        self.name = name
        self.cuisine = cuisine
        self.wine = wine
        self.ings = ings

days = dict()
dishes = list()
ingrs = dict()

week = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']
week2 = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']

print('Welcome to Christina\'s food hax!')
cnt = 0
fhand = open('food.csv')
for line in fhand:
    cnt += 1
    line = line.rstrip()
    line = line.split(',')
    stuff = [x for x in line[3].split(';')]
    dishes.append(Dish(cnt, line[0], line[1], line[2], stuff))
#for dish in dishes:
#    print(dish.name, dish.wine)

print('There are {} dishes to choose from.\n'.format(cnt))

if 'Friday' not in days:
    fr = input('Pizzas on Friday as usual?\n\'Y\' for yes or anything else for no.\n')
    if fr.lower() == 'y':
        for dish in dishes:
            if dish.name == 'Pizzas':
                for x in dish.ings:
                    ingrs[x] = ingrs.get(x, 0) + 1
                days['Friday'] = dish
                week.remove('Friday')
                dishes.remove(dish)

if 'Saturday' not in days:
    sat = input('Poutine on Saturday as usual?\n\'Y\' for yes or anything else for no.\n')
    if sat.lower() == 'y':
        for dish in dishes:
            if dish.name == 'Poutine':
                for x in dish.ings:
                    ingrs[x] = ingrs.get(x, 0) + 1
                days['Saturday'] = dish
                week.remove('Saturday')
                dishes.remove(dish)

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
                    for x in dish.ings:
                        ingrs[x] = ingrs.get(x, 0) + 1
                    week.remove(day)
                    if not 'Other' in dish.name:
                        dishes.remove(dish)
        except:
            print('That doesn\'t seem to be a valid number.')

#print(days)
for day in week2:
    food = days[day]
    print('{}: {}, {}'.format(day, food.name, food.wine))
q = input('\nWould you like to see the list of ingredients required?\n')
if q.lower() == 'y' or q.lower() == 'yes':
    print('Ingredients required:')
    for (ing, amount) in ingrs.items():
        print(ing, 'x', amount)
fhand.close()
