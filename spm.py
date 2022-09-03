import json
import base64

print("Welcome to my Password Manager")
print("\n1. Add Data")
print("2. Show Data")

user_input = input("Option - > ")

if (user_input == "1"):
    username = input("Username : ")
    password = input("Password : ")
    website = input("Website : ")

    with open("data.txt", 'w') as f:
        data = 'Website : ', website, ' | ', 'Username : ', username, ' | ', 'Password : ', password
        input_data = str(data)
        input_bytes = input_data.encode('ascii')

        base64_bytes = base64.b64encode(input_bytes)
        base64_string = base64_bytes.decode("ascii")

        f.write(str(base64_string))

if (user_input == "2"):
    
    with open ("data.txt", 'r') as user_data_r:
        user_data = user_data_r.read()
        needs_to_decode = str(user_data)

        base64_string = needs_to_decode
        base64_bytes = base64_string.encode("ascii")

        decoded_string_bytes = base64.b64decode(base64_bytes)
        decoded_data = decoded_string_bytes.decode("ascii")

        print(decoded_data)

        


