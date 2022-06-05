import time

class Network:
  total_site_users = 0
  total_site_posts = 0
  user_database = []
  user_database_names = []
  user_database_posts = []

class User:
  total_site_users = 0
  def __init__(self, this_user_name):
    self.name = this_user_name
    self.age = int(input("How old is " + self.name + " ?:"))
    self.email = str(self.name + "@gmail.com")
    self._password = str(self.name + str(self.age))
    self.friends = 0
    self.posts = []
    self.post_count = 0
    Network.total_site_users += 1
    Network.user_database.append(self)
    Network.user_database_names.append(self.name)
    print(Network.user_database_names)

  def add_friend(self, friend_name):
    print(self.name + " and " + friend_name + " are now friends!")
    self.friends += 1 

  def remove_friend(self, friend_name):
    print(self.name + " and " + friend_name + " are no longer friends.")
    self.friends -= 1
  
  def add_post(self, post):
    self.posts.append(post)
    self.post_count += 1
    Network.total_site_posts += 1
    Network.user_database_posts.append(post)

class Post:
  def __init__(self, this_post_content, poster_name):
    self.name = poster_name
    post_time = time.time()
    self.time = time.ctime(post_time)
    self.text = this_post_content
    self.likes = 0
    self.liked_by = []

  def add_like(self, friend_name):
    self.likes += 1
    print(friend_name + " liked your post!")  
    self.liked_by.append(friend_name)
    