import pymongo
import hashlib
import sys
from pymongo import MongoClient

if __name__ == '__main__':
	valid = 0
	#f = open("temp.txt", "a")
	client = MongoClient()
	db = client.test_database
	users = db.users

	
	while (valid == 0):
		d = input("Type L for Login, C for creating account: ")
		if (d.upper() == "L"):
			username = input("Username: ")
			pw = input("Password: ")
			pw_hash = hashlib.sha256(pw.encode())
			pw_hash_dig = pw_hash.hexdigest()

			count = db.users.find( { "Name" : username }).count()

			if(count == 0):
				print("user does not exist")
				valid = 0

			else:
				c2 = db.users.find( { "Name" : username , "Password" : pw_hash_dig}).count()
				if (c2 == 0):
					print("invalid password!")
					valid = 0
				else:
					print("Welcome, " + username)




			
		elif (d.upper() == "C"):
			#check if username is already taken
			username = input("Username: ")
			while (db.users.find( { "Name" : username }).count() != 0):
				print("Username already taken, try again")
				username = input("Username: ")
			#user_hash = hashlib.sha256(username.encode())
			#hdig = user_hash.hexdigest()


			#f.write(hdig)
			#f.write('\n')

			pw = input("Password: ")
			pw_hash = hashlib.sha256(pw.encode())
			pw_hash_dig = pw_hash.hexdigest()

			userAdd = {"Name" : username, "Password" : pw_hash_dig}
			user_id = users.insert_one(userAdd).inserted_id

			print("Added user " + username + ". Please log in")
			#f.write(pw_hash.hexdigest())
			#f.write('\n')
		elif(d.upper() == "X"):
			sys.exit()
		else:
			print("Invalid selection")


	#f.truncate(0)
	#f.close
