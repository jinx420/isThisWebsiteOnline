import httpx
import sys


def isWebsiteOnline(url):
    try:
        httpx.get(f'https://{url}')
        print(f'{url} is using HTTPS')
        return True
    except:
        try:
            httpx.get(f'http://{url}')
            print(f'{url} is using HTTP')
            return True
        except:
            return False


# main
if __name__ == "__main__":
    # cli
    if isWebsiteOnline(sys.argv[1]):
        print("Website is online")
    else:
        print("Website is offline")

    sys.exit(0)
