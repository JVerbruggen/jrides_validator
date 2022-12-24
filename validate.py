import hashlib

def validate(username, license_key):
    # Bundle the username and license key into an object
    data = {
        "username": username,
        "license_key": license_key
    }

    # Convert the object to a JSON string
    data_string = json.dumps(data)

    # Encrypt the JSON string using SHA-256
    hash_object = hashlib.sha256(data_string.encode())
    encrypted_data = hash_object.hexdigest()

    return encrypted_data
