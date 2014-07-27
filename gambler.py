class Gambler(object):

	def __init__(self, name):
		self.name = name
		self.balance = 0
		self.BalanceHistory = [self.balance]
		self.bet = 10
		self.BetHistory = [self.bet]

	def gamble(self,w):
		if (w):
			self.win()
		else:
			self.lose()
		self.BalanceHistory.append(self.balance)
		self.BetHistory.append(self.bet)

	def win(self):
		self.balance += self.bet
	
	def lose(self):
		self.balance -= self.bet


class Martingale(Gambler):

	def __init__(self, name):
		super(Martingale,self).__init__(name)
		self.originalBet = self.bet
		self.targetBalance = self.bet

	def win(self):
		super(Martingale,self).win()
		self.targetBalance += self.originalBet
		self.setBet()

	def lose(self):
		super(Martingale,self).lose()
		self.setBet()

	def setBet(self):
		self.bet = self.targetBalance - self.balance

class Martingale2(Martingale):

	def setBet(self):
		self.bet = min(500,self.targetBalance - self.balance)