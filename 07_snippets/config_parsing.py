"""
Practice: Config Parsing (configparser)
"""
import configparser
import os

def config_demo():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'ServerAliveInterval': '45'}
    config['database'] = {'Host': 'localhost', 'Port': '5432', 'User': 'admin'}

    filename = 'config.ini'
    with open(filename, 'w') as f:
        config.write(f)
    print("config.ini written.")

    config_read = configparser.ConfigParser()
    config_read.read(filename)
    host = config_read['database']['Host']
    print(f"Read host: {host}")

    # Cleanup config file
    if os.path.exists(filename):
        os.remove(filename)

if __name__ == "__main__":
    config_demo()
