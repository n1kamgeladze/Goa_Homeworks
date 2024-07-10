# shevqmnat swori paroli
correct_password = "nika"

# shevqmnat araswori parolis shemtxvevashi carieli string
user_input = ""

# ar daprintos sanam swori paroli ar iqneba
while user_input != correct_password:
    # vtxovot momxmarebels paroli
    user_input = input("Enter the password: ")
    
    # shevamowmot tu paroli sworia
    if user_input != correct_password:
        print("Password is wrong, please try again.")
    else:
        print("Authorization successful!")