import user

user_1 = user.User("Karen")
user_2 = user.User("Stephanie")
user_3 = user.User("Adrienne")
user_4 = user.User("Sarah")
user_5 = user.User("Chris")
user_6 = user.User("Angelo")
user_7 = user.User("Joshua")


Karen_post = user.Post("It's beautiful spring weather outside. Can't wait for the summer!")
Karen_1.add_post(Karen_post)
Karen_post.add_like("Denise")
Karen_post.add_like("Camelia")
Karen_post.add_like("Joshua")

Angelo_post = user.Post("Just purchased some fishing gear, can't wait for the weekend!")
Angelo_3.add_post(Karen_post)
Angelo_post.add_like("Sarah")
Angelo_post.add_like("Chris")

print("Chris' post: " + Karen_post.text)
print("Post liked by: " + str(Karen_post.liked_by))
print("Number of likes: " + str(Karen_post.likes))
print("Time of post: " + str(Karen_post.time))

print(user_1.name + " has " + str(user_1.friends) + " friends!")
print(user_2.name + " has " + str(user_2.friends) + " friends!")
print(user_3.name + " has " + str(user_3.friends) + " friends!")
print(user_4.name + " has " + str(user_4.friends) + " friends!")
print(user_5.name + " has " + str(user_5.friends) + " friends!")
print(user_6.name + " has " + str(user_6.friends) + " friends!")
print(user_7.name + " has " + str(user_7.friends) + " friends!")

print("There are " + str(user.Network.total_site_users) + " users on The Social Network!")

print("There are " + str(user.Network.total_site_posts) + " posts on The Social Network!")
