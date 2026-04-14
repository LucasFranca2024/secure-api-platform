def authenticate_user(username, password):
    # aqui você valida no banco depois
    if username == "admin" and password == "123":
        return {"id": 1, "username": username}
    return None
