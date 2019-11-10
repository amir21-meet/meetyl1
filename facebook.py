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
		friends_list=friends_list(email)
		

