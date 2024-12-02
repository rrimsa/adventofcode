f_list = []
s_list = []
with open('input.txt') as input:
    for line in input.read().splitlines():
        f_list.append(int(line.split(' ')[0]))
        s_list.append(int(line.split(' ')[-1]))
f_list.sort()
s_list.sort()
zipped = zip(f_list, s_list)

absolutes = [abs(z[0] - z[1]) for z in zipped]
print(sum(absolutes))
print('\n')

f_list_apperances = []
for f in f_list:
    f_list_apperances.append({
        'num': f,
        'fapps': len([i for i in f_list if i == f]),
        'sapps': len([i for i in s_list if i == f]),
    })
for app in f_list_apperances:
    app['score'] = app['num'] * app['sapps']
print(f_list_apperances)
scores = [app['score'] for app in f_list_apperances]
print(sum(scores))

