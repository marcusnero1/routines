import random
lst = ['wash face','Journal (10 mins)','30 BF progress', '1 Medium', 'Stretch', 'WO', '10 minutes of coding', '10 minutes of melody making', 'Vitamins', 'Look at work calendar', 'Plan next day goals', 'Clean up one thing in room', 'Full teeth - B, T, W, F', '50 shuf', 'Read', 'BONUS: Turn phone pics into action', 'BONUS: Read big me', 'run chord script and learn a new chord','BONUS: Read daily reminders', 'BONUS: Clean up work comp', 'BONUS: Music youtube vid','Read a poem','people.py','french.py','creative_kickstart.py']
random.shuffle(lst)
non_bonus = len(lst) - 5
routine_totals = 0
bonus_totals = 0
wo_dict = {'Workout A': ['3 X ALL', '10 Arnold Curls', '10 Pushups', '10 Rows (bb)', '10 Squats','10 pull ups'],
         'Workout B': ['3 X ALL', '10 incline Pushups', '10 Lunges','10 OHP + Tops for traps', '10 db sits','10 chinups'], 
         'Workout C': ['3 X ALL', '10 Body-weight Triceps', '10 Pushups', '10 db Rows', '10 Squats + Arnold']}
for i in lst:
    if i == 'WO':
        print(f'TASK: {i}')
        print('Weights or Abs? w for weights a for abs')
        inp = input()
        if inp.upper() == 'W':
            a = random.choice(list(wo_dict.keys()))
            print('\n'.join(wo_dict[a]))
        elif inp.upper() == 'A':
            print('Stretch')
            print('5 minutes of abs')
        else:
            print('Only select w or a')
        print('Did you finish?')
        answer = input()
        if answer == 'y':
            routine_totals += 1
            continue
        elif answer == 'n':
            print('Go to sleep. I\'m done with you')
            break
    else:
        print(f'TASK: {i}')
        x = input()
        if x.upper() == 'X' and 'BONUS' not in i:
            routine_totals += 1
            continue
        elif x.upper() == 'S':
            print('Are you sure you want to skip?')
            z = input()
            if z == 'y' and 'BONUS' not in i:
                continue
        elif x.upper() == 'X' and 'BONUS' in i:
            bonus_totals += 1
        else:
            print('TYPE S OR X ONLY')
print(f'You completed {(float(routine_totals) / float(non_bonus))*100:.2f}% of the routine, plus {bonus_totals} bonuses') 
        
