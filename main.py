import requests

session = requests.Session()


def login():
    url = "http://140.127.113.89:3009/v1/login"
    account = input("請輸入帳號：")
    password = input("請輸入密碼：")
    data = {
        "account": account,
            "password": password
            }
    loginResponse = session.post(url=url,data=data)
    uuid = loginResponse.json()['uuid']
    token = loginResponse.json()['token']
    res = session.get(url=f"http://140.127.113.89:3009/v1/member/fillter/{uuid}",headers={'Authorization':token})
    name = res.json()['name']
    enterCode = res.json()['enterCode']
    print(f"{name} 你好，你的通行碼是 {enterCode}")


if __name__ == '__main__':
    login()

