from json import load

def load_settings():
    with open('settings.json','r') as file_obj:
        settings=json.load(file_obj)
        return settings
