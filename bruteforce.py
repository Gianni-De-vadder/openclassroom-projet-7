import csv
import itertools
import cProfile


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
        print(f"\nMost profitable investment ({len(best_combo)} shares) :\n")
        for share in best_combo:
            print(share)
        print("\nTotal cost : ", InvestmentOptimizer.calc_cost(best_combo), "€")
        print(
            "Profit after 2 years : +", InvestmentOptimizer.calc_profit(best_combo), "€"
        )

    def optimize_investment(self):
        """Main function to optimize the investment"""
        print(f"\nProcessing {len(self.shares_list)} shares for {self.max_invest}€ :")
        best_combo = self.set_combos()
        InvestmentOptimizer.display_results(best_combo)


if __name__ == "__main__":
    optimizer = InvestmentOptimizer(500, "actions.csv")
    cProfile.run("optimizer.optimize_investment()", sort="tottime")
