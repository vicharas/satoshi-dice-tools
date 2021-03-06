from satoshidicetools.simulator import satoshidice

"""
On loss, double bet amount.
"""

class Martingale(satoshidice.Simulator):
    def strategy(self, previous_bet):
        # if previous bet was a loss then double bet amount
        if previous_bet and previous_bet['profit'] < 0:
            self.bet_amount = previous_bet['bet_amount'] * 2
        else:
            self.bet_amount = self.initial_bet_amount

    def on_strategy_end(self):
        self.plot()

martingale = Martingale(balance=0.001, bet_amount=0.00001, less_then=32112)
martingale.run()
