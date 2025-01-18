def get_subtitle_text(subtitleUrl):
    # access the API
    url = "https://youtube-media-downloader.p.rapidapi.com/v1/subtitles"
    headers = {
        'x-rapidapi-host': "youtube-media-downloader.p.rapidapi.com",
        'x-rapidapi-key': "YOUR API KEY"
    }
    # send a get subtitle text request to the API 
    querystring = {"subtitleUrl": subtitleUrl}
    response = requests.request("GET", url, headers=headers, params=querystring)
    # return the text response
    return response.text