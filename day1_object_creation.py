class Use:
    def __new__(cls):
        print("Object is created")
        return super().__new__(cls)
    def __init__(self):
        print("Object is initialized")

obj = Use()