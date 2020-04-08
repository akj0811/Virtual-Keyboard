matches = {}
players = {}
for i in range(int(input())):
	match_info = list(input().split(':'))
	player_info = list(match_info[1].split(','))
	matches[match_info[0]] = {}
	for x in player_info:
		y = x.split('-')
		matches[match_info[0]][y[0]] = int(y[1])
		if y[0] in players:
			players[y[0]] += int(y[1])
		else:
			players[y[0]] = int(y[1])
print(matches)
print(sorted(list(players.items()), key = lambda item: (item[1], item[0]), reverse = True))
