import requests as re
import jsonmodule as jm
import onem2m
import logging

logging.basicConfig(filename='../info.log', filemode='w', level=logging.INFO, format='%(asctime)s - %(levelname)s [%(filename)s]: %(name)s %(funcName)20s - Message: %(message)s')

def settingFlexContainer():
    body = onem2m.createFlexContainer(jm.get_secret("body")["CREATE"]["devLt"], "")
    logging.info(body)
    body = onem2m.createFlexContainer(jm.get_secret("body")["CREATE"]["binSh"], "/Light")
    logging.info(body)
    body = onem2m.createFlexContainer(jm.get_secret("body")["CREATE"]["color"], "/Light")
    logging.info(body)
    
def resetFlexContainer():
    body = onem2m.deleteFlexContainer("/Light/Color")
    logging.info(body)
    body = onem2m.deleteFlexContainer("/Light/Switch")
    logging.info(body)
    body = onem2m.deleteFlexContainer("/Light")
    logging.info(body)
    
if __name__ == "__main__":
    resetFlexContainer()
