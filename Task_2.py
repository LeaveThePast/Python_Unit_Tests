import requests


class YaManager:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, folder_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': folder_path}
        result = requests.put(url, headers=headers, params=params)
        return result


if __name__ == '__main__':
    token = ''
    folder_creator = YaManager(token)
    folder_path = 'API_Test'
    folder_creator.create_folder(folder_path)

