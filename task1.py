import numpy as np

t = int(input())

matches = {}
player_score = {}
for i in range(t):
	match_info = list(input().split(':'))
	player_info = list(match_info[1].split(','))

	ind_info = {}
	for z in player_info:
		z = list(z.split('-'))
		ind_info[z[0]] = int(z[1])
		if z[0] in player_score:
			player_score[z[0]] += int(z[1])
		else:
			player_score[z[0]] = int(z[1])
	matches[match_info[0]] = ind_info

data = [('name', 'U10'),('score', int)]
scores = np.array(list(player_score.items()), dtype = data)
scores[::-1].sort(order = ['score', 'name'])
print(matches)
print(list(scores))