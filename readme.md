# 2023年下半年江西省普通高中学业水平考试 模拟练习

https://xkjk.jxeea.cn:8000/

账号：考籍号
密码：123456

模拟考试时间为10月20日至11月7日

## 题型和分散

### 信息技术

1. 单选题 每题2分 20题
2. 多选题 每题3分 5题
3. 填空题 每题3分 5题
4. 综合题 每题10分 3题

### 通用技术

1. 单选题 每题3分 20题

2. 多选题 每题4分 3题

3. 填空题 每题4分 2题

4. 绘图题  每题6分 1题

5. 综合题  每题12分 1题

正则表达式在线测试

https://www.mklab.cn/utils/regex

```code
待匹配：
<img src=\"/images/28/119201_1.png\" />

需要的结果：
/images/28/119201_1.png

最终url:
https://xkjk.jxeea.cn:8000/images/28/119201_1.png
```

```python
import re

reg='<img src=\\"(.*?)\\" />'

s='<img src=\"/images/28/119201_1.png\" />'
res_list=re.findall(reg,s)
for res in res_list:
    url='https://xkjk.jxeea.cn:8000'+res
    print(url)
```