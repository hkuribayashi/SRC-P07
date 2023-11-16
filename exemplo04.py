import hashlib

def get_hash(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


if __name__ == '__main__':
    with open('list.txt') as f:
        lines = f.read().splitlines()

    for senha in lines:
        hash = get_hash(senha)
        print("A senha {} possui o hash {}".format(senha, hash))


