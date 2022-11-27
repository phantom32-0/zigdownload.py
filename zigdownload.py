#!/usr/bin/env python3

import requests
import os

response = requests.get('https://ziglang.org/download/index.json')

if response.status_code != 200:
    print(f"Error {response.status_code} while trying to download Zig Downloads index.json")

data = response.json()

masterversion = data['master']['version']

downloadurl = data['master']['x86_64-linux']['tarball']

if input(f"Zig Master: {masterversion} Download? [y/n]> ").lower() != 'y':
    exit(0)

if os.system(f"wget {downloadurl} -O zigdownload.tar.xz") != 0:
    print(f"Error while trying to download {downloadurl}")
    exit(1)

if (os.path.exists('./zig')):
    if input(f"The directory 'zig' already exists. Overwrite? [y/n]> ").lower() != 'y':
        print("Error, 'zig' already exists.")
        exit(1)
    if os.system(f"rm -r ./zig/") != 0:
        print("Error while deleting 'zig' directory.")
        exit(1)

os.system(f"mkdir zig");

if os.system(f"tar xvf zigdownload.tar.xz -C ./zig") != 0:
    print(f"Error while trying to extract Zig")
    exit(1)
