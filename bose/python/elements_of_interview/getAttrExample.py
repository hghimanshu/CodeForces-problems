{"pooler1":"pooler"}

class funcTest:
    def __init__(self):
        pass
    def pooler(self):
        print("Hello world")



if __name__ == "__main__":
    func = funcTest()
    getattr(func, 'pooler')()
