import csv
import itertools


class Share:
    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit

    def __repr__(self):
        return f"{self.name} ({self.price} €, {self.profit} %)"


class InvestmentOptimizer:
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
        """Set all possible combinations of shares
        Check if under max possible investment
        Check and get highest profit

        @return: most profitable combination (list of Share objects)
        """
        profit = 0
        best_combo = []

        for i in range(len(self.shares_list)):
            combos = itertools.combinations(self.shares_list, i + 1)

            for combo in combos:
                total_cost = self.calc_cost(combo)

                if total_cost <= self.max_invest:
                    total_profit = self.calc_profit(combo)

                    if total_profit > profit:
                        profit = total_profit
                        best_combo = combo

        return best_combo

    @staticmethod
    def calc_cost(combo):
        """Sum of current share combo prices

        @param combo: list of current shares combo
        @return: total cost (float)
        """
        return sum([share.price for share in combo])

    @staticmethod
    def calc_profit(combo):
        """Sum of current share combo profit

        @param combo: list of current shares combo
        @return: total profit (float)
        """
        return sum([share.price * share.profit / 100 for share in combo])

    @staticmethod
    def display_results(best_combo):
        """Display best combination results

        @param best_combo: most profitable shares combination (list of Share objects)
        """
        print(f"\nLes plus profitables ({len(best_combo)} Actions) :\n")
        for share in best_combo:
            print(share)
        print(f"\nCout total : {InvestmentOptimizer.calc_cost(best_combo):.2f} €")
        print(
            f"Profit après 2 ans : {InvestmentOptimizer.calc_profit(best_combo):.2f} €"
        )

    def optimize_investment(self):
        """Main function to optimize the investment"""
        print(f"\nAnalyse de {len(self.shares_list)} actions pour {self.max_invest}€ :")
        best_combo = self.set_combos()
        InvestmentOptimizer.display_results(best_combo)


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
                if float(row[1]) <= 0 or float(row[2]) <= 0:
                    continue
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
        print(f"\nAnalyse de {len(self.shares_list)} actions pour {self.max_invest}€ :")
        best_combo = self.set_combos()
        InvestmentOptimizer.display_results(best_combo)
