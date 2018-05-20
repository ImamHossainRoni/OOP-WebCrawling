import requests
url = "https://dimikcomputing.com/"
response =requests.get(url)
with open("dimik.index.html","w") as f:
    f.write(response.text)