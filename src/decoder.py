
import base64
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from.banner import banner


def decrypt_file(filepath, debug=False):

    banner()
    print(f"Decoding save data: {filepath.split("/")[-1]}")

    with open(filepath, "rb") as file:
        raw_save = file.read()

    # skip header and last byte

    trimmed_file = raw_save[25:-1]

    # convert to base64 str

    b64_str = trimmed_file.decode("latin-1")

    # decode base64

    file_bytes = base64.b64decode(b64_str)

    # AES decryption

    decrypt_key = b"UKu52ePUBwetZ9wNX88o54dnfKRu0T1l"

    cipher = AES.new(decrypt_key, AES.MODE_ECB)

    decrypted = cipher.decrypt(file_bytes)

    decrypted = unpad(decrypted, AES.block_size)

    # decode readable json str

    json_str = decrypted.decode("utf=8")

    # save file
    
    json_str = json.loads(json_str)

    banner()
    print(f"Save data successfully decoded.")

    if debug:
        with open("decrypted.json", "w+") as save_file:
            json.dump(json_str, save_file, indent=2)

    return json_str

        


