# ===========================
# Created by Pepper Scott
# 21/01/2026
# ===========================

from pylibdmtx.pylibdmtx import encode
from PIL import Image
import sys
import os

OUT_PATH = "output"

EXTENSION = ".png"

os.makedirs(OUT_PATH, exist_ok=True)

data = []

def main():
    if (len(sys.argv) == 1): #no arguments given
        while True:
            userinput = input("Enter data to encode to ECC200: ")
            encoded = encode(userinput.encode('utf8'))
            image = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
            path = os.path.join(OUT_PATH, userinput + EXTENSION)
            try:
                image.save(path)
            except:
                print("Laziest error handling possible; a try statement. Something failed")

    else: #at least 1 arg given
        failed = []
        for arg in sys.argv[1:]:
            encoded = encode(arg.encode('utf8'))
            image = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
            path = os.path.join(OUT_PATH, arg + EXTENSION)
            try:
                image.save(path)
            except:
                failed.append(arg)
        if (len(failed) != 0):
            print(f"Failed to save:",end="")
            print(*failed, sep="\n\t")

if __name__ == "__main__":
    main()