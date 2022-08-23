import requests as re
import jsonmodule as jm
import logging

logging.basicConfig(filename='../info.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s [%(filename)s]: %(name)s %(funcName)20s - Message: %(message)s')

url = jm.get_secret("url")
headers = jm.get_secret("headers")


def createFlexContainer(body, path = ""):
    logging.info("post method for createFlexContainer")
    res = re.post(url + path, headers=headers, json=body)
    return res.text


def updateFlexContainer(body, path = ""):
    logging.info("put method for updateFlexContainer")
    res = re.put(url + path, headers=headers, json=body)
    return res.text


def retrieveFlexContainer(path = ""):
    logging.info("put method for updateFlexContainer")
    res = re.get(url + path, headers=headers, params={"rcn":4})
    return res.text


def deleteFlexContainer(path = ""):
    logging.info("delete method for deleteFlexContainer")
    res = re.delete(url + path, headers=headers)
    return res.text
