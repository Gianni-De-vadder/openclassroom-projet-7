from utils.classes import InvestmentOptimizer
import sys, cProfile


optimizer = InvestmentOptimizer(500, sys.argv[1])

if len(sys.argv) >= 3 and sys.argv[2] == "true":
    cProfile.run("optimizer.optimize_investment()", sort="tottime")
else:
    optimizer.optimize_investment()
