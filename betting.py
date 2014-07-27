import random
import pygal
import gambler

gamblers = []
gamblers.append(gambler.Gambler('Flat Better'))
gamblers.append(gambler.Martingale('Martingale No Max'))
gamblers.append(gambler.Martingale2('Martingale with Max Bet'))

for x in range(0,10000):
	w = random.random() < (18.0/38.0)
	for g in gamblers: g.gamble(w)
	
balancesChart = pygal.Bar()
for g in gamblers: balancesChart.add(g.name,g.BalanceHistory)
balancesChart.render_to_file('balances.svg')

betAmountsChart = pygal.Bar()
for g in gamblers: betAmountsChart.add(g.name,g.BetHistory)
betAmountsChart.render_to_file('betAmounts.svg')
