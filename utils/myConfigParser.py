import configparser
from pathlib import Path

cfgfile = 'petqa.ini'
cfgfileDir = 'config'

config = configparser.ConfigParser()
BASE_DIR =Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(cfgfileDir).joinpath(cfgfile)
config.read(CONFIG_FILE)


def getPetAPIURL():
    return (config['pet']['url'])

def getStoreAPIURL():
    return (config['store']['url'])

print(getPetAPIURL())