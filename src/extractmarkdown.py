import re

def extract_markdown_images(text):
    extracted_images = []
    matches = re.findall(r"\!\[(.+?)]\((.+?)\)", text)
    extracted_images.extend(matches)
    return extracted_images

def extract_markdown_links(text):
    extracted_links = []
    matches = re.findall(r"\[(.+?)]\((.+?)\)", text)
    extracted_links.extend(matches)
    return extracted_links