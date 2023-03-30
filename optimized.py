from bruteforce import InvestmentOptimizer, Share
import csv


class InvestmentOptimizerGreedy:
    def __init__(self, max_invest, shares_file):
        self.max_invest = max_invest
        self.shares_list = self.read_csv(shares_file)

    def read_csv(self, file_path):
        """Import shares data from a CSV file

        @param file_path: path to the CSV file
        @return: shares data (list of Share objects)
        """
        shares_list = []
        with open(file_path) as csvfile:
            shares_file = csv.reader(csvfile, delimiter=",")
            for row in shares_file:
                name, price, profit = row
                shares_list.append(Share(name, float(price), float(profit)))
        return shares_list

    def set_combos(self):
        """Get the most profitable combination of shares for the investment limit"""
        shares_sorted = sorted(self.shares_list, key=lambda share: -share.profit)
        combo = []
        total_cost = 0
        total_profit = 0
        for share in shares_sorted:
            if total_cost + share.price <= self.max_invest:
                combo.append(share)
                total_cost += share.price
                total_profit += share.price * share.profit / 100
        return combo

    def optimize_investment(self):
        """Main function to optimize the investment"""
        print(f"\nProcessing {len(self.shares_list)} shares for {self.max_invest}€ :")
        best_combo = self.set_combos()
        InvestmentOptimizer.display_results(best_combo)


invesment = InvestmentOptimizerGreedy(500, "actions.csv")
print(invesment.optimize_investment())
