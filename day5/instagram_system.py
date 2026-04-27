# instagram_system.py

class InstagramAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password   # private
        self.__reels = ["Public Reel 1", "Private Reel 2", "Archived Reel 3"]

    def show_public_reels(self):
        print("Public Reels:", self.__reels[0])

    def show_private_reels(self, is_follower):
        if is_follower:
            print("Private Reel:", self.__reels[1])
        else:
            print("Access Denied")

    def show_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reel:", self.__reels[2])
        else:
            print("Wrong Password")


# Example usage
acc = InstagramAccount("user123", "1234")

acc.show_public_reels()
acc.show_private_reels(True)
acc.show_archived_reels("1234")
