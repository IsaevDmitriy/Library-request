import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""

        file_name = file_path.split("\\")[-1]
        response = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            params={
                "path": f'{file_name}'
            },
            headers={
            "Authorization": f"OAuth {self.token}"
            }
        )
        response.raise_for_status()
        href = response.json()["href"]
        with open(f'{file_path}', "rb") as f:
            upload_response = requests.put(href, files={"file": f})
            upload_response.raise_for_status()

        return print(f'Успешная загрузка')


if __name__ == '__main__':
    uploader = YaUploader("<Your Yandex Disk token>")
    result = uploader.upload("<Your path to the file>")





