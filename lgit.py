import paramiko

from sys import argv
import os.path

import config

if len(argv) >= 2:
    with paramiko.SSHClient() as client:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(config.hostname, config.port, config.username, config.password)

        mkdir_stdin, mkdir_stdout, mkdir_stderr = client.exec_command(f'mkdir {argv[1]}')
        if mkdir_stderr.read():
            print('Error creating a directory')
        else:
            git_stdin, git_stdout, git_stderr = client.exec_command(f'git init --bare {argv[1]}')
            if git_stderr.read():
                print('Error initialisation a git repository')
            else:
                pwd_stdin, pwd_stdout, pwd_stderr = client.exec_command(f'pwd')
                print(f'Your SSH link: ssh://{config.username}@{config.hostname}:{config.port}'
                      f'{os.path.join(pwd_stdout.read().decode().strip(), argv[1])}')
else:
    print('Check arguments')
