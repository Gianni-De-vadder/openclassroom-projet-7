from utils.classes import InvestmentOptimizerGreedy
import sys, cProfile

invesment = InvestmentOptimizerGreedy(500, sys.argv[1])


if len(sys.argv) >= 3 and sys.argv[2] == "true":
    cProfile.run("invesment.optimize_investment()", sort="tottime")
else:
    invesment.optimize_investment()
