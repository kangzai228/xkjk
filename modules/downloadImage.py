import re

def downloadImage(param):
    reg='<img src=\\"(.*?)\\" />'
    # s='<img src=\"/images/28/119201_1.png\" />'
    res_list=re.findall(reg,param)
    for res in res_list:
        url='https://xkjk.jxeea.cn:8000'+res
        print(url)