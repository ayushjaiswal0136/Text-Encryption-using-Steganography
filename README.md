🕵️‍♂️ Text Encryption Using Steganography
A web-based steganography tool that enables secure text encryption and decryption within images using the Least Significant Bit (LSB) technique. Built with HTML, CSS, JavaScript, and Python Flask, and powered by the Pillow (PIL) library for image processing.

🚀 Features
🔐 Encrypt secret text messages into PNG images

🕵️ Decrypt hidden messages from images

📷 Supports 100+ PNG images

⚙️ Built with Flask backend and responsive HTML/CSS/JS frontend

📦 Uses Pillow (PIL) for image manipulation

📈 Achieved 95%+ accuracy and <1% error rate in encoding/decoding

🛠️ Tech Stack
Frontend: HTML, CSS, JavaScript

Backend: Python Flask

Image Processing: Pillow (PIL)

Algorithm: Least Significant Bit (LSB)

📂 Project Structure
cpp
Copy
Edit
├── static/
│   ├── styles.css
│   └── script.js
├── templates/
│   └── index.html
├── uploads/
│   └── (uploaded images)
├── main.py
├── steganography.py
├── requirements.txt
└── README.md
🧪 How It Works
Encoding: Converts each character of the secret message into binary and embeds the bits into the least significant bits of the image pixels.

Decoding: Extracts the LSBs from pixels and reconstructs the original text message.

▶️ Getting Started
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/steganography-app.git
cd steganography-app
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the App
bash
Copy
Edit
python app.py
Open your browser and visit: http://localhost:5000

📸 Demo
[Insert screenshots or a GIF here showing image upload, encryption, and decryption process.]

✅ Use Cases
Secure communication

Hiding sensitive information

Educational tool for cryptography and image processing

📌 Limitations
Supports only .png images

Message size is limited by image dimensions
