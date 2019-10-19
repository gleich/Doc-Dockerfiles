import requests

def get_image_meta(dockerID, imgName):
    """Do a get request to get the meta data files for the image on docker hub
    
    Arguments:
        dockerID {string} -- docker id, name of the owner
        imgName {string} -- name of the image
    
    Returns:
        json -- response to GET request
    """
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
