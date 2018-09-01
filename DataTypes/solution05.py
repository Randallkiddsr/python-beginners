#!/usr/bin/env python3
COST_HOUR = 0.51
BUDGET = 918

cost_single_day = 24 * COST_HOUR
cost_single_month = 30 * cost_single_day
cost_twenty_day = cost_single_day * 20
cost_twenty_month = cost_single_month * 20
possible_days = BUDGET / cost_single_day

print("\nCost 1 server/day: {:.2f}$".format(cost_single_day))
print("Cost 1 server/month: {:.2f}$\n".format(cost_single_month))
print("\nCost 20 server/day: {:.2f}$".format(cost_twenty_day))
print("Cost 20 server/month: {:.2f}$\n".format(cost_twenty_month))
print("Possible days with a budget of {}$: {:.2f}".format(BUDGET, possible_days))