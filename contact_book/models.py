from dataclasses import dataclass, field
import re

@dataclass
class Contact:
    name: str
    phone: str
    email: str
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        """Python automatically runs this method immediately after initialization 
        to handle data validation and cleanup."""
        self.email = self.validate_email(self.email)
        self.phone = self.validate_phone(self.phone)

    def validate_email(self, email: str) -> str:
        """Validates that the email string follows a proper email format."""
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        cleaned_email = email.strip()
        
        if not re.match(email_regex, cleaned_email):
            raise ValueError(f"Invalid email format: '{email}'")
            
        return cleaned_email.lower()

    def validate_phone(self, phone: str) -> str:
        """Validates that the phone number contains 7 to 15 digits."""
        # Removes common formatting characters like spaces, dashes, or parentheses
        cleaned_phone = re.sub(r"[\s\-\(\)]", "", phone)
        
        # Regex checks for optional leading '+' followed by 7 to 15 digits
        phone_regex = r"^\+?[1-9]\d{6,14}$"
        if not re.match(phone_regex, cleaned_phone):
            raise ValueError(f"Invalid phone number format: '{phone}'. Must contain 7-15 digits.")
            
        return cleaned_phone
