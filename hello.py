def greet(name: str) -> str:
    """Provides a formal cloud-based greeting."""
    return f"Salutations, {name}! You have successfully accessed the GitHub Cloud Lab."

def farewell(name: str) -> str:
    """Provides a formal parting message."""
    return f"Goodbye, {name}! We appreciate your contribution to the Cloud environment."

if __name__ == "__main__":
    # Primary logic for Ominakavsar Abduganieva
    user_identity = ["World", "GitHub", "Ominakavsar"]
    for user in user_identity:
        print(greet(user))
    
    print("\n" + farewell("Abduganieva"))
