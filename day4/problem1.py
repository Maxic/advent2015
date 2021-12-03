import hashlib

def main():
    puzzle_input = "yzbqklnj"

    found = False
    counter = 0

    while not found:
        counter += 1

        attempt = puzzle_input + str(counter)
        hash_object = hashlib.md5(attempt.encode())
        md5_hash = hash_object.hexdigest()

        if md5_hash.startswith("00000"):
            found = True

    print(md5_hash)
    print(counter)


if __name__ == "__main__":
    main()

