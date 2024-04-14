import io
import cv2
from tensorflow.keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import sys, time, os, base64, json, requests
from PIL import Image # Image 함수를 통한 이미지 크기 출력하는 라이브러리
from torchvision import transforms

@st.cache(allow_output_mutation=True)
def load():
    return load_model('model.h5') # 텐서플로우의 모델
model = load()

st.write('# MNIST Recognizer')

CANVAS_SIZE = 192

col1, col2 = st.beta_columns(2)

with col1:
    canvas = st_canvas(
        fill_color='#000000',
        stroke_width=20,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode='freedraw',
        key='canvas'
    )

if canvas.image_data is not None:
    img = canvas.image_data.astype(np.uint8)
    img = cv2.resize(img, dsize=(28, 28))

    preview_img = cv2.resize(img, dsize=(CANVAS_SIZE, CANVAS_SIZE), interpolation=cv2.INTER_NEAREST)

    col2.image(preview_img)

    x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    x = x.reshape((-1, 28, 28, 1))
    y = model.predict(x).squeeze()

    st.write('## Result: %d' % np.argmax(y))
    st.bar_chart(y)

    cv2.imwrite('test.jpeg', preview_img)
    print("저장 완료")
    image = Image.open('./test.jpeg')

    def image_to_tensor(image):
        gray_image = transforms.functional.to_grayscale(image)
        resized_image = transforms.functional.resize(gray_image, (28, 28))
        input_image_tensor = transforms.functional.to_tensor(resized_image)
        input_image_tensor_norm = transforms.functional.normalize(input_image_tensor, (0.1302,), (0.3069,))
        return input_image_tensor_norm

    image_tensor = image_to_tensor(image)

    dimensions = io.StringIO(json.dumps({'dims': list(image_tensor.shape)}))
    data = io.BytesIO(bytearray(image_tensor.numpy()))

    r = requests.post('http://localhost:5001/test',
                      files={'metadata': dimensions, 'data' : data})
    print("송신 완료")
    response = json.loads(r.content)

    print("Predicted digit :", response)