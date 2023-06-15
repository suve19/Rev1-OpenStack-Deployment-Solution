#!/usr/bin/env python

import os

def upgrade_system():
    os.system("sudo apt-get update && sudo apt-get upgrade")

def install_dependencies():
    os.system("sudo apt-get install -y python3-pip")
    os.system("sudo pip3 install -r requirements.txt")

def write_script():
    with open("deploy.sh", "w") as f:
        f.write("#!/bin/bash\n")
        f.write("sudo apt-get update && sudo apt-get upgrade\n")
        f.write("sudo apt-get install -y python3-pip\n")
        f.write("sudo pip3 install -r requirements.txt\n")

if __name__ == '__main__':
    upgrade_system()
    install_dependencies()
    write_script()
    os.system("chmod +x deploy.sh")
    print("Installation complete. Run `./deploy.sh` to install dependencies.")