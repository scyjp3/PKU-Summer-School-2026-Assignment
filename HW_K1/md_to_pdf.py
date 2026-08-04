import os
import markdown
from playwright.sync_api import sync_playwright
from pygments.formatters import HtmlFormatter
from pygments import highlight
from pygments.lexers import PythonLexer
import re


def add_syntax_highlight(md_content):
    python_pattern = r'```python\s*\n(.*?)```'
    
    def replace_match(match):
        code = match.group(1)
        lexer = PythonLexer()
        formatter = HtmlFormatter(style='default', linenos=False)
        highlighted_code = highlight(code, lexer, formatter)
        return highlighted_code
    
    return re.sub(python_pattern, replace_match, md_content, flags=re.DOTALL)


def md_to_pdf(md_file_path=None, pdf_file_path=None, md_content=None):
    if md_file_path is not None and md_content is None:
        with open(md_file_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
    elif md_file_path is None and md_content is None:
        raise ValueError("Either md_file_path or md_content must be provided")
    
    if pdf_file_path is None and md_file_path is not None:
        pdf_file_path = md_file_path.replace('.md', '.pdf')
    
    md_content = add_syntax_highlight(md_content)
    
    html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
    
    pygments_css = HtmlFormatter(style='default').get_style_defs('.highlight')
    
    css_style = """
    @page {
        size: A4;
        margin: 1.2cm;
    }
    
    body {
        font-family: "Microsoft YaHei", "SimHei", "Noto Sans CJK SC", sans-serif;
        font-size: 11px;
        line-height: 1.3;
        color: #333;
        margin: 0;
        padding: 0;
    }
    
    h1 {
        font-size: 16px;
        font-weight: bold;
        text-align: center;
        color: #000;
        border-bottom: 2px solid #333;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    
    h2 {
        font-size: 12px;
        font-weight: bold;
        color: #1a1a1a;
        margin-top: 3px;
        margin-bottom: 1px;
        padding-left: 6px;
        border-left: 3px solid #4a90d9;
    }
    
    h2.page-break {
        page-break-before: always;
    }
    
    h3 {
        font-size: 11px;
        font-weight: bold;
        color: #2a2a2a;
        margin-top: 2px;
        margin-bottom: 1px;
    }
    
    h4 {
        font-size: 11px;
        font-weight: bold;
        color: #3a3a3a;
        margin-top: 1px;
        margin-bottom: 0;
    }
    
    p {
        margin: 1px 0;
        text-align: justify;
    }
    
    ul, ol {
        margin: 3px 0;
        padding-left: 18px;
    }
    
    li {
        margin: 1px 0;
    }
    
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 1px 0;
        font-size: 10px;
    }
    
    table th, table td {
        border: 0.5px solid #ccc;
        padding: 1px 3px;
        text-align: left;
        vertical-align: top;
    }
    
    table th {
        background-color: #f5f5f5;
        font-weight: bold;
    }
    
    code {
        font-family: "Consolas", "Monaco", "Courier New", monospace;
        font-size: 9px;
        background-color: #f4f4f4;
        padding: 0 2px;
        border-radius: 1px;
    }
    
    pre {
        background-color: #f8f8f8;
        border: 0.5px solid #ddd;
        border-radius: 2px;
        padding: 2px 4px;
        overflow-x: auto;
        margin: 1px 0;
    }
    
    pre code {
        background-color: transparent;
        padding: 0;
        font-size: 8px;
        line-height: 1.1;
        white-space: pre;
    }
    
    blockquote {
        border-left: 4px solid #4a90d9;
        padding-left: 10px;
        margin: 4px 0;
        color: #666;
        background-color: #f9f9f9;
        padding: 3px 10px;
    }
    
    strong {
        font-weight: bold;
        color: #000;
    }
    
    hr {
        border: none;
        border-top: 1px solid #ddd;
        margin: 8px 0;
    }
    
    a {
        color: #4a90d9;
        text-decoration: none;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    .highlight {
        background-color: #f8f8f8;
        border-radius: 2px;
        padding: 2px 4px;
        margin: 1px 0;
        overflow-x: auto;
    }
    
    .highlight pre {
        background-color: transparent;
        border: none;
        padding: 0;
        margin: 0;
        font-size: 8px;
        line-height: 1.1;
    }
    
    .highlight .kn { color: #008000; font-weight: bold; }
    .highlight .k { color: #008000; font-weight: bold; }
    .highlight .kp { color: #008000; }
    .highlight .kr { color: #008000; font-weight: bold; }
    .highlight .kt { color: #0000ff; }
    .highlight .na { color: #ff0000; }
    .highlight .nb { color: #008000; }
    .highlight .nc { color: #0000ff; font-weight: bold; }
    .highlight .no { color: #808080; }
    .highlight .nd { color: #808080; }
    .highlight .ni { color: #800080; }
    .highlight .ne { color: #0000ff; font-weight: bold; }
    .highlight .nf { color: #0000ff; }
    .highlight .py { color: #0000ff; }
    .highlight .nl { color: #0000ff; }
    .highlight .nn { color: #0000ff; }
    .highlight .nt { color: #008000; font-weight: bold; }
    .highlight .nv { color: #ff8000; }
    .highlight .vg { color: #ff8000; }
    .highlight .vi { color: #ff8000; }
    .highlight .vm { color: #ff8000; }
    .highlight .s { color: #ba2121; }
    .highlight .sa { color: #ba2121; }
    .highlight .sb { color: #ba2121; }
    .highlight .sc { color: #ba2121; }
    .highlight .dl { color: #ba2121; }
    .highlight .sd { color: #ba2121; }
    .highlight .s2 { color: #ba2121; }
    .highlight .se { color: #ba2121; }
    .highlight .sh { color: #ba2121; }
    .highlight .si { color: #ba2121; }
    .highlight .sx { color: #ba2121; }
    .highlight .sr { color: #ba2121; }
    .highlight .s1 { color: #ba2121; }
    .highlight .ss { color: #ba2121; }
    .highlight .m { color: #666666; }
    .highlight .mb { color: #666666; }
    .highlight .mf { color: #666666; }
    .highlight .mh { color: #666666; }
    .highlight .mi { color: #666666; }
    .highlight .il { color: #666666; }
    .highlight .mo { color: #666666; }
    .highlight .o { color: #666666; }
    .highlight .ow { color: #008000; font-weight: bold; }
    .highlight .c { color: #808080; font-style: italic; }
    .highlight .ch { color: #808080; font-style: italic; }
    .highlight .cm { color: #808080; font-style: italic; }
    .highlight .c1 { color: #808080; font-style: italic; }
    .highlight .cs { color: #808080; font-style: italic; }
    .highlight .cp { color: #808080; }
    .highlight .cpf { color: #808080; }
    """
    
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>【K1】数值和编码 - 作业答案</title>
        <style>
            {pygments_css}
            {css_style}
        </style>
    </head>
    <body>
        {html_content}
        <script>
            var headings = document.querySelectorAll('h2');
            for (var i = 1; i < headings.length; i++) {{
                headings[i].classList.add('page-break');
            }}
        </script>
    </body>
    </html>
    """
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        page.set_content(full_html, wait_until='networkidle')
        
        page.pdf(
            path=pdf_file_path,
            format='A4',
            margin={
                'top': '1.2cm',
                'right': '1.2cm',
                'bottom': '1.2cm',
                'left': '1.2cm'
            },
            print_background=True
        )
        
        browser.close()
    
    print(f"PDF文件已生成: {pdf_file_path}")
    print(f"文件大小: {os.path.getsize(pdf_file_path) / 1024:.2f} KB")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    md_files = [
        os.path.join(base_dir, "K1_题目1~4", "converter.md"),
        os.path.join(base_dir, "K1_题目5~8", "【K1】数值和编码_作业答案.md")
    ]
    
    combined_content = ""
    for md_file in md_files:
        if os.path.exists(md_file):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                combined_content += content + "\n"
        else:
            print(f"文件不存在: {md_file}")
    
    output_pdf = os.path.join(base_dir, "【K1】数值和编码_answers_final.pdf")
    md_to_pdf(None, output_pdf, combined_content)