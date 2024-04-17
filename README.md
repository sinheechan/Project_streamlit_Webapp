# Porject_streamlit_Webapp

- Streamlit을 통한 다양한 웹 서비스 구축

<br /><br /> 

<img src="image/mnist_result.png">
<br /><br />
<img src="image/bcoin_result.png">
<br /><br /> 

## Object

Streamlit은 파이썬 스크립트로 데이터를 시각화하고 웹 애플리케이션을 생성할 수 있다.

본 프로젝트에서는 해당 도구를 활용하여 웹 서비스 구축 모델 생성을 목표로 한다.

1. Mnist 손글씨 분류 및 시각화 웹 애플리케이션
2. 비트코인의 가격 및 거래량 시각화 웹 애플리케이션

<br /><br /> 
## Dataset
- [Kaggle] Mnist 손글씨 데이터셋
- [coinmarketcap] 비트코인_암호화폐 주식 데이터 

<br /><br /> 
## File explanation
- server.py : Flask 웹 서버를 사용하여 API를 제공
- mnist.py : 사용자가 숫자를 그리고 해당 숫자를 인식하는 기능 구현
- crypto_price_history_app.py : 비트코인의 가격과 거래량을 시각화하는 간단한 웹 애플리케이션

<br /><br /> 
## Version

본 테스트의 간편성을 위해 위 client 작업들의 가상환경을 통일하였습니다.

**[mnist.py]**
- python 3.6
- pandas_datareader
- streamlit 1.10.0
- streamlit-drawable-canvas 0.5.1
- opencv-python 4.5.3.56
- tensorflow 2.4.0
- cryptocmd 0.6.0

**[server.py]**
- Python 3.11.0
- Flask 2.3.0

<br /><br /> 
## Result

