
from pprint import pprint

import keys
import mosyle
import dsmreftab
import dsmgoogle


def main():
	print("Creating a new user in Google, Mosyle, and Reftab.")
	print("Enter the new employee's information below.")
	fname = input("First name: ")
	lname = input("Last name: ")
	# username = input("Username (First inital and last name): ")
	# email_address = input("Email address: ")
	title = input("Title: ")
	home_city = input("Home office: ")

	username = fname[0].lower() + lname.lower()

	if home_city.lower() == "stl" or home_city.lower() == "st. louis":
		if title.lower() == "marketing milk":
			email_suffix = "@marketingmilk.com"
		else:
			email_suffix = "@drivestl.com"

	else:
		email_suffix = "@drivesmn.com"

	email_address = username + email_suffix

	userinfo = dict(
		fname = fname,
		lname = lname,
		email_address = email_address,
		username = username,
		title = title,
		home_city = home_city
	)

	# pprint(userinfo, width=75)
	# print("Full Name: ")
	# print(userinfo['fname'] + " " + userinfo['lname'])
	 
	gresp = dsmgoogle.create_user_google(userinfo)
	mosyle_resp = mosyle.create_user_mosyle(userinfo)
	reftab_resp = dsmreftab.create_user_reftab(userinfo)

	if mosyle_resp != True:
		print("Mosyle user creation error:")
		pprint(mosyle_resp, width=75)

	if reftab_resp != True:
		print("Reftab user creation error")
		pprint(reftab_resp, width=75)

	if "google_error" in gresp:
		print("Google user creation error")
		pprint(gresp['google_error'], width=75)
	else:
		answer = input("Would you like to see the user's groups? (y/n)")

		if answer == 'y':
			pprint(gresp['group_resp'], width=75)


if __name__ == '__main__':
    main()
