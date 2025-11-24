import requests

TOKEN = "c0b41dad848fe108b36f55a0649798f350251b9e448c364f8afca955041ad382"

s = requests.Session()

auth = s.post(
    "http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar",
    params={"token": TOKEN}
)

print("AUTH TEXT RAW:", repr(auth.text))
