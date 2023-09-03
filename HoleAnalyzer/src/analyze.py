import matplotlib.pyplot as plt
import csv
import os

path = '../analyzed_results'
files = os.listdir(path)

results = {}
for f in files:
    file_path = os.path.join(path, f)
    file = open(file_path, 'r')
    c = csv.DictReader(file)
    l = []
    for row in c:
        l.append(dict(row))
    d = {}
    for team in l:
        dd = {}
        for k in team.keys():
            if k == 'team_name':
                continue
            dd[k] = team[k]
        d[team['team_name']] = dd
    results[f.split('.')[0]] = d

avg_holes = []
for r in results.keys():
    avg_holes.append([r, results[r]['Total']['avg_hole'], results[r]['Total']['avg_clash']])
avg_holes.sort(key=lambda x: x[0])
fig, ax = plt.subplots()
ax.scatter([h[0] for h in avg_holes], [float(h[1]) for h in avg_holes])
ax.scatter([h[0] for h in avg_holes], [float(h[2]) for h in avg_holes])
plt.legend(['hole', 'clash'])
fig.autofmt_xdate()
plt.show()

fig, ax = plt.subplots()
data = []
for r in results.keys():
    data.append([r, []])
    for team in results[r].keys():
        if team == 'Total':
            continue
        data[-1][-1].append(float(results[r][team]['avg_clash']) + 0.001)
data.sort(key=lambda x: x[0])
print(data)
ax.boxplot([d[1] for d in data])
plt.xticks([i + 1 for i in range(len(results.keys()))], [i[0] for i in data])
i=1
for d in data:
    plt.plot([i] * len(d[1]), d[1], 'r.', alpha=0.2)
    i += 1
plt.yscale("log")
fig.autofmt_xdate()
plt.show()
# print(data)

data = []
label = []
for r in results.keys():
    label.append(r)
    data.append([r, []])
    for team in results[r].keys():
        if team == 'Total':
            continue
        data[-1][-1].append(float(results[r][team]['avg_clash']))
data.sort(key=lambda x: x[0])
print(data)
data2 = []
for c in data:
    data2.append([0] * 10)
    for d in c[1]:
        if d == 0:
            data2[-1][0] += 1
        elif d < 1:
            data2[-1][1] += 1
        elif d < 2:
            data2[-1][2] += 1
        elif d < 3:
            data2[-1][3] += 1
        elif d < 4:
            data2[-1][4] += 1
        elif d < 5:
            data2[-1][5] += 1
        elif d <= 10:
            data2[-1][6] += 1
        elif d <= 20:
            data2[-1][7] += 1
        elif d <= 30:
            data2[-1][8] += 1
        else:
            data2[-1][9] += 1
    s = sum(data2[-1])
    for d in range(len(data2[-1])):
        data2[-1][d] /= s

for d in data2:
    plt.plot(d)
plt.legend([l[0] for l in data])
plt.xticks(list(range(10)), ['0', '1', '2', '3', '4', '5', '6-10', '11-20', '21-30', '>31'])
plt.show()
print('END')