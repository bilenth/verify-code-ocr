from tkinter import image_names
from flask import Flask, request, jsonify
import base64
from io import BytesIO
from PIL import Image
import ddddocr

app = Flask(__name__)
ocr = ddddocr.DdddOcr()

@app.route('/api/recognize', methods=['POST'])
def recognize():
    try:
        data = request.json
        if 'image' not in data:
            return jsonify({'error': 'No image provided'}), 400
        
        image_data = str(data['image']).replace('data:image;base64,','')
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))
        # image = open("68747470733a2f2f63646e2e77656e616e7a68652e636f6d2f696d672f32303231303731353231313733333835352e706e67.webp", "rb").read()
        
        # Perform OCR
        result = ocr.classification(image)
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5083)
