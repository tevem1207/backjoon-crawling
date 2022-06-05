import requests
from bs4 import BeautifulSoup
import os
base = 'https://www.acmicpc.net/problem/'

while True:
    print('문제 번호를 입력하세요. 중단하려면 n을 입력하세요.')
    num = input()
    if num == 'n' or num == 'N':
        break
    url = base + num
    print(url)

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        title = soup.find("span", id="problem_title").get_text()
        sample_i = soup.select("pre[id^=sample-input]")

        os.system(f"mkdir \"[BOJ_{num}]{title}\"")
        os.system(f"echo import sys > \"[BOJ_{num}]{title}/BOJ_{num}.py\"")

        for i in range(len(sample_i)):
            for text_i in sample_i[i].text.strip().split('\n'):
                os.system(f"echo {text_i} >> \"[BOJ_{num}]{title}/input{i+1}.txt\"")

        with open(f'[BOJ_{num}]{title}/BOJ_{num}.py', 'a') as file_data:
            file_data.write(f"for i in range({len(sample_i)}):\n")
            file_data.write("    sys.stdin = open(f'input{i}.txt')")

    else:
        print(response.status_code)
        break
