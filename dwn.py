import os, subprocess

def dwn_from_url(url):    
    # subprocess.Popen('youtube-dl -x {0}'.format(url), shell=False)
    try:
        subprocess.check_call('youtube-dl -x {0}'.format(url), shell=False)
    except subprocess.CalledProcessError as e:
        print("Error: ", e)


with open('urls.txt', 'r') as f:
    i = 1
    print("*" * 71)
    for link in f.readlines():
        url = link.strip()
        print("strip", url)
        print("Current Index", i)
        i = i + 1
        dwn_from_url(url)
        print("*" * 71)
        print("*" * 71)


print("DONE")