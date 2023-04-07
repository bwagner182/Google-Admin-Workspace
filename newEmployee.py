
from pprint import pprint
import os

import keys
import mosyle
import dsmreftab
import dsmgoogle
import sys


def collect_name(userinfo):
	print("Enter the new employee's information below.")
	userinfo['fname'] = input("First name: ")
	userinfo['lname'] = input("Last name: ")
	userinfo['username'] = userinfo['fname'][0].lower() + userinfo['lname'].lower()
	return userinfo

def collect_title(userinfo):
	userinfo['title'] = input("Title: ")
	return check_title(userinfo)

def check_title(userinfo):
	if len(userinfo['title']) > 4:
		match userinfo['title'].lower():
			case "associate account executive":
				userinfo['title_short'] = "aae"
			case "associate director of strategy":
				userinfo['title_short'] = "ados"
			case "associate director of operations":
				userinfo['title_short'] = "adoo"
			case "account executive":
				userinfo['title_short'] = "ae"
			case "business developer":
				userinfo['title_short'] = "bd"
			case "community manager":
				userinfo['title_short'] = "cm"
			case "copywriter":
				userinfo['title_short'] = "cw"
			case "creative director":
				userinfo['title_short'] = "cd"
			case "developer":
				userinfo['title_short'] = "dev"
			case "director of analytics":
				userinfo['title_short'] = "dam"
			case "director of business development":
				userinfo['title_short'] = "dbd"
			case "director of copywriting":
				userinfo['title_short'] = "dcw"
			case "director of franchise":
				userinfo['title_short'] = "dfch"
			case "director of human resources":
				userinfo['title_short'] = "dhr"
			case "director of operations":
				userinfo['title_short'] = "doo"
			case "director of recruiting":
				userinfo['title_short'] = "dor"
			case "recruiter":
				userinfo['title_short'] = "rcr"
			case "director of social strategy":
				userinfo['title_short'] = "dss"
			case "director of videography":
				userinfo['title_short'] = "dvp"
			case "graphic designer":
				userinfo['title_short'] = "gd"
			case "leadership":
				userinfo['title_short'] = "lead"
			case "office admin":
				userinfo['title_short'] = "oa"
			case "photographer":
				userinfo['title_short'] = "p/v"
			case "videographer":
				userinfo['title_short'] = "p/v"
			case "project manager":
				userinfo['title_short'] = "pm"
			case "project coordinator":
				userinfo['title_short'] = "pm"
			case "web developer":
				userinfo['title_short'] = "web"
			case "marketing milk":
				userinfo['title_short'] = "mm"
			case "analytic manager":
				userinfo['title_short'] = "am"
			case "digital analyst":
				userinfo['title_short'] = "am"
			case "controller":
				userinfo['title_chort'] = "fin"
			case "finance":
				userinfo['title_short'] = "fin"
			case _:
				print("Unable to recognize the employee's title. Consult the application developer and give them the error below.")
				print("ERROR: Incorrect title entered. Provided input: " + userinfo['title'])
				answer = input("would you like to correct the title? (y/n)")

				if answer.lower() == "y":
					collect_title(userinfo)
				elif answer.lower() == "n":
					print("Please alert the developer of this error")
					pprint(userinfo, width=75)
				else:
					os.system("clear")
					sys.exit("Invalid input, program exiting")
	else:
		userinfo['title_short'] = userinfo['title']

	return userinfo

def collect_city(userinfo):
	userinfo['home_city'] = input("Home office: ")
	return check_city(userinfo)

def check_city(userinfo):
	userinfo['city'] = userinfo['home_city']
	if len(userinfo['home_city']) > 3:
		match userinfo['home_city'].lower():
			case "st. louis":
				userinfo['city'] = "stl"
			case "atlanta":
				userinfo['city'] = "atl"
			case "tampa":
				userinfo['city'] = "tpa"
			case  "miami":
				userinfo['city'] = "mia"
			case "nashville":
				userinfo['city'] = "nsh"
			case "nash":
				userinfo['city'] = "nsh"
			case _:
				os.system("clear")
				print("Unable to recognize the employee's home city. Consult the application developer and give them the error below.")
				print("ERROR: Incorrect city entered. Provided input: " + userinfo['home_city'])
				answer = input("would you like to correct the employee's home city? (y/n)")

				if answer.lower() == "y":
					collect_city(userinfo)
				elif answer.lower() == "n":
					print("Please alert the developer of this error")
					pprint(userinfo, width=75)
				else:
					os.system("clear")
					sys.exit("Invalid input, program exiting")
	else:
		userinfo['city'] = userinfo['home_city']

	if userinfo['home_city'].lower() == "stl" or userinfo['home_city'].lower() == "st. louis":
		if userinfo['title'].lower() == "marketing milk":
			userinfo['email_suffix'] = "@marketingmilk.com"
		else:
			userinfo['email_suffix'] = "@drivestl.com"

	else:
		userinfo['email_suffix'] = "@drivesmn.com"

	userinfo['email_address'] = userinfo['username'] + userinfo['email_suffix']

	return userinfo

def collect_info(userinfo):
	userinfo = collect_name(userinfo)
	userinfo = collect_title(userinfo)
	userinfo = collect_city(userinfo)
	return userinfo

def display_user(userinfo):
	os.system("clear")
	print("This information will be used to create the new employee's accounts,")
	print("make sure the information is correct before continuing.")
	print("First name: " + userinfo['fname'])
	print("Last name: " + userinfo['lname'])
	print("Email address: " + userinfo['email_address'])
	print("Home Office: " + userinfo['home_city'])
	answer = input("Is all the above information correct? (y/n)")

	if answer.lower() == "y":
		os.system("clear")
		return True
	elif answer.lower() == "n":
		answer = input("Would you like to fix it? (y/n)")
		if answer.lower() == "y":
			main()
		elif answer.lower() == "n":
			os.system("clear")
			sys.exit("Invalid input, program exiting.")
	else:
		os.system("clear")
		sys.exit("Invalid input, program exiting")


def main():
	userinfo = dict([])
	arguments = sys.argv

	if "test" in arguments:
		userinfo['test_mode'] = True
		os.system("clear")
		print("*****Test mode enabled*****")
	else:
		userinfo['test_mode'] = False
		os.system("clear")



	userinfo = collect_info(userinfo)
	resp = display_user(userinfo)
		

	# pprint(userinfo, width=75)
	# print("Full Name: ")
	# print(userinfo['fname'] + " " + userinfo['lname'])
	 
	userinfo = dsmgoogle.create_user_google(userinfo)
	userinfo = mosyle.create_user_mosyle(userinfo)
	userinfo = dsmreftab.create_user_reftab(userinfo)

	if "mosyle_resp" in userinfo and userinfo['mosyle_resp'] != "success":
		print("Mosyle user creation error:")
		pprint(mosyle_resp, width=75)

	if "reftab_resp" in userinfo and userinfo['reftab_resp'] != "success":
		print("Reftab user creation error")
		pprint(reftab_resp, width=75)

	if "google_resp" in userinfo and userinfo['google_resp'] != "success":
		print("Google user creation error")
		pprint(userinfo['google_error'], width=75)
	else:
		if userinfo['test_mode'] == False:
			answer = input("Would you like to see the user's groups? (y/n)")

			if answer == 'y':
				if "google_groups_resp" in userinfo:
					pprint(userinfo['google_groups_resp'], width=75)
				elif len(userinfo['google_groups_resp']) < 1:
					print("No Groups")

	if userinfo['test_mode'] == True:
		os.system("clear")
		pprint(userinfo, width=75)


if __name__ == '__main__':
    main()
