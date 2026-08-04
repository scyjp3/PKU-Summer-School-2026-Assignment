import asyncio
import markdown
import pygments
from pygments.formatters import HtmlFormatter
from playwright.async_api import async_playwright
import os

async def convert_md_to_pdf():
    input_file = "python_scripts.md"
    output_file = "python_scripts.pdf"
    
    with open(input_file, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    md_extensions = [
        'extra',
        'codehilite',
        'tables',
        'fenced_code',
    ]
    
    html_content = markdown.markdown(md_content, extensions=md_extensions)
    
    formatter = HtmlFormatter(style='default')
    css = formatter.get_style_defs('.codehilite')
    
    html_full = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap');
        
        body {{
            font-family: 'Noto Sans SC', 'SimSun', 'Microsoft YaHei', sans-serif;
            font-size: 12px;
            line-height: 1.6;
            color: #333;
            margin: 0;
            padding: 40px;
            background-color: #fff;
        }}
        
        h1 {{
            font-size: 24px;
            text-align: center;
            border-bottom: 2px solid #000;
            padding-bottom: 10px;
            margin-bottom: 25px;
            font-weight: 700;
        }}
        
        h2 {{
            font-size: 18px;
            color: #333;
            margin-top: 30px;
            margin-bottom: 15px;
            font-weight: 600;
        }}
        
        h3 {{
            font-size: 14px;
            color: #555;
            margin-top: 20px;
            margin-bottom: 10px;
            font-weight: 600;
        }}
        
        .codehilite {{
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 15px;
            margin: 12px 0;
            overflow-x: auto;
        }}
        
        .codehilite pre {{
            font-family: 'JetBrains Mono', 'Consolas', 'Monaco', monospace;
            font-size: 10px;
            line-height: 1.5;
            margin: 0;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
        
        {css}
        
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 12px 0;
            font-size: 11px;
        }}
        
        th, td {{
            border: 1px solid #ccc;
            padding: 8px 12px;
            text-align: left;
        }}
        
        th {{
            background-color: #f5f5f5;
            font-weight: 600;
        }}
        
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 15px auto;
        }}
        
        hr {{
            border: none;
            border-top: 1px dashed #ccc;
            margin: 25px 0;
        }}
        
        blockquote {{
            border-left: 4px solid #007bff;
            padding-left: 15px;
            margin: 12px 0;
            color: #666;
            font-style: italic;
        }}
        
        pre:not(.codehilite pre) {{
            background-color: #f5f5f5;
            padding: 10px 15px;
            border-radius: 4px;
            font-family: 'JetBrains Mono', 'Consolas', monospace;
            font-size: 10px;
            overflow-x: auto;
            margin: 12px 0;
        }}
        
        code {{
            font-family: 'JetBrains Mono', 'Consolas', monospace;
            font-size: 10px;
        }}
        </style>
    </head>
    <body>
    {html_content}
    </body>
    </html>
    """
    
    html_file = "temp_output.html"
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_full)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto(f"file:///{os.path.abspath(html_file)}")
        
        await page.pdf(
            path=output_file,
            format='A4',
            margin={
                'top': '20mm',
                'bottom': '20mm',
                'left': '20mm',
                'right': '20mm'
            },
            print_background=True
        )
        
        await browser.close()
    
    os.remove(html_file)
    print(f"PDF generated successfully: {output_file}")

if __name__ == "__main__":
    asyncio.run(convert_md_to_pdf())
