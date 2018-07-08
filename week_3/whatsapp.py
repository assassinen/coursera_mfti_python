import requests


from fake_useragent import UserAgent
import requests


# ua = UserAgent()
# print(ua.chrome)
# print(ua.msie)
# header = {'User-Agent':str(ua.msie)}
# print(header)
# url = "https://www.hybrid-analysis.com/recent-submissions?filter=file&sort=^timestamp"
# url = 'https://web.whatsapp.com'
# content  = requests.get(url, headers=header).content
# print(content)


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get('https://web.whatsapp.com', headers=headers)
content = response.content

# for i in content:
#     print(i)

with open('whatsapp.html', 'bw') as f:
    # out = json.dumps(data, indent=4)
    f.write(content)
