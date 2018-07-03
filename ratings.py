"""Restaurant rating lister."""


# put your code here
import sys

menu = """Menu:
		- (A)dd a restaurant
		- (S)how the list of restaurants
		- (Q)uit
		"""


def show_menu():
	print (menu)


def show_restaurants(dictionary):
	for key, value in sorted(dictionary.items()):
		print ("{} is rated at {}".format(key, value))




def add_restaurant(dictionary):
	asking = True
	while asking:
		ask_q = input("Do you want to add a new review? Y/N ").upper().strip()
		if ask_q == "Y":
			ask_restaurant = input("Which restaurant do you want to rate? ").title()
			if ask_restaurant in dictionary:
				print ("This restaurant already has a rating , it's {}".format(dictionary[ask_restaurant]))
				ask_rating = round(float(input("What would you like to replace the rating with? 1-5: ")))
			else:
				ask_rating = round(float(input("This restaurant has never been rated. What would you like to rate it? 1-5: ")))
			
			if ask_rating >=1 and ask_rating <= 5:
				dictionary[ask_restaurant] = ask_rating
				print ("You've successfully added {} with {} rating".format(ask_restaurant, ask_rating))
			else:
				print ("This is outside of the rating range. Please try again.")
		else:
			print ("OK, all the ratings:\n")
			asking = False

	return dictionary






def run_restaurant_rating(filename):
	restaurant_dct = {}
	for line in open(filename):
		line = line.rstrip()
		restaurant, rating = line.split(":")
		restaurant_dct[restaurant] = rating

	showing_menu =True
	while showing_menu:
		show_menu()
		choice = input("What would you like to do?: ").capitalize().strip()
		if choice == "A":
			restaurant_dct = add_restaurant(restaurant_dct)
		elif choice == "S":
			show_restaurants(restaurant_dct)
		elif choice == "Q":
			break
		else:
			print ("Don't recognize this option. PLease try again")
			continue


current_file = sys.argv[1]
run_restaurant_rating(current_file)