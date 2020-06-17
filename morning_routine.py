import random
morning_list = ['Eat: Smoothie, yogurt, banana, granola, oatmeal', 'Put music on (mood)', 'Read 5 pages of something or a medium article', 'Stretch --> 10 squats --> pushups', 'Sustain a note on an instrument, think of a song', 'Read work goals', 'Set after work goals', 'fiber', 'Make your bed', 'Clean 1 thing up', 'Make coffee']
random.shuffle(morning_list)
routine_totals = 0
non_bonus = len(morning_list)
bonus_totals = 0
for i in morning_list:
    print(f'TASK: {i}')
    x = input()
    if x.upper() == 'X' and 'BONUS' not in i:
            routine_totals += 1
            continue
    elif x.upper() == 'S':
            print('Press y if you want to skip or x if you completed')
            z = input()
            if z.upper() == 'Y' and 'BONUS' not in i:
                    continue
            elif z.upper() == 'X':
                    routine_totals += 1
                    continue
    elif x.upper() == 'X' and 'BONUS' in i:
            bonus_totals += 1
    else:
            print('TYPE S OR X ONLY')
print(f'You completed {float(routine_totals) / float(non_bonus)} of the routine')
