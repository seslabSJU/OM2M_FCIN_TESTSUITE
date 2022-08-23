import os
import json
import logging

logging.basicConfig(filename='../info.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s [%(filename)s]: %(name)s %(funcName)20s - Message: %(message)s')

secret_file = os.path.join("../", 'settings.json')
with open(secret_file, 'r', encoding="UTF-8") as f:
    secrets = json.loads(f.read())
 
def get_secret(setting):
        try:
            return secrets[setting]
        except KeyError:
            error_msg = "Set the {} environment variable".format(setting)
            logging.info(error_msg)
            return error_msg

if __name__ == "__main__":
    print(get_secret("Test"))