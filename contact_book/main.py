from models import Contact

contact1 = Contact(
    name="Alice Smith", 
    phone="+1 (555) 019-2834", 
    email="ALICE@example.com", 
    tags=["Work", "Friends"]
)
print(contact1) 
# Output: Contact(name='Alice Smith', phone='+15550192834', email='alice@example.com', tags=['Work', 'Friends'])

# This will raise a ValueError for the email
# contact2 = Contact(name="Bob", phone="123456789", email="bad-email", tags=[])
