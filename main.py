class User :

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

user_1 = User("001", "First User's Name")
user_2 = User("002", "Second User's Name")


print(user_1.followers)
