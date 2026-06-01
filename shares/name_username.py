class UserInfo:
    def add_user(self):
        name = input("Enter your name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")

        try:
            file = open("users.txt", "r")
            lines = file.readlines()
            file.close()
        except FileNotFoundError:
            lines = []
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue
            old_name, old_username, old_password = parts
            if old_username == username:
                print("Username already exists")
                return
        count = 0
        for ch in username:
            if ch >= "0" and ch <= "9":
                count += 1
        if count < 3:
            print("Username must contain at least 3 digits")
            return
        file = open("users.txt", "a")
        file.write(name + "," + username + "," + password + "\n")
        file.close()
        print("User saved successfully")


if __name__ == "__main__":
    user_info = UserInfo()
    user_info.add_user()
