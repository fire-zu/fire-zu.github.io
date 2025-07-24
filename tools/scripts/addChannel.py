import os

# 定义模板 HTML
html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="baidu-site-verification" content="codeva-GcOPVmWcrg" />

    <title>FIRE族</title>
    
    <!-- Favicon -->
    <link rel="icon" href="/assets/images/favicon.ico" type="image/x-icon">
    <link rel="icon" href="/assets/images/favicon-16x16.png" sizes="16x16" type="image/png">
    <link rel="icon" href="/assets/images/favicon-32x32.png" sizes="32x32" type="image/png">
    <link rel="apple-touch-icon" href="/assets/images/apple-touch-icon.png">
    <link rel="icon" href="/assets/images/android-chrome-192x192.png" sizes="192x192" type="image/png">
    <link rel="icon" href="/assets/images/android-chrome-512x512.png" sizes="512x512" type="image/png">
    <link rel="manifest" href="/site.webmanifest">
    <link rel="stylesheet" href="/assets/css/styles.css">
</head>
<body>
    <main>
        <h1>新躺平主义者的聚集地</h1>
        <p>扫描下方二维码，前往FIRE族社区，加入我们一起探索FIRE生活吧~</p>
        <img id="qrcode" src="/assets/images/qrcode_for_fire-zu/{page}.jpg" alt="FIRE族社区二维码">
    </main>
    
    <footer>
        <p class="icp-info">
            <a href="https://beian.miit.gov.cn/" target="_blank" rel="noopener noreferrer">京ICP备2023036916号-1</a>
        </p>
    </footer>
</body>
</html>
"""

# 公共样式文件内容
styles_content = """body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    min-height: 100vh;
    background-color: #f4f4f4;
    color: #333;
    text-align: center;
}

main {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
}
h1 {
    font-size: 2rem;
    margin: 0 auto 1rem auto;
    padding: 0 2rem;
    max-width: 90%;
}
p {
    font-size: 1rem;
    margin: 0 auto 2rem auto;
    padding: 0 2rem;
    max-width: 90%;
}
img {
    width: 200px;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

footer {
    padding: 1rem 0;
    margin-top: auto;
    width: 100%;
}

.icp-info {
    font-size: 0.75rem;
    color: #666;
    margin: 0;
}

.icp-info a {
    color: #666;
    text-decoration: none;
}

.icp-info a:hover {
    text-decoration: underline;
}
"""

# 自动生成的子路径编号
pages = [1, 2, 3]  # 需要生成的页面路径

# 创建项目根目录
project_dir = "../../"
os.makedirs(project_dir, exist_ok=True)

# 创建公共样式文件到新位置
assets_css_dir = os.path.join(project_dir, "assets", "css")
os.makedirs(assets_css_dir, exist_ok=True)
with open(os.path.join(assets_css_dir, "styles.css"), "w", encoding="utf-8") as styles_file:
    styles_file.write(styles_content)

# 创建渠道页面到pages/channels目录
channels_dir = os.path.join(project_dir, "pages", "channels")
os.makedirs(channels_dir, exist_ok=True)
for page in pages:
    page_dir = os.path.join(channels_dir, str(page))
    os.makedirs(page_dir, exist_ok=True)
    with open(os.path.join(page_dir, "index.html"), "w", encoding="utf-8") as html_file:
        html_file.write(html_template.format(page=page))

print(f"项目已成功生成在目录: {project_dir}")
