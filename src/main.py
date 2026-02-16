from textnode import TextNode, TextType

import os, shutil, sys

from generate_page import generate_page, generate_pages_recursively

basepath = sys.argv[0]
if basepath == "":
    basepath = "/"

def copy_static_contents(public = "", static = ""):
    subpublic = os.path.join("./docs", public)
    substatic = os.path.join("./static", static)

    if os.path.exists(subpublic): 
        shutil.rmtree(subpublic)

    os.mkdir(subpublic)
    
    for content in os.listdir(substatic):
        path = os.path.join(substatic, content)
        if os.path.isdir(path):
            copy_static_contents(content, content)
        else:
            destination = os.path.join(subpublic, content)
            shutil.copy(path, destination)

def main():
    copy_static_contents()
    #generate_page("content/index.md", "src/template.html", "public/index.html")
    generate_pages_recursively("content/", "src/template.html", "docs/", basepath)
main()