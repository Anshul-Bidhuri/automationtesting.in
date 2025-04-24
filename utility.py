import random
import json
import os


def generate_random_email_and_password():
    email = f"testuser{random.randint(0, 1000)}@example.com"
    password = f"Password@{random.randint(0, 1000)}"
    file_path = get_file_path("config.json")
    update_json_file(file_path, "new_user_email_address", email)
    update_json_file(file_path, "new_user_password", password)
    return email, password


def get_file_path(file_name):
    cur_path = os.path.abspath(os.path.dirname(__file__))
    for root, dirs, files in os.walk(cur_path):
        for name in files:
            if name == file_name:
                match = root
    file_path = os.path.join(match, file_name)
    return file_path


def update_json_file(file_path, key, new_value):
    with open(file_path, 'r') as file:
        data = json.load(file)
    if key in data:
        data[key] = new_value
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def read_json_file(file_name):
    file_path = get_file_path(file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data