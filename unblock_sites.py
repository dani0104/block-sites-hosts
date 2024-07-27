import os
import getpass
import time
import sys

blocked_websites = [
    "www.linkedin.com", "linkedin.com",
    "www.facebook.com", "facebook.com",
    "www.twitter.com", "twitter.com",
    "www.youtube.com", "youtube.com",
    "www.reddit.com", "reddit.com",
    "www.instagram.com", "instagram.com"
]
redirect_ip = "127.0.0.1"
password = "D0nt_5urf_Th3_W3b"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

def is_blocked():
    with open(hosts_path, 'r') as file:
        content = file.read()
        for site in blocked_websites:
            if site in content:
                return True
    return False

def unblock_sites():
    with open(hosts_path, 'r') as file:
        lines = file.readlines()
    with open(hosts_path, 'w') as file:
        for line in lines:
            if not any(site in line for site in blocked_websites):
                file.write(line)



def main():
    if is_blocked():
        input_password = getpass.getpass("Enter password to access blocked site: ")
        if input_password == password:
            unblock_sites()

if __name__ == "__main__":
    main()
