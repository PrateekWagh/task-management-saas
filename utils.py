import pwdlib
password_hash = pwdlib.PasswordHash.recommended()


def convert_password_to_hash(plain_password):
    return password_hash.hash(plain_password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)