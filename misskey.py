import requests
import os
import urllib.request, json

def download_favorite_images(instance_url, user_token, download_path):
    id = get_my_id(instance_url, user_token)
    
    images = get_my_reaction_image(instance_url, id)
    for img in images:
        for file in img['note']['files']:
            print(file['url'])
    
def get_my_reaction_image(instance_url, id):
    # Misskey APIエンドポイント
    endpoint = f"{instance_url}/api/users/reactions"
    headers = {"Content-Type" : "application/json"}
    params = json.dumps({"i": access_token, "userId" : id}).encode("utf-8")

    # 自分のID取得
    response = requests.post(endpoint, data=params, headers=headers)
    response.raise_for_status()
    return response.json()
    
    None
    
def get_my_id(instance_url, user_token):
    # Misskey APIエンドポイント
    endpoint = f"{instance_url}/api/i"
    headers = {"Content-Type" : "application/json"}
    params = json.dumps({"i": user_token}).encode("utf-8")

    # 自分のID取得
    response = requests.post(endpoint, data=params, headers=headers)
    response.raise_for_status()
    res_json = response.json()
    return res_json.get("id")


def download_url(url, download_path, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(os.path.join(download_path, filename), "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

if __name__ == "__main__":
    # MisskeyインスタンスのURLとユーザートークンを指定
    instance_url = "https://submarin.online"
    # 設定 > API > アクセストークンの発行
    access_token = ""

    # ダウンロード先のフォルダーを指定
    download_path = "./favorite_images"

    # ダウンロード実行
    download_favorite_images(instance_url, access_token, download_path)