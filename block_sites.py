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
    "www.instagram.com", "instagram.com"]
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

def block_sites():
    with open(hosts_path, 'a') as file:
        for site in blocked_websites:
            file.write(f"{redirect_ip} {site}\n")



def main():
    if not is_blocked():
        block_sites()

if __name__ == "__main__":
    main()
