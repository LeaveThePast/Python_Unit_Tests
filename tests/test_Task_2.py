from Task_2 import YaManager

def test_responce():
    token = ''
    folder_creator = YaManager(token)
    folder_path = 'API_Test'
    response = folder_creator.create_folder(folder_path)
    try:
        assert response.status_code == 201, 'Folder was not created'
    except AssertionError:
        print(f"Folder was not created, status code: {response.status_code}; response text: {response.text}")
        raise