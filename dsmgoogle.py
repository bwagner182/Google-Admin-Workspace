"""
This file will hold my work with the Google Admin API to allow for
better testing and code readability
"""

from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from pprint import pprint

import keys


SCOPES = [
			'https://www.googleapis.com/auth/admin.directory.user',
			'https://www.googleapis.com/auth/admin.directory.user.security',
			'https://apps-apis.google.com/a/feeds/alias/',
			'https://www.googleapis.com/auth/admin.directory.user.alias',
			'https://apps-apis.google.com/a/feeds/groups/',
			'https://www.googleapis.com/auth/admin.directory.group.member'
			]


def create_user_google(userinfo):
	creds = None
	# The file token.json stores the user's access and refresh tokens, and is
	# created automatically when the authorization flow completes for the first
	# time.
	if os.path.exists('token.json'):
		creds = Credentials.from_authorized_user_file('token.json', SCOPES)
	# If there are no (valid) credentials available, let the user log in.
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file(
				'credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
		# Save the credentials for the next run
		with open('token.json', 'w') as token:
			token.write(creds.to_json())

	service = build('admin', 'directory_v1', credentials=creds)

	# Build out user object
	userinfo['org_unit'] = ""
	userinfo['groups'] = ['03l18frh32ojm10', '03o7alnk1bd3k5c']

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
			case _:
				print("Unable to recognize the employee's title. Consult the application developer and give them the error below.")
				print("ERROR: Incorrect title entered. Provided input: " + userinfo['title'])
				exit(1)

	city = ""
	if len(userinfo['home_city']) > 3:
		if userinfo['home_city'].lower() == "st. louis":
			city = "stl"
		elif userinfo['home_city'].lower() == "atlanta":
			city = "atl"
		elif userinfo['home_city'].lower() == "tampa":
			city = "tpa"
		elif userinfo['home_city'].lower() == "miami":
			city = "mia"
		elif userinfo['home_city'].lower() == "nashville" or userinfo['home_city'].lower() == "nash":
			city = "nsh"
	else:
		city = userinfo['home_city']

	match city:
		case "atl":
			userinfo['org_unit'] = userinfo['org_unit'] + "/Atlanta"
			userinfo['groups'].append("01opuj5n4frlm0x")
			match userinfo['title_short'].lower():
				case "aae":
					# Add user to drivestl.com>Atlanta>Account Executive OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Account Executive"
					# Add user to userinfo['groups']
					userinfo['groups'].append("026in1rg3muty9l")
				case "ados":
					# Add user to drivestl.com>Atlanta>Associate Director of Strategy OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Associate Director of Strategy"
				case "adoo":
					# Add user to drivestl.com>Atlanta>Associate Director of Operations OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Associate Director Operations"
				case "ae":
					# Add user to drivestl.com>Atlanta>Account Executive OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Account Executive"
					# Add user to userinfo['groups']
					userinfo['groups'].append("026in1rg3muty9l")
				case "bd":
					# Add user to drivestl.com>Atlanta>Business Developer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Business Developer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("03dy6vkm31u1guq")
				case "cm":
					# Add user to drivestl.com>Atlanta>Community Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Community Manager"
				case "cw":
					# Add user to drivestl.com>Atlanta>Copywriter OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Copywriter"
					# Add user to userinfo['groups']
					userinfo['groups'].append("039kk8xu3rstfjy")
					userinfo['groups'].append("03o7alnk2gh07zy")
				case "cd":
					# Add user to drivestl.com>Atlanta>Creative Director OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Creative Director"
					# Add user to userinfo['groups']
				case "mm":
					# Add user to drivestl.com>Atlanta>Developers OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Developer"
					# Add user to userinfo['groups']
				case "doa":
					# Add user to drivestl.com>Atlanta>Director of Analytics OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Analytics"
					# Add user to userinfo['groups']
					userinfo['groups'].append("03ep43zb3nwj23j")
					userinfo['groups'].append("02dlolyb4bv2zpf")
				case "am":
					# Add user to drivestl.com>Atlanta>Digital Analyst OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Digital Analyst"
					# Add user to userinfo['groups']
					userinfo['groups'].append("03ep43zb3nwj23j")
					userinfo['groups'].append("02dlolyb4bv2zpf")
				case "dbd":
					# Add user to drivestl.com>Atlanta>Director of Business Development OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Business Development"
					# Add user to userinfo['groups']
					userinfo['groups'].append("03dy6vkm31u1guq")
				case "dcw":
					# Add user to Drivestl.com>Atlanta>Director of Copywriting OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Copywriting"
					# Add user to userinfo['groups']
					userinfo['groups'].append("039kk8xu3rstfjy")
					userinfo['groups'].append("03o7alnk2gh07zy")
				case "dfch":
					# Add user to drivestl.com>Atlanta>Director of Franchise OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Franchise"
				case "dhr":
					# Add user to drivestl.com>Atlanta>Director of HR OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Human Resources"
				case "doo":
					# Add user to drivestl.com>Atlanta>Director of Operations OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Operations"
				case "dor":
					# Add user to drivestl.com>Atlanta>Director of Recruiting OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Recreuiting"
				case "rcr":
					# Add user to drivestl.com>Atlanta>Recruiter OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Recruiter"
				case "dss":
					# Add user to drivestl.com>Atlanta>Director of Social Strategy OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Social Strategy"
				case "dvp":
					# Add user drivestl.com>Atlanta>Director of Videography and Photography OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Videography and Photography"
					# Add user to userinfo['groups']
					userinfo['groups'].append("03whwml42fzm6zl")
				case "gd":
					# Add user to drivestl.com>Atlanta>Graphic Designer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Graphic Designer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("02afmg282x7059d")
					userinfo['groups'].append("01pxezwc1r0v4xc")
				case "lead":
					# Add user to drivestl.com>Atlanta>Leadership OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Leadership"
				case "oa":
					# Add user to drivestl.com>Atlanta>Office Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Office Administrator"
				case "p/v":
					# Add user to drivestl.com>Atlanta>Photographer - Videographer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Photographer - Videographer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("03whwml42fzm6zl")
				case "pm":
					# Add user to drivestl.com>Atlanta>Project Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Project Manager"
					# Add user to userinfo['groups']
					userinfo['groups'].append("00z337ya246ggr2")
				case "web":
					# Add user to drivestl.com>Atlanta>Developer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Developer"
					# Add user to userinfo['groups']
		case "stl":
			userinfo['org_unit'] = userinfo['org_unit'] + "/St. Louis"
			userinfo['groups'].append("02250f4o22xony2")
			match userinfo['title_short'].lower():
				case "aae":
					# Add user to drivestl.com>St. Louis>Account Executive OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Account Executive"
					# Add user to userinfo['groups']
					userinfo['groups'].append("02dlolyb38n5zqy")
				case "ados":
					# Add user to drivestl.com>St. Louis>Associate Director of Strategy OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Associate Director of Strategy"
				case "adoo":
					# Add user to drivestl.com>St. Louis>Associate Director of Operations OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Associate Director Operations"
				case "ae":
					# Add user to drivestl.com>St. Louis>Account Executive OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Account Executive"
					# Add user to userinfo['groups']
					userinfo['groups'].append("02dlolyb38n5zqy")
				case "bd":
					# Add user to drivestl.com>St. Louis>Business Developer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Business Developer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("023ckvvd42s1399")
				case "cm":
					# Add user to drivestl.com>St. Louis>Community Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Community Manager"
					# Add user to userinfo['groups']
					userinfo['groups'].append("01opuj5n1g3uqe9")
				case "cw":
					# Add user to drivestl.com>St. Louis>Copywriter OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Copywriter"
					# Add user to userinfo['groups']
					userinfo['groups'].append("01tuee741ixbnww")
					userinfo['groups'].append("03o7alnk2gh07zy")
				case "cd":
					# Add user to drivestl.com>St. Louis>Creative Director OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Creative Director"
				case "mm":
					# Add user to drivestl.com>St. Louis>Developers OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Developer"
				case "doa":
					# Add user to drivestl.com>St. Louis>Director of Analytics OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Analytics"
					# Add user to userinfo['groups']
					userinfo['groups'].append("03x8tuzt2z8a6u8")
					userinfo['groups'].append("02dlolyb4bv2zpf")
				case "am":
					# Add user to drivestl.com>St. Louis>Digital Analyst OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Digital Analyst"
					# Add user to userinfo['groups']
					userinfo['groups'].append("03x8tuzt2z8a6u8")
					userinfo['groups'].append("02dlolyb4bv2zpf")
				case "dbd":
					# Add user to drivestl.com>St. Louis>Director of Business Development OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Business Development"
					# Add user to userinfo['groups']
					userinfo['groups'].append("023ckvvd42s1399")
				case "dcw":
					# Add user to Drivestl.com>St. Louis>Director of Copywriting OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Copywriting"
					# Add user to userinfo['groups']
					userinfo['groups'].append("01tuee741ixbnww")
					userinfo['groups'].append("03o7alnk2gh07zy")
				case "dfch":
					# Add user to drivestl.com>St. Louis>Director of Franchise OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Franchise"
				case "dhr":
					# Add user to drivestl.com>St. Louis>Director of HR OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Human Resources"
				case "doo":
					# Add user to drivestl.com>St. Louis>Director of Operations OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Operations"
				case "dor":
					# Add user to drivestl.com>St. Louis>Director of Recruiting OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Recruiting"
				case "rcr":
					# Add user to drivestl.com>St. Louis>Recruiter OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Recruiter"
				case "dss":
					# Add user to drivestl.com>St. Louis>Director of Social Strategy OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Social Strategy"
				case "dvp":
					# Add user to drivestl.com>St. Louis>Director of Videography and Photography OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Videography and Photography"
					# Add user to userinfo['groups']
					userinfo['groups'].append('046r0co22dwkvwl')
				case "gd":
					# Add user to drivestl.com>St. Louis>Graphic Designer
					userinfo['org_unit'] = userinfo['org_unit'] + "/Graphic Designer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("01d96cc028hge2y")
					userinfo['groups'].append("01pxezwc1r0v4xc")
				case "lead":
					# Add user to drivestl.com>St. Louis>Leadership OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Leadership"
				case "oa":
					# Add user to drivestl.com>St. Louis>Office Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Office Admin"
				case "p/v":
					# Add user to drivestl.com>St. Louis>Photographer - Videographer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Photographer - Videographer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("046r0co22dwkvwl")
				case "pm":
					# Add user to drivestl.com>St. Louis>Project Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Project Manager"
					# Add user to userinfo['groups']
					userinfo['groups'].append("03bj1y3824riiqg")
				case "web":
					# Add user to drivestl.com>St. Louis>Developer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Developer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("045jfvxd49srolp")
		case "nsh":
			userinfo['org_unit'] = userinfo['org_unit'] + "/Nashville"
			userinfo['groups'].append("00xvir7l4j91awi")
			match userinfo['title_short'].lower():
				case "aae":
					# Add user to drivestl.com>Nashville>Account Executive OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Account Executive"
					# Add user to userinfo['groups']
					userinfo['groups'].append("03oy7u291f8spdb")
				case "ados":
					# Add user to drivestl.com>Nashville>Associate Director of Strategy OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Associate Director of Strategy"
				case "adoo":
					# Add user to drivestl.com>Nashville>Associate Director of Operations OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Associate Director Operations"
				case "ae":
					# Add user to drivestl.com>Nashville>Account Executive OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Account Executive"
					# Add user to userinfo['groups']
					userinfo['groups'].append("03oy7u291f8spdb")
				case "bd":
					# Add user to drivestl.com>Nashville>Business Developer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Business Developer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("04anzqyu4kp42n2")
				case "cm":
					# Add user to drivestl.com>Nashville>Community Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Community Manager"
					# Add user to userinfo['groups']
					userinfo['groups'].append("cmnash")
				case "cw":
					# Add user to drivestl.com>Nashville>Copywriter OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Copywriter"
					# Add user to userinfo['groups']
					userinfo['groups'].append("01d96cc03a3wdkw")
					userinfo['groups'].append("03o7alnk2gh07zy")
				case "cd":
					# Add user to drivestl.com>Nashville>Creative Director OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Creative Director"
				case "mm":
					# Add user to drivestl.com>Nashville>Developers OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Developer"
				case "doa":
					# Add user to drivestl.com>Nashville>Director of Analytics OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Analytics"
					# Add user to userinfo['groups']
					userinfo['groups'].append("02iq8gzs3m29blf")
					userinfo['groups'].append("02dlolyb4bv2zpf")
				case "am":
					# Add user to drivestl.com>Nashville>Digital Analyst OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Digital Analyst"
					# Add user to userinfo['groups']
					userinfo['groups'].append("02iq8gzs3m29blf")
					userinfo['groups'].append("02dlolyb4bv2zpf")
				case "dbd":
					# Add user to drivestl.com>Nashville>Director of Business Development OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Business Development"
					# Add user to userinfo['groups']
					userinfo['groups'].append("04anzqyu4kp42n2")
				case "dcw":
					# Add user to Drivestl.com>Nashville>Director of Copywriting OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Copywriting"
					# Add user to userinfo['groups']
					userinfo['groups'].append("01d96cc03a3wdkw")
					userinfo['groups'].append("03o7alnk2gh07zy")
				case "dfch":
					# Add user to drivestl.com>Nashville>Director of Franchise OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Franchise"
				case "dhr":
					# Add user to drivestl.com>Nashville>Director of HR OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Human Resources"
				case "doo":
					# Add user to drivestl.com>Nashville>Director of Operations OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Operations"
				case "dor":
					# Add user to drivestl.com>Nashville>Director of Recruiting OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Recruiting"
				case "rcr":
					# Add user to drivestl.com>Nashville>Recruiter OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Recruiter"
				case "dss":
					# Add user to drivestl.com>Nashville>Director of Social Strategy OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Social Strategy"
				case "dvp":
					# Add user to drivestl.com>Nashville>Director of Videography and Photography OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Videography and Photography"
					# Add user to userinfo['groups']
					userinfo['groups'].append("01y810tw0h96ffg")
				case "gd":
					# Add user to drivestl.com>Nashville>Graphic Designer
					userinfo['org_unit'] = userinfo['org_unit'] + "/Graphic Designer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("01qoc8b121jf1b7")
					userinfo['groups'].append("01pxezwc1r0v4xc")
				case "lead":
					# Add user to drivestl.com>Nashville>Leadership OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Leadership"
				case "oa":
					# Add user to drivestl.com>Nashville>Office Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Office Admin"
				case "p/v":
					# Add user to drivestl.com>Nashville>Photographer - Videographer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Photographer - Videographer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("01y810tw0h96ffg")
				case "pm":
					# Add user to drivestl.com>Nashville>Project Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Project Manager"
					# Add user to userinfo['groups']
					userinfo['groups'].append("04bvk7pj35skvwo")
				case "web":
					# Add user to drivestl.com>Nashville>Developer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Developer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("025b2l0r4e0wos7")
		case "mia":
			userinfo['org_unit'] = userinfo['org_unit'] + "/Miami"
			userinfo['groups'].append("0147n2zr1uqnpyg")
			match userinfo['title_short'].lower():
				case "aae":
					# Add user to drivestl.com>Miami>Account Executive OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Account Executive"
					# Add user to userinfo['groups']
					userinfo['groups'].append("02250f4o0pk3ne6")
				case "ados":
					# Add user to drivestl.com>Miami>Associate Director of Strategy OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Associate Director of Strategy"
				case "adoo":
					# Add user to drivestl.com>Miami>Associate Director of Operations OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Associate Director Operations"
				case "ae":
					# Add user to drivestl.com>Miami>Account Executive OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Account Executive"
					# Add user to userinfo['groups']
					userinfo['groups'].append("02250f4o0pk3ne6")
				case "bd":
					# Add user to drivestl.com>Miami>Business Developer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Business Developer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("02nusc192m9i40d")
				case "cm":
					# Add user to drivestl.com>Miami>Community Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Community Manager"
					# Add user to userinfo['groups']
					userinfo['groups'].append("cmmiami")
				case "cw":
					# Add user to drivestl.com>Miami>Copywriter OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Copywriter"
					# Add user to userinfo['groups']
					userinfo['groups'].append('03fwokq034dfz8j')
					userinfo['groups'].append("03o7alnk2gh07zy")
				case "cd":
					# Add user to drivestl.com>Miami>Creative Director OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Creative Director"
				case "mm":
					# Add user to drivestl.com>Miami>Developers OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Developer"
				case "doa":
					# Add user to drivestl.com>Miami>Director of Analytics OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Analytics"
					# Add user to userinfo['groups']
					userinfo['groups'].append("0111kx3o0h8c0rw")
					userinfo['groups'].append("02dlolyb4bv2zpf")
				case "am":
					# Add user to drivestl.com>Miami>Digital Analyst OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Digital Analyst"
					# Add user to userinfo['groups']
					userinfo['groups'].append("0111kx3o0h8c0rw")
					userinfo['groups'].append("02dlolyb4bv2zpf")
				case "dbd":
					# Add user to drivestl.com>Miami>Director of Business Development OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Business Development"
					# Add user to userinfo['groups']
					userinfo['groups'].append("02nusc192m9i40d")
				case "dcw":
					# Add user to Drivestl.com>Miami>Director of Copywriting OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Copywriting"
					# Add user to userinfo['groups']
					userinfo['groups'].append("03fwokq034dfz8j")
					userinfo['groups'].append("03o7alnk2gh07zy")
				case "dfch":
					# Add user to drivestl.com>Miami>Director of Franchise OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Franchise"
				case "dhr":
					# Add user to drivestl.com>Miami>Director of HR OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Human Resources"
				case "doo":
					# Add user to drivestl.com>Miami>Director of Operations OU
					userinfo['org_unit'] = userinfo['org_unit'] +"/Director of Operations"
				case "dor":
					# Add user to drivestl.com>Miami>Director of Recruiting OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Recruiting"
				case "rcr":
					# Add user to drivestl.com>Miami>Recruiter OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Recruiter"
				case "dss":
					# Add user to drivestl.com>Miami>Director of Social Strategy OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Social Strategy"
				case "dvp":
					# Add user to drivestl.com>Miami>Director of Videography and Photography OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Videography and Photography"
					# Add user to userinfo['groups']
					userinfo['groups'].append("04anzqyu0hvk4qe")
				case "gd":
					# Add user to drivestl.com>Miami>Graphic Designer
					userinfo['org_unit'] = userinfo['org_unit'] + "/Graphic Designer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("02jxsxqh1zq45u9")
					userinfo['groups'].append("01pxezwc1r0v4xc")
				case "lead":
					# Add user to drivestl.com>Miami>Leadership OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Leadership"
				case "oa":
					# Add user to drivestl.com>Miami>Office Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Office Admin"
				case "p/v":
					# Add user to drivestl.com>Miami>Photographer - Videographer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "Photographer - Videographer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("04anzqyu0hvk4qe")
				case "pm":
					# Add user to drivestl.com>Miami>Project Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Project Manager"
					# Add user to userinfo['groups']
					userinfo['groups'].append("041mghml0joav79")
				case "web":
					# Add user to drivestl.com>Miami>Developer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Developer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("025b2l0r4e0wos7")
		case "tpa":
			userinfo['org_unit'] = userinfo['org_unit'] + "/Tampa"
			userinfo['groups'].append("04i7ojhp0rm8evs")
			match userinfo['title_short'].lower():
				case "aae":
					# Add user to drivestl.com>Tampa>Account Executive OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Account Executives"
					# Add user to userinfo['groups']
					userinfo['groups'].append("043ky6rz414eajf")
				case "ados":
					# Add user to drivestl.com>Tampa>Associate Director of Strategy OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Associate Director of Strategy"
				case "adoo":
					# Add user to drivestl.com>Tampa>Associate Director of Operations OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Associate Director of Operations"
				case "ae":
					# Add user to drivestl.com>Tampa>Account Executive OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Account Executives"
					# Add user to userinfo['groups']
					userinfo['groups'].append("043ky6rz414eajf")
				case "bd":
					# Add user to drivestl.com>Tampa>Business Developer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Business Developers"
					# Add user to userinfo['groups']
					userinfo['groups'].append("00z337ya28xmoku")
				case "cm":
					# Add user to drivestl.com>Tampa>Community Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Community Manager"
				case "cw":
					# Add user to drivestl.com>Tampa>Copywriter OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Copywriter"
					# Add user to userinfo['groups']
					userinfo['groups'].append("01ci93xb40oqui1")
					userinfo['groups'].append("03o7alnk2gh07zy")
				case "cd":
					# Add user to drivestl.com>Tampa>Creative Director OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Creative Director"
				case "mm":
					# Add user to drivestl.com>Tampa>Developers OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Developer"
				case "doa":
					# Add user to drivestl.com>Tampa>Director of Analytics OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Analytics"
					# Add user to userinfo['groups']
					userinfo['groups'].append("03cqmetx3cnrd76")
					userinfo['groups'].append("02dlolyb4bv2zpf")
				case "am":
					# Add user to drivestl.com>Tampa>Digital Analyst OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Digital Analyst"
					# Add user to userinfo['groups']
					userinfo['groups'].append("03cqmetx3cnrd76")
					userinfo['groups'].append("02dlolyb4bv2zpf")
				case "dbd":
					# Add user to drivestl.com>Tampa>Director of Business Development OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director pf Business Development"
					# Add user to userinfo['groups']
					userinfo['groups'].append("00z337ya28xmoku")
				case "dcw":
					# Add user to Drivestl.com>Tampa>Director of Copywriting OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Copywriting"
					# Add user to userinfo['groups']
					userinfo['groups'].append("01ci93xb40oqui1")
					userinfo['groups'].append("03o7alnk2gh07zy")
				case "dfch":
					# Add user to drivestl.com>Tampa>Director of Franchise OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Franchise"
				case "dhr":
					# Add user to drivestl.com>Tampa>Director of HR OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Human Resources"
				case "doo":
					# Add user to drivestl.com>Tampa>Director of Operations OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Operations"
				case "dor":
					# Add user to drivestl.com>Tampa>Director of Recruiting OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Recruiting"
				case "rcr":
					# Add user to drivestl.com>Tampa>Recruiter OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Recruiter"
				case "dss":
					# Add user to drivestl.com>Tampa>Director of Social Strategy OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Social Strategy"
				case "dvp":
					# Add user to drivestl.com>Tampa>Director of Videography and Photography OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Director of Videography and Photography"
					# Add user to userinfo['groups']
					userinfo['groups'].append("01hmsyys2pmrbqu")
				case "gd":
					# Add user to drivestl.com>Tampa>Graphic Designer
					userinfo['org_unit'] = userinfo['org_unit'] + "/Graphic Designer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("0111kx3o48ihide")
					userinfo['groups'].append("01pxezwc1r0v4xc")
				case "lead":
					# Add user to drivestl.com>Tampa>Leadership OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Leadership"
				case "oa":
					# Add user to drivestl.com>Tampa>Office Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Office Admin"
				case "p/v":
					# Add user to drivestl.com>Tampa>Photographer - Videographer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Photographer - Videographer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("01hmsyys2pmrbqu")
				case "pm":
					# Add user to drivestl.com>Tampa>Project Manager OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Project Manager"
					# Add user to userinfo['groups']
					userinfo['groups'].append("01y810tw0u14znz")
				case "web":
					# Add user to drivestl.com>Tampa>Developer OU
					userinfo['org_unit'] = userinfo['org_unit'] + "/Developer"
					# Add user to userinfo['groups']
					userinfo['groups'].append("025b2l0r4e0wos7")
		case _:
			print("New office? Contact the developer to have it added to the app.")
			print("Location entered: " + userinfo['home_city'])

	user = {
			"primaryEmail": userinfo['email_address'],
			"name": {
				"givenName": userinfo['fname'],
				"familyName": userinfo['lname']
				},
			"suspended": False,
			"password": keys.EMPLOYEE_PASSWORD,
			"changePasswordAtNextLogin": True,
			"ipWhitelisted": False,
			"ims": [],
			"emails": [],
			"addresses": [],
			"externalIds": [],
			"organizations": [],
			"phones": [],
			"orgUnitPath": userinfo['org_unit'],
			"includeInGlobalAddressList": True
			}

	# Double check for user email address first and confirm that the user
	# wants to create a new account if an account is found
	# (will need a new email address: userinfo['fname'][0-1] + userinfo['lname'] )

	result = service.users().insert(body=user).execute()
	
	if 'id' in result:
		userinfo['google'] = "success"
	else:
		userinfo['google'] = "fail"
		userinfo['google_error'] = result
		return userinfo

	# put code here to loop through userinfo['groups'] and add the user to applicable userinfo['groups']
	member = {
			"kind": "admin#directory#member",
			"email": userinfo['email_address'],
			"role": "MEMBER",
			"type": "USER",
			"delivery_settings": "ALL_MAIL",
		}
	group_resp = []	
	for group in userinfo['groups']:
		# print("Group ID: " + group)
		resp = service.members().insert(groupKey=group, body=member).execute()
		group_resp.append(resp)
		
	userinfo['google_groups_resp'] = group_resp
	return userinfo
