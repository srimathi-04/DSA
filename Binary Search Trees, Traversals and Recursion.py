#QUESTION 1: As a senior backend engineer at Jovian, you are tasked with
#developing a fast in-memory data structure to manage profile information
#(username, name and email) for 100 million users. It should allow the following
#operations to be performed efficiently:
#1. Insert the profile information for a new user.
#2. Find the profile information of a user, given their username
#3. Update the profile information of a user, given their username
#4. List all the users of the platform, sorted by username
#You can assume that usernames are unique.





class User:
  def __init__(self, username,name,email):
    self.username = username
    self.name = name
    self.email = email
  def __repr__(self):
    return "User(username='{}', name='{}', email='{}')".format(self.username,self.name,self.email)
  def __str__(self):
    return self.__repr__()



class UserDatabase:
  def __init__(self):
    self.users=[]

#insert
  def insert(self,user):
    i=0
    while i<len(self.users):
      if self.users[i].username > user.username: 
        #a,b,g  new= c,   g>c => g is replaced by c
        break
      i+=1
    self.users.insert(i,user)

#find
  def find(self,username):
    for user in self.users:
      if user.username == username:
        return user

#update
  def update(self,user):
    target = self.find(user.username)
    target.name , target.email = user.name , user.email

#list
  def list_all(self):
    return self.users

#USERDATA
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh  = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

#USERS
users = [aakash,biraj,hemanth,jadhesh,siddhant,sonaksh,vishal]  #sorted

#insert
print("INSERTING USERS IN DATABASE")
database = UserDatabase()
database.insert(hemanth)
database.insert(aakash)
database.insert(biraj)

print(database.users)

#find
print("FIND USER")
user = database.find("siddhant")
user1 = database.find("aakash")

print(user)
print(user1)

#update
print("UPDATE USER INFO")

database.update(User(username='aakash', name='Aakash R', email='aakash@example.com'))
user = database.find('aakash')
print(user)

#list all
print("LIST ALL THE USERS")
database.list_all()