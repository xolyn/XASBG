import os
import datetime
import re
import markdown

def formatTime(t):
    return datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]

def getCat(s):
    return [x.strip() for x in s.split(",")]

def getDeafult(filename):
    path=os.path.join("post",filename)
    name=filename.replace(".md","").strip()
    time=formatTime(os.path.getmtime(path))
    return name,time

postList=os.listdir("./post")

def getAllPostInfo():
    postInfo={}
    for i in postList:
        with open(os.path.join("post",i)) as md:
            md=md.read()
        try:
            meta=re.search(r'<!--(.*?)-->', md, re.DOTALL).group(1).split("\n")
            meta=[x.strip() for x in meta if x.strip()!=""]
            postInfo[i]={x.split(":",maxsplit=1)[0]:x.split(":",maxsplit=1)[1].strip() for x in meta}
        except:
            # postInfo[i]={'title':i.replace(".md","").strip(), 'time':formatTime(os.path.getmtime(os.path.join("post",i))), 'category':""}
            postInfo[i]={'title':getDeafult(i)[0], 'time':getDeafult(i)[1], 'category':""}
    for i in postInfo:
        postInfo[i]["category"]=getCat(postInfo[i]["category"])
    return postInfo

def getMetaSingle(path):
    with open(path) as md:
        md=md.read()
    try:
        meta=re.search(r'<!--(.*?)-->', md, re.DOTALL).group(1).split("\n")
        meta=[x.strip() for x in meta if x.strip()!=""]
    except:
        meta=["title: "+getDeafult(os.path.basename(path))[0], "time: "+getDeafult(os.path.basename(path))[1]]
    return meta

def checkSite():
    if os.path.exists("site/")==False:
        os.makedirs("site/")
    
def md2html(mdPath):
    cssPath='https://f.xoy.one/css/styles.css'
    title=getMetaSingle(mdPath)[0].split(":",maxsplit=1)[1].strip()
    fileName=os.path.basename(mdPath).rsplit(".",maxsplit=1)[0]
    checkSite()
    htmlPath=os.path.join("site",fileName+".html")
    with open(mdPath, 'r', encoding='utf-8') as md:
        md = md.read()
    html_content = markdown.markdown(md,extensions=['tables','fenced_code'])
    # re.sub(r'<!--(.*?)-->', '',html_content, count=1)
    with open(htmlPath, 'w', encoding='utf-8') as html:
        html.write(
        f'''<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n<link rel='stylesheet' href='{cssPath}'>\n<title>{title}</title>\n</head>\n<body>\n
        ''')
        html.write(html_content)
        html.write("\n</body>\n</html><br>\n<center>\n<hr><p style='font-size:small'>built by <a href='#'>XASBG</a></p>\n</center>")

def getNewest(map:dict):
    try:
        return dict(sorted(map.items(), key=lambda item: item[1]['time'],reverse=True))
    except:
        print("invalid posts info format")

def buildIndex(blogName,indexCSSPath):
    newest=getNewest(getAllPostInfo())
    checkSite()
    with open("site/index.html", "w") as ip:
        ip.write(f'''<!DOCTYPE html>
                <html lang='en'>
                <head>
                <meta charset='UTF-8'>
                <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                <link rel='stylesheet' href='{indexCSSPath}'>
                <title>{blogName}</title>
                </head>
                <body>
                ''')
        for i in newest:
            postLoc=os.path.join('.',i.strip()[:-2]+'html')
            ip.write(f'''<div class="post">
                    <a href="{postLoc}" class="title">{newest[i]["title"]}</a>
                    <p class="date">{newest[i]["time"]}</p>
                    </div>
                    ''')
        ip.write("\n</body>\n</html>")

siteName=""

def build(siteName=siteName,IndexCSS="https://f.xoy.one/css/index.css"):
    mdNames=getAllPostInfo().keys()
    for i in mdNames:
        print(f"Converting `{i}`")
        md2html(os.path.join("post",i))
    buildIndex(siteName,IndexCSS)

menu='''
+---+----------------+
| B |  Build Site    |
+---+----------------+
| S |  Set Site Name |
+---+----------------+
| E |  Exit          |
+---+----------------+  
| M |  Menu          |
+---+----------------+  
'''

# ux:
print(f'''
   _  __ ___   _____ ____  ______
  | |/ //   | / ___// __ )/ ____/
  |   // /| | \__ \/ __  / / __  
 /   |/ ___ |___/ / /_/ / /_/ /  
/_/|_/_/  |_/____/_____/\____/  
                      Build 1.0.1   
''')

print("Welcome to use XASBG.\n\nSeems you haven't set your site name yet. Press 'S' to set it, or press 'M' to see more options:")

while (ui:=input(f"\nAwaiting user's prompt:").lower())!="e":
    ui=ui.lower()
    if ui not in ["b","s","m"]:
        print(f'''\ninvalid input, see options:\n{menu}''')
    elif ui=="m":
        print(menu)
    elif ui=="b":
        build(siteName=siteName)
        print("Build succesfully! Check site/ for website files!")
    elif ui=="s":
        siteName=input(f'''\nCurrent site name is: " {siteName} ".\nEnter your site name here, end by ENTER:\n''')
        print(f"Site name set to {siteName}!")
print("Program ends.")

