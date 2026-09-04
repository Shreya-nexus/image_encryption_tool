from PIL import Image
import os


def process_image(input_path, output_path, key):

    image = Image.open(input_path).convert("RGB")
    pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):

            r, g, b = pixels[x, y]

            r = r ^ key
            g = g ^ key
            b = b ^ key

            pixels[x, y] = (r, g, b)

    image.save(output_path)


def main():

    print("==============================")
    print("     IMAGE ENCRYPTION TOOL")
    print("==============================")

    print("\n1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("\nEnter your choice (1/2): ")

    input_path = input("Enter image path: ")

    # Check whether image exists
    if not os.path.exists(input_path):
        print("Error: Image not found!")
        return

    # Get encryption key
    try:
        key = int(input("Enter encryption key (0-255): "))
    except ValueError:
        print("Error: Key must be a number.")
        return

    # Check key range
    if key < 0 or key > 255:
        print("Error: Key must be between 0 and 255.")
        return

    output_path = input("Enter output image name: ")

    if choice == "1":

        process_image(input_path, output_path, key)

        print("\nImage encrypted successfully!")
        print("Saved as:", output_path)

    elif choice == "2":

        process_image(input_path, output_path, key)

        print("\nImage decrypted successfully!")
        print("Saved as:", output_path)

    else:

        print("Invalid choice!")


if __name__ == "__main__":
    main()