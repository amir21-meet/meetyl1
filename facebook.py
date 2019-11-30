class Posts(object):
	def __init__(self,name,day,date,message):
		self.name = name
		self.day = day
		self.date = date
		self.message = message



class User(object):
	def __init__(self,name,email,password,friends_list,posts):
		friends_list=[]
		posts=[]
		self.name = name
		self.email = email
		self.password = password
		self.friends_list = friends_list
		self.posts = posts
	def add_friend(self,email):
		self.friends_list.append(email)
	def remove_friend(self,email):
		self.friends_list.remove(email)
	def post(self,text):

		post1 = Posts("Amir","Sunday","17/11/2019", text)
		self.posts.append(post1)
		print(self.posts)

user1 = User("Amir","amirsamidarwish@gmail.com","meet",0,0)
user2 = User("Jenny","jenny@gmail.com","meet",0,0)
user3 = User("Sadeq","sadeq@gmail.com","meet",0,0)
user4 = User("Mousa","mousa@gmail.com","meet",0,0)
users_name={user1.name,user2.name,user3.name,user4.name}
users_password={user1.password,user2.password,user3.password,user4.password}
users_friend={user1.name,user2.name,user3.name,user4.name}
friends_list=[]
user_post=[]
yes=("y,yes,Yes,YES")
no = ("no,no,No,NO")
profile=("MyProfile,Myprofile,myprofile,myProfile,profile,Profile")
security=("Password,password")
friends=("Friends,friends,friend,myfriend,myfriends,MyFriend,myFriend,MyFriends,myFriends")
logout=("logout,Logout,LogOut,LOGOUT")
users_posts=("posts,post,POST,POSTS,Post,Posts")
Name =input("YourName: ")
if Name not in users_name:
	print("Sorry Try Again")
	exit()
else:
	print("Correct")

Password =input("Yourpassword: ")
if Password not in users_password:
	print("Try Again")
	exit()
else:
	print("Correct")


Options = input("Do You Want Add a Friend :")
if Options in yes:
	Friend = input("Type Friends Name?")
	if Friend in users_friend:
		print(Name+" has added " + Friend +" as  a friend")
		friends_list.append(Friend)
	else:
		print("Sorry")
else:
	print("skipping")

Profile = input("MyProfile,Security,Friends,,Posts,Logout :")
if Profile in profile:
	print("-------------------------Your Profile----------------------------")
	print("Name: "+Name)
	print("Password: "+Password)
	print("Friends:"+str(friends_list))
if Profile in security:
	input("Do you want to change Your Password? ")
	if yes:
		input("Current Password")
		if users_password:
			input("New Password")
		else:
			print("Try Again")
if Profile in friends:
	print(friends_list)
	input("Do you want To Add a friend? ")
	if yes:
		print(Options)
	else:
		print("-__-")
if Profile in logout:
	print("-----------------------------Thank You-------------------------------")
	exit()
if Profile in users_posts:
	print("Your Posts"+str(user_post))
	input("Do You Want To Post Something?yes/no")
	if yes:
		input("YourPost: ")
		user_post.append(user_post)

Profile = input("MyProfile,Password,Friends,Posts,Logout :")

if Profile in profile:
	print("-------------------------Your Profile----------------------------")
	print("Name: "+Name)
	print("Password: "+Password)
	print("Friends:"+str(friends_list))
if Profile in security:
	input("Do you want to change Your Password? ")
	if yes:
		input("Current Password")
		if users_password:
			input("New Password")
		else:
			print("Try Again")
if Profile in friends:
	print(friends_list)
	input("Do you want To Add a friend? ")
	if yes:
		print(Options)
	else:
		print("-__-")
if Profile in logout:
	print("-----------------------------Thank You-------------------------------")
	exit()
if Profile in users_posts:
	print("Your Posts"+str(user_post))
	input("Do You Want To Post Something?yes/no")
	if yes:
		input("YourPost: ")
		user_post.append(user_post)
Profile = input("MyProfile,Security,Friends,,Posts,Logout :")

if Profile in profile:
	print("-------------------------Your Profile----------------------------")
	print("Name: "+Name)
	print("Password: "+Password)
	print("Friends:"+str(friends_list))
if Profile in friends:
	print(friends_list)
	input("Do you want To Add a friend? ")
	if yes:
		print(Options)
	else:
		print("-__-")

if Profile in security:
	input("Do you want to change Your Password? ")
	if yes:
		input("Current Password")
		if users_password:
			input("New Password")
		else:
			print("Try Again")
if Profile in logout:
	print("-----------------------------Thank You-------------------------------")
	exit()
if Profile in users_posts:
	print("Your Posts"+str(user_post))
	input("Do You Want To Post Something?yes/no")
	if yes:
		input("YourPost: ")
		user_post.append(user_post)
Profile = input("MyProfile,Security,Friends,Posts,Logout :")
if Profile in profile:
	print("-------------------------Your Profile----------------------------")
	print("Name: "+Name)
	print("Password: "+Password)
	print("Friends:"+str(friends_list))
if Profile in logout:
	print("-----------------------------Thank You-------------------------------")
	exit()
if Profile in security:
	input("Do you want to change Your Password? ")
	if yes:
		input("Current Password")
		if users_password:
			input("New Password")
		else:
			print("Try Again")
if Profile in friends:
	print(friends_list)
	input("Do you want To Add a friend? ")
	if yes:
		print(Options)
	else:
		print("-__-")
if Profile in users_posts:
	print()
	input("Do You Want To Post Something?yes/no")
	if yes:
		input("YourPost: ")
		user_post.append(user_post)

Profile = input("MyProfile,Security,Friends,Posts,Logout :")
if Profile in profile:
	print("-------------------------Your Profile----------------------------")
	print("Name: "+Name)
	print("Password: "+Password)
	print("Friends:"+str(friends_list))
if Profile in logout:
	print("-----------------------------Thank You-------------------------------")
	exit()
if Profile in security:
	input("Do you want to change Your Password? ")
	if yes:
		input("Current Password")
		if users_password:
			input("New Password")
		else:
			print("Try Again")
if Profile in friends:
	print(friends_list)
	input("Do you want To Add a friend? ")
	if yes:
		print(Options)
	else:
		print("-__-")
if Profile in users_posts:
	print()
	input("Do You Want To Post Something?yes/no")
	if yes:
		input("YourPost: ")
		user_post.append(user_post)





