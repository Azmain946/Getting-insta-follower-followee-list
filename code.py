import instaloader
import csv

username=input() #whose follower list / followee list you want(must be start with '@')

directory=input() #where to save your file
filename=input() #name the csv file

# Get instance
L = instaloader.Instaloader()

# Login or load session
USER='' #put your username
PASSWORD='' #put your password
L.login(USER, PASSWORD)        # (login)


# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context,username)


with open(directory+filename+".csv",'w',encoding="utf-8",newline='') as f:
	writer=csv.DictWriter(f,fieldnames=["Username","URL"])
	writer.writeheader()
	for follower in profile.get_followers():
		writer.writerow({"Username":follower.username,"URL":"https://www.instagram.com/"+follower.username+"/"})

# (likewise with profile.get_followees())
