import requests

def get_video_detail(videoID):
    # access the API
    url = "https://youtube-media-downloader.p.rapidapi.com/v1/details"
    headers = {
        'x-rapidapi-host': "youtube-media-downloader.p.rapidapi.com",
        'x-rapidapi-key': "YOUR API KEY"
    }
    # send a get request to the API 
    querystring = {"videoId": videoID}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # conver the response to json format
    json_response = response.json()
    # obtain the subtitle url (in XML format)
    subtitleURL = json_response['subtitles']['items'][0]['url']

    return subtitleURL