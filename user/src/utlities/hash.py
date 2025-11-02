from argon2 import PasswordHasher, exceptions
import string

ph = PasswordHasher()


class PasswordManager:
    @classmethod
    def is_strong(cls, s: str) -> bool:
        """Check for uppercase, lowercase, digit, and special char"""
        has_upper = any(c.isupper() for c in s)
        has_lower = any(c.islower() for c in s)
        has_digit = any(c.isdigit() for c in s)
        has_special = any(c in string.punctuation for c in s)
        return has_upper and has_lower and has_digit and has_special

    @classmethod
    def set_password(cls, password: str) -> str:
        """Hash password if strong, else raise ValueError"""
        if len(password) >= 8 and cls.is_strong(password):
            return ph.hash(password) 
        raise ValueError(
            "Password must be at least 8 characters long and include uppercase, lowercase, digit, and special character."
        )

    @classmethod
    def verify(cls, hashed: str, password: str) -> bool:
        """Verify password against a hash"""
        try:
            return ph.verify(hashed, password)
        except exceptions.VerifyMismatchError:
            return False
