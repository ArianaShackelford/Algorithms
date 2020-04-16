#!/usr/bin/python

import argparse

def find_max_profit(prices):


    max_price = 0 #integer
    min_price = 0
  #find the largest value in the prices list
    for i in prices:
      #i is an integer
      if max_price < i:
        #integer     integer
        max_price = i
        #integer    integer
        new_list = [prices[: prices[i]]]
        #list       ^list     ^list ^is this the proper index? or just the value?
  #get rid of everything to the right of that index

    

  #now find the smallest index
    for i in new_list:
      if min_price > i:
        min_price = i

  #subtract the smallest index from the largest
    max_profit = max_price - min_price
  #return max profit
    return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))