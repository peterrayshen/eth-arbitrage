
class OpportunityPair:

    def __init__(self):
        self.buy_volume = 0.0
        self.sell_volume = 0.0
        self.buy_price = 0.0
        self.sell_price = 0.0
        self.buy_exchange = 'none'
        self.sell_exchange = 'none'
        self.profit = 0.0

    def calculate_profit(self):
        buy_taker_fee_perc = 0.0
        sell_taker_fee_perc = 0.0
        withdraw_fee_flat = 0.0
        deposit_fee_flat = 0.0

        volume = min(self.buy_volume, self.sell_volume)

        initial_value = self.buy_price * volume
        final_value = self.sell_price * (volume - volume * buy_taker_fee_perc - withdraw_fee_flat - deposit_fee_flat) * (1 - sell_taker_fee_perc)
                
        self.profit = final_value - initial_value
        return self.profit



