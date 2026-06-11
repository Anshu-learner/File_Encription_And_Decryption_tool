import os
import base64
import hashlib
import datetime

LOG_FILE = "logs.txt"

# ==========================
# LOGGING
# ==========================

def write_log(action):
    with open(LOG_FILE, "a") as file:
        timestamp = datetime.datetime.now()
        file.write(f"{timestamp} : {action}\n")

# ==========================
# KEY GENERATION
# ==========================

def generate_key(password):
    return hashlib.sha256(password.encode()).digest()

# ==========================
# XOR ENCRYPTION
# ==========================

def xor_data(data, key):
    result = bytearray()

    for i in range(len(data)):
        result.append(
            data[i] ^ key[i % len(key)]
        )

    return bytes(result)

# ==========================
# TEXT ENCRYPTION
# ==========================

def encrypt_text():

    text = input("Enter text: ")

    password = input(
        "Enter password: "
    )

    key = generate_key(password)

    encrypted = xor_data(
        text.encode(),
        key
    )

    encoded = base64.b64encode(
        encrypted
    ).decode()

    print("\nEncrypted Text:\n")
    print(encoded)

    write_log("Text Encrypted")

# ==========================
# TEXT DECRYPTION
# ==========================

def decrypt_text():

    encrypted = input(
        "Paste encrypted text:\n"
    )

    password = input(
        "Enter password: "
    )

    try:

        key = generate_key(
            password
        )

        decoded = (
            base64.b64decode(
                encrypted
            )
        )

        decrypted = xor_data(
            decoded,
            key
        )

        print(
            "\nDecrypted Text:\n"
        )

        print(
            decrypted.decode()
        )

        write_log(
            "Text Decrypted"
        )

    except Exception:

        print(
            "Decryption Failed"
        )

# ==========================
# FILE ENCRYPTION
# ==========================

def encrypt_file():

    filename = input(
        "Enter file name: "
    )

    if not os.path.exists(
        filename
    ):

        print(
            "File not found"
        )

        return

    password = input(
        "Enter password: "
    )

    key = generate_key(
        password
    )

    with open(
        filename,
        "rb"
    ) as file:

        data = file.read()

    encrypted = xor_data(
        data,
        key
    )

    output = (
        filename + ".enc"
    )

    with open(
        output,
        "wb"
    ) as file:

        file.write(
            encrypted
        )

    print(
        "File encrypted"
    )

    print(
        "Output:",
        output
    )

    write_log(
        f"Encrypted {filename}"
    )

# ==========================
# FILE DECRYPTION
# ==========================

def decrypt_file():

    filename = input(
        "Enter encrypted file: "
    )

    if not os.path.exists(
        filename
    ):

        print(
            "File not found"
        )

        return

    password = input(
        "Enter password: "
    )

    key = generate_key(
        password
    )

    with open(
        filename,
        "rb"
    ) as file:

        data = file.read()

    decrypted = xor_data(
        data,
        key
    )

    output = (
        filename.replace(
            ".enc",
            ""
        )
    )

    with open(
        output,
        "wb"
    ) as file:

        file.write(
            decrypted
        )

    print(
        "File decrypted"
    )

    print(
        "Output:",
        output
    )

    write_log(
        f"Decrypted {filename}"
    )

# ==========================
# VIEW LOGS
# ==========================

def view_logs():

    if not os.path.exists(
        LOG_FILE
    ):

        print(
            "No logs found"
        )

        return

    print(
        "\n===== LOGS =====\n"
    )

    with open(
        LOG_FILE,
        "r"
    ) as file:

        print(
            file.read()
        )

# ==========================
# FILE INFORMATION
# ==========================

def file_info():

    filename = input(
        "Enter file name: "
    )

    if not os.path.exists(
        filename
    ):

        print(
            "File not found"
        )

        return

    size = os.path.getsize(
        filename
    )

    print(
        "\nFile Name:",
        filename
    )

    print(
        "Size:",
        size,
        "Bytes"
    )

# ==========================
# DELETE LOGS
# ==========================

def clear_logs():

    with open(
        LOG_FILE,
        "w"
    ) as file:
        pass

    print(
        "Logs Cleared"
    )

# ==========================
# PASSWORD CHECK
# ==========================

def password_strength():

    password = input(
        "Enter password: "
    )

    score = 0

    if len(password) >= 8:
        score += 1

    if any(
        c.isupper()
        for c in password
    ):
        score += 1

    if any(
        c.isdigit()
        for c in password
    ):
        score += 1

    if any(
        not c.isalnum()
        for c in password
    ):
        score += 1

    print("\nStrength:")

    if score == 4:
        print("Strong")

    elif score >= 2:
        print("Medium")

    else:
        print("Weak")

# ==========================
# ABOUT
# ==========================

def about():

    print("\n")
    print("=" * 50)

    print(
        "FILE ENCRYPTION "
        "& DECRYPTION TOOL"
    )

    print(
        "Cyber Security Project"
    )

    print(
        "Python Based Security Tool"
    )

    print("=" * 50)

# ==========================
# MENU
# ==========================

def menu():

    while True:

        print("\n")
        print("=" * 50)

        print(
            "FILE ENCRYPTION TOOL"
        )

        print("=" * 50)

        print(
            "1. Encrypt Text"
        )

        print(
            "2. Decrypt Text"
        )

        print(
            "3. Encrypt File"
        )

        print(
            "4. Decrypt File"
        )

        print(
            "5. View Logs"
        )

        print(
            "6. Clear Logs"
        )

        print(
            "7. File Info"
        )

        print(
            "8. Password Check"
        )

        print(
            "9. About"
        )

        print(
            "10. Exit"
        )

        choice = input(
            "\nEnter Choice: "
        )

        if choice == "1":
            encrypt_text()

        elif choice == "2":
            decrypt_text()

        elif choice == "3":
            encrypt_file()

        elif choice == "4":
            decrypt_file()

        elif choice == "5":
            view_logs()

        elif choice == "6":
            clear_logs()

        elif choice == "7":
            file_info()

        elif choice == "8":
            password_strength()

        elif choice == "9":
            about()

        elif choice == "10":

            print(
                "Exiting..."
            )

            break

        else:

            print(
                "Invalid Choice"
            )

# ==========================
# MAIN
# ==========================

if __name__ == "__main__":

    about()

    menu()