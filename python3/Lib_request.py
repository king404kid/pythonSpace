import requests

respone = requests.get("http://tieba.baidu.com/p/2460150866");
print(respone.content);