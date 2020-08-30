from configparser import ConfigParser

config = ConfigParser()
config.read("config.cfg")

print(config.get('section1', 'username'))
print(config.get('section1', 'password'))
