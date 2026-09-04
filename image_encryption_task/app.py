from flask import Flask, render_template, request, send_file
from PIL import Image
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


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


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():

    image_file = request.files.get("image")
    key = request.form.get("key")
    action = request.form.get("action")

    if not image_file:
        return "No image selected", 400

    if not key:
        return "Please enter a key", 400

    try:
        key = int(key)
    except ValueError:
        return "Key must be a number", 400

    if key < 0 or key > 255:
        return "Key must be between 0 and 255", 400

    input_path = os.path.join(
        UPLOAD_FOLDER,
        "input.png"
    )

    if action == "encrypt":

        output_path = os.path.join(
            UPLOAD_FOLDER,
            "encrypted.png"
        )

    elif action == "decrypt":

        output_path = os.path.join(
            UPLOAD_FOLDER,
            "decrypted.png"
        )

    else:

        return "Invalid action", 400

    image_file.save(input_path)

    process_image(
        input_path,
        output_path,
        key
    )

    return send_file(
        output_path,
        mimetype="image/png"
    )


if __name__ == "__main__":
    app.run(debug=True)
