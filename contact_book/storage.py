import json


def load_contacts():
  """Reads the contacts.json file and returns a dictionary."""
  try:
      with open("contacts.json", "r", encoding="utf-8") as file:
          data = json.load(file)
      return data
  except FileNotFoundError:
    return {}



def save_contacts(data_dictionary):
  """Saves a dictionary back into the contacts.json file with formatting."""
  with open("contacts.json", "w", encoding="utf-8") as file:
    json.dump(data_dictionary, file, indent=2, ensure_ascii=False)
  print("contacts.json has been updated and saved!")



# Data we want to save
my_updated_contacts = {
    "contacts": [
        {"name": "Alice", "phone": "555-0123"},
        {"name": "Bob", "phone": "555-4567"},
        {"name": "Charlie", "phone": "555-9999"},
    ]
}

# Run our save function
save_contacts(my_updated_contacts)

# Optional: Run our load function to prove it works!
loaded_data = load_contacts()
print("Loaded Data:", loaded_data)
