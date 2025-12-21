def login(func):
    def wrapper(*args,**kw):
        print("Access Granted")
        result = func(*args,**kw)
        print("Access Finished")
        return result
    return wrapper

@login
def dashboard():
    print("welcome to dashboard")

dashboard()