import json 


def load_contacts():
  # 2. Open the file in 'r' (read) mode
  with open("contacts.json", "r", encoding="utf-8") as file:

    # 3. Read the file AND convert it to a dictionary all at once
    data = json.load(file)

  # 4. Return our brand new dictionary
  return data


# my_dictionary = load_contacts()

# print(my_dictionary)


