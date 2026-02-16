from blocktype import markdown_to_html_node
from extract_title import extract_title

import os, shutil

def generate_page(from_path, template_path, dest_path):
    print (f"Generating page from {from_path} to {dest_path} using {template_path}.")

    with open(from_path, "r") as f:
        from_markdown = f.read()

    with open(template_path, "r") as f:
        template_markdown = f.read()

    new_html = markdown_to_html_node(from_markdown).to_html()
    title = extract_title(from_markdown)

    full_html = template_markdown.replace(" Title ", title).replace(" Content ", new_html)
    
    with open(dest_path, "w") as f:
        f.write(full_html)

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    
    dirs = os.listdir(dir_path_content)
    for dir in dirs:
        check = os.path.join(dir_path_content, dir)
        check_dest = os.path.join(dest_dir_path, dir).replace(".md", ".html")
        if os.path.isdir(check):
            generate_pages_recursively(check, template_path, check_dest)
        else:
            generate_page(check, template_path, check_dest)