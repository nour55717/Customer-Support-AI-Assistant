import re


class ContextCleaner:
    """
    Clean placeholders from retrieved documents and generated answers.
    """

    def __init__(self):

        self.replacements = {
            "website url": "the company's official website",
            "login page url": "the login page",
            "customer support phone number": "customer support",
            "customer support hours": "business hours",
            "online company portal info": "your account",
            "online order interaction": "Order History",
            "forgot password": "Forgot Password",
            "order number": "your order number",
            "tracking number": "your tracking number",
            "account number": "your account number",
            "person name": "the customer",
            "client name": "the customer",
            "client last name": "the customer",
            "salutation": "",
            "email": "your email address",
        }

    def clean(self, texts: list[str]) -> list[str]:

        cleaned = []

        for text in texts:

            if not text:
                cleaned.append("")
                continue

            for key, value in self.replacements.items():

                pattern = (
                    r"[`'\"]?"
                    r"\{\{\s*"
                    + re.escape(key)
                    + r"\s*\}\}"
                    r"[`'\"]?"
                )

                text = re.sub(
                    pattern,
                    value,
                    text,
                    flags=re.IGNORECASE,
                )

            # Remove any remaining placeholders
            text = re.sub(
                r"[`'\"]?\{\{.*?\}\}[`'\"]?",
                "",
                text,
                flags=re.IGNORECASE,
            )

            # Remove duplicate spaces
            text = re.sub(r"\s+", " ", text)

            cleaned.append(text.strip())

        return cleaned