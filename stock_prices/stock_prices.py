#!/usr/bin/python

import argparse

def find_max_profit(prices):

    for i in range(len(prices)):
      cur_index = i
      min_price = cur_index
      max_price = cur_index
      max_profit = None
      
  #find the largest value in the prices list
      for h in range(max_price, len(prices)):
        if prices[max_price] < prices[h]:
          max_price = h

      for j in range(min_price, max_price):
        if prices[min_price] > prices[j]:#find the smallest index befor max_price
          min_price = j
  
  #subtract the smallest index from the largest
      max_profit = prices[max_price] - prices[min_price]
  #return max profit
      return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))