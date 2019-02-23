def being_polite(func):
    def another():
        print("Good Morning!")
        func()
    return another