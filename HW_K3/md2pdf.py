import markdown
import os

md_file = r"c:\Users\panji\Desktop\暑假\北大暑校\HW\HW_K3\【K3】数据类型思考题.md"
html_file = r"c:\Users\panji\Desktop\暑假\北大暑校\HW\HW_K3\【K3】数据类型思考题.html"

with open(md_file, 'r', encoding='utf-8') as f:
    md_content = f.read()

html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

html_with_style = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body {{ font-family: "Microsoft YaHei", "微软雅黑", Arial, sans-serif; line-height: 1.8; max-width: 800px; margin: 0 auto; padding: 20px; }}
h1, h2, h3 {{ color: #2c3e50; }}
h1 {{ border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
code {{ background: #f4f4f4; padding: 2px 5px; border-radius: 3px; font-family: Consolas, monospace; }}
pre {{ background: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }}
pre code {{ background: none; padding: 0; }}
table {{ border-collapse: collapse; width: 100%; margin: 15px 0; }}
th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
th {{ background-color: #3498db; color: white; }}
tr:nth-child(even) {{ background-color: #f2f2f2; }}
blockquote {{ border-left: 4px solid #3498db; margin: 15px 0; padding: 10px 20px; background: #f9f9f9; }}
</style>
</head>
<body>
{html_content}
</body>
</html>
"""

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_with_style)

print(f"HTML已生成：{html_file}")
print("请用浏览器打开HTML文件，然后 Ctrl+P 打印为PDF")
