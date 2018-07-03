"""Restaurant rating lister."""


# put your code here
import sys


def rate_restaurant(filename):
	restaurant_dct={}
	for line in  open(filename):
		line = line.rstrip()
		restaurant, rating = line.split(":")
		restaurant_dct[restaurant]=rating

	for key, value in sorted(restaurant_dct.items()):
		print ("{} is rated at {}".format(key, value))


current_file = sys.argv[1]
rate_restaurant(current_file)



