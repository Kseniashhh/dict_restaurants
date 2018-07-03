"""Restaurant rating lister."""


# put your code here
import sys


def rate_restaurant(filename):
	restaurant_dct={}
	for line in  open(filename):
		line = line.rstrip()
		restaurant, rating = line.split(":")
		restaurant_dct[restaurant]=rating

	asking = True
	while asking:
		ask_q = input("Do you want to add a new review? Y/N ").upper()
		if ask_q == "Y":
			ask_restaurant = input("Which restaurant do you want to rate? ").title()
			if ask_restaurant in restaurant_dct:
				print ("This restaurant already has a rating , it's {}".format(restaurant_dct[ask_restaurant]))
				ask_rating = int(input("What would you like to replace the rating with? 1-5: "))
			else:
				ask_rating = int(input("this restaurant has never been rated. What would you like to rate it? 1-5: "))
			restaurant_dct[ask_restaurant]=ask_rating
		else:
			print ("OK, all the ratings:\n")
			asking = False

	for key, value in sorted(restaurant_dct.items()):
		print ("{} is rated at {}".format(key, value))


current_file = sys.argv[1]
rate_restaurant(current_file)



