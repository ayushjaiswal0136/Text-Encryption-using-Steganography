from flask import Flask, render_template, request, send_file, jsonify
from PIL import Image
import io

app = Flask(__name__)

EOF_MARKER = '1111111111111110'  # 16-bit EOF marker

def encode_text_into_image(image, text):
    encoded = image.copy()
    width, height = encoded.size
    index = 0
    binary_text = ''.join(format(ord(c), '08b') for c in text) + EOF_MARKER

    for y in range(height):
        for x in range(width):
            if index < len(binary_text):
                r, g, b = encoded.getpixel((x, y))
                r = (r & ~1) | int(binary_text[index])
                encoded.putpixel((x, y), (r, g, b))
                index += 1
    return encoded

def decode_text_from_image(image):
    binary_data = ''
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            binary_data += str(r & 1)

    eof_index = binary_data.find(EOF_MARKER)
    if eof_index == -1:
        # EOF marker not found, image likely not encoded
        return None

    # Extract bits up to EOF marker
    encoded_bits = binary_data[:eof_index]

    if len(encoded_bits) % 8 != 0:
        # Bits length not multiple of 8, invalid data
        return None

    chars = [encoded_bits[i:i+8] for i in range(0, len(encoded_bits), 8)]

    try:
        decoded_text = ''.join(chr(int(byte, 2)) for byte in chars)
    except Exception:
        # Any error converting binary to chars means invalid image
        return None

    return decoded_text.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    image = request.files['image']
    text = request.form['text']
    img = Image.open(image)
    encoded_img = encode_text_into_image(img, text)

    img_io = io.BytesIO()
    encoded_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png', download_name='encoded_image.png')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    image = request.files['image']
    try:
        img = Image.open(image)
        text = decode_text_from_image(img)
        if text is None or text == '':
            return jsonify({"error": "Invalid Image"}), 200
        return jsonify({"decoded_text": text})
    except Exception:
        return jsonify({"error": "Invalid Image"}), 400

if __name__ == '__main__':
    app.run(debug=True)
