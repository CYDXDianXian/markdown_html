from time import sleep
import traceback
import markdown
from pathlib import Path
from markdown.extensions.abbr import AbbrExtension
from markdown.extensions.def_list import DefListExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.footnotes import FootnoteExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.admonition import AdmonitionExtension
from mdx_math import MathExtension

output_path = 'html输出'
input_path = 'markdown输入'
Path(input_path).mkdir(parents=True, exist_ok=True)
print('【markdown输入】文件夹已创建，请将markdowm文件放入该文件夹中')
Path(output_path).mkdir(parents=True, exist_ok=True)

# 创建markdown扩展列表
ext_list = [
    AbbrExtension(), 
    DefListExtension(), 
    FencedCodeExtension(), 
    FootnoteExtension(), 
    TableExtension(), 
    AdmonitionExtension(), 
    MathExtension()
    ]

c_num = 0
f_num = 0
for markdown_file in Path(input_path).iterdir():
    try:
        text = Path(markdown_file).read_text(encoding='utf-8') # 以字符串形式返回路径指向的文件的解码后文本内容。
        html = markdown.markdown(text, extensions=ext_list) # 转为html文本，extensions使用扩展列表
        # 保存为文件
        html_name = f"{markdown_file.name.split('.')[0]}.html" 
        # .name读取路径中的文件名。.split('.')[0]表示以.为分割生成一个列表并读取列中表第一个值
        Path(output_path, html_name).write_text(html, encoding='utf-8')
        c_num += 1
        print('ok:', html_name)
    except:
        f_num += 1
        traceback.print_exc()
        print('失败:', markdown_file.name)

print(f'全部完成，成功{c_num}个，失败{f_num}个')
print('程序将在10秒后结束')
sleep(10)