import requests
from bs4 import BeautifulSoup
import os

num = '11920'
base = 'https://www.acmicpc.net/problem/'
url = base + num

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find("span", id="problem_title").get_text()
    sample_i = soup.select("pre[id^=sample-input]")

    os.system(f"mkdir \"[BOJ_{num}]{title}\"")
    os.system(f"echo import sys > \"[BOJ_{num}]{title}/BOJ_{num}.py\"")
    os.system(f"echo sys.stdin = open('input.txt') >> \"[BOJ_{num}]{title}/BOJ_{num}.py\"")
    
    for i in range(len(sample_i)):
        for text_i in sample_i[i].text.strip().split('\n'):
            os.system(f"echo {text_i} >> \"[BOJ_{num}]{title}/input{i+1}.txt\"")

else:
    print(response.status_code)