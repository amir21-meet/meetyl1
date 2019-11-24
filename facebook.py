class Posts(object):
	def __init__(self,name,day,date,message):
		self.name = name
		self.day = day
		self.date = date
		self.message = message

x=1
print(x)
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
		print(self.name+"	has added " + email +" as  a friend")
	def remove_friend(self,email):
		self.friends_list.remove(email)
		print(self.name+"xhas removed " + email +" as  a friend")
	def post(self,text):

		post1 = Posts("Amir","Sunday","17/11/2019", text)
		self.posts.append(post1)
		print(self.posts)
		print(self.name +"has posted:" + text)
	def get_userinfo(self):
		print("Name:" + self.name)
		print("Email:" + self.email)
		print("Password:" + self.password)
		print("Friends:" + str(self.friends_list))
		print("Posts:" + str(self.posts))

user1 = User("Amir","amirsamidarwish@gmail.com","a0522906096D",0,0)
user2 = User("Celine","celineyaghi@gmail.com","cece",0,0)

user1.add_friend(user2.email)
user1.post("Hi Ana Celine")
user1.get_userinfo()
user1.remove_friend(user2.email)


