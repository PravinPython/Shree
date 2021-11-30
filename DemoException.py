class NumberOfAttempts(BaseException):
    def __init__(self,error):
        self.errorMessage=error

def take_user_data_input():
    name=input("Enter your Name :")
    for item in range(3):
        try:
            age=int(input("Enter your age:"))
        except valueError as v:
            # print(v.args)
            if item == 2:
                raise NumberOfAttempts("Number of attempts exceeds.....")
        else:
            break
    email=input("Enter your email:")
    return name,age,email

while True:
    try:
        data= take_user_data_input()
        if data:
            print(data)
        choice = input("Do you want to continue : Y/N")
        if choice.lower() in ['n','no']:
            break
    except NumberOfAttempts as e:
        print(e.errorMessage)