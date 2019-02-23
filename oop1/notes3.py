# class methods - @classmethod

class User:
    active = 100

    def __init__(self, first):
        self.first = first
        User.active += 1

    @classmethod
    def get_active_users(cls):   # note: we are passing the "class" instead of "self" in an instance method
        return (f"There are current {User.active} active users")


t = User('tom')
print(User.get_active_users())