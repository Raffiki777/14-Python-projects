def email(email):
    username = email[:email.index("@")] # Use string method index within indexing
    domain = email[email.index("@") + 1:]  # email[x + 1: 0]
    print(f"Username: {username}")
    print(f"Domain: {domain}")

email(email = "raffiki@gmail.com")
