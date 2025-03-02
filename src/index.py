def validate_credit_card(number):
    def luhn_algorithm(card_number):
        total = 0
        reverse_digits = card_number[::-1]
        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    def get_card_issuer(card_number):
        card_issuers = {
            "Visa": ["4"],
            "MasterCard": ["51", "52", "53", "54", "55"],
            "American Express": ["34", "37"],
            "Discover": ["6011", "65"],
            "JCB": ["35"],
            "Diners Club": ["300", "301", "302", "303", "304", "305", "36", "38"],
            "EnRoute": ["2014", "2149"],
            "Voyager": ["8699"],
            "Hiper": ["637", "638", "639"],
            "Aura": ["50"]
        }
        for issuer, prefixes in card_issuers.items():
            if any(card_number.startswith(prefix) for prefix in prefixes):
                return issuer
        return "Unknown"

    if luhn_algorithm(number):
        return {
            "valid": True,
            "bandeira": get_card_issuer(number)
        }
    else:
        return {
            "valid": False,
            "bandeira": None
        }

# Example usage
card_number = "4111111111111111"
result = validate_credit_card(card_number)
print(result)