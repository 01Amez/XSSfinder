import requests
import subprocess as s

site = input("target.com: ")
payload = input("payload: ")

def geturls():
    cmd = f"waybackurls {site} > urls.txt"
    s.run(cmd, shell=True)

geturls()

def xssurls():
    with open("urls.txt", "r") as urls, open("urls1.txt", "w") as urls1:
        for x in urls:
            if "=" in x:
                urls1.write(x)

xssurls()

def xss():
    with open("urls1.txt", "r") as urls1, open("urls2.txt", "a") as sa:
        for xx in urls1:
            links = xx.replace("=", f'=">{payload}')
            sa.write(links)

xss()

def xssfinder():
    with open("urls2.txt", "r") as urls2:
        for xx in urls2:
            links = xx.strip("\n")
            a = requests.get(links)
            if payload in a.text:
                print("xss haya:" + links)
                with open("find_xss.txt", "a") as find_xss:
                    find_xss.write(links + "\n")
            else:
                print("xss nia:" + links)

xssfinder()