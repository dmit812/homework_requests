import requests


class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_upload_link(self, file_path):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def get_upload_file(self, file_path, file_name):
        href = self.get_upload_link(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Файл успешно загружен.')
