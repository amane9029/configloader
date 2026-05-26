import json 
from pathlib import Path

print("welcome to JSON Data Explorer")
print("Choose a dataset:")
print("1. Albums")
print("2. Comments")
print("3. posts")
print("4. users")


choice = input("Enter your optin:")

files = {
    "1": "albums.json",
    "2": "comments.json",
    "3": "posts.json",
    "4": "users.json",
}

if choice not in files:
    print("Invalid option selected")
    exit()

selected_file = files[choice]

file_path = Path("data") / selected_file

f = open(file_path)
data = json.load(f)
f.close()

print(json.dumps(data,indent = 4))

ask = input("Do you want specific data? (yes/no):")

if ask.lower() == "yes":
    print("Available fields:")
    print(data[0].keys())

    field = input("Which field do you want to see? ")

    if field not in data[0]:
        print("Invalid field selected")
        exit()
    
    for item in data:
        if field in item:
            print(item[field])



else:
    print("Okay, exiting...")

print("Thanks for using JSON Data Explorer")
