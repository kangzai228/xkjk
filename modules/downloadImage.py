import re,requests,os

def savefile(fileName,content):
    file_path ='/'.join(fileName.split('/')[:-1])
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    with open(fileName,'wb') as f:
        f.write(content)

def downloadImage(param):
    reg='<img src=\\"(.*?)\\" />'
    # s='<img src=\"/images/28/119201_1.png\" />'
    res_list=re.findall(reg,param)
    for res in res_list:
        url='https://xkjk.jxeea.cn:8000'+res
        # print(url)
        headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Origin': 'https://xkjk.jxeea.cn:8000',
        'Referer': 'https://xkjk.jxeea.cn:8000/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }
        r=requests.get(url,headers=headers)
        if r.status_code==200:
            savefile('.'+res,r.content)
            print(url,'图片保存成功')
        else:
            print(url,'图片保存失败')


