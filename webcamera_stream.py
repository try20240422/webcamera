import streamlit as st
import requests
import time

st.title('リモートカメラ制御')

esp_ip = "42.151.114.219"  # ESP32の外部IPアドレス
port = "82"  # ESP32で設定されたポート番号

def set_servo(angle):
    url = f"http://{esp_ip}:{port}/servo?pos={angle}"
    response = requests.get(url)
    if response.status_code == 200:
        st.success(f'カメラを {angle} 度に動かしました。')
    else:
        st.error('Failed to move the camera')

def get_camera_image():
    # タイムスタンプを現在時刻に設定してURLに追加する
    timestamp = int(time.time())
    return f"http://{esp_ip}:{port}/capture?timestamp={timestamp}"

angle = st.slider('カメラの角度', 0, 180, 90)
if st.button('角度を設定'):
    set_servo(angle)

st.image(get_camera_image(), caption="Live Camera Feed")
