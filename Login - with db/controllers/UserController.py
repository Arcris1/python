class User:
    def __init__(self, username, password, gender):
        self.username = username
        self.password = password
        self.gender = gender

    def display_info(self):
        print("Username: ", self.username)
        print("Password: ", self.password)
        print("Gender: ", self.gender)

    def validate_login(self, username, password):
        return self.username == username and self.password == password