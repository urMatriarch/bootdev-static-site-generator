def extract_title(markdown):
    lines = markdown.split("\n")
    title = ""
    for line in lines:
        if line.startswith("#"):
            title = line.strip("#").strip()
    return title