# lgit
Quickly create repositories on your own git server
# Installation
## Linux
Follow these commands:
```
git clone https://github.com/esc-home-end-delete/lgit
cd lgit
pip install -r requirements.txt
echo alias lgit=python $(pwd)/lgit.py >> ~/.bashrc
```
Edit [config.py](config.py) with your preferences
## Windows
Clone the repository

Edit [config.py](config.py) with your preferences

Compile [lgit.py](lgit.py) and [config.py](config.py) to .exe with [pyinstaller](https://github.com/pyinstaller/pyinstaller)

Add compiled .exe file to the PATH
# Usage
`lgit [repository name]`
## For example
Input:
`lgit test`

Output:
`Your SSH link: ssh://git@192.168.1.196:22/home/git/test`
