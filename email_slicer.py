def email(email):
    username = email[:email.index("@")] # Use string method index within indexing
    domain = email[email.index("@") + 1:]  # email[x + 1: 0]
    print(f"Your username is {username}")
    print(f"Your domain is {domain}")

email(email = "raffiki@gmail.com")