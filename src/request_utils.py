import requests

def get_image_meta(dockerID, imgName):
    url = "https://hub.docker.com/v2/repositories/{owner}/{name}/".format(owner=dockerID, name=imgName)
    headers = {
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "hub.docker.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers).json()
    return response
