import os
import re

files = [
    "skyapp/organization/templates/organization/home.html",
    "skyapp/organization/templates/organization/team_type_list.html",
    "skyapp/organization/templates/organization/department_detail.html",
    "skyapp/organization/templates/organization/team_detail.html"
]

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Extract script
    script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
    script_content = script_match.group(1) if script_match else ''

    # Extract style
    style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    style_content = style_match.group(1) if style_match else ''

    # Remove global styles
    for selector in ['body', '\.sidebar', '\.main', ':root', '\.topbar', '\.logo', '\.logo img', '\.nav-item', '\.nav-item:hover', '\.nav-item\.active', '\.layout', '\.sky-navbar', '\.sky-logo', '\.search', '\.search::placeholder', '\.icons']:
        style_content = re.sub(rf'{selector}\s*\{{[^}}]*\}}', '', style_content)

    # Extract body content
    body_match = re.search(r'<body>(.*?)</body>', content, re.DOTALL)
    if not body_match:
        body_content = ""
    else:
        body_content = body_match.group(1)

    # Clean up body content
    if 'home.html' in filepath:
        body_content = re.sub(r'<div class="sidebar">.*?</div>\s*<div class="main">', '<div class="main">', body_content, flags=re.DOTALL)
        body_content = re.sub(r'<div class="topbar">.*?</div>', '', body_content, flags=re.DOTALL)
        body_content = body_content.replace('<div class="layout">', '')
        body_content = body_content.replace('<div class="main">', '')
        # Remove the last two </div> tags
        body_content = body_content.rsplit('</div>', 2)[0]
    elif 'team_detail.html' in filepath:
        body_content = body_content.replace('<div class="main">', '')
        body_content = body_content.rsplit('</div>', 1)[0]
    else:
        body_content = body_content.replace('<div class="main">', '')
        body_content = body_content.rsplit('</div>', 1)[0]

    # Handle team_detail.html sidebar
    if 'team_detail.html' in filepath:
        body_content = re.sub(r'<div class="sidebar">.*?</div>', '', body_content, flags=re.DOTALL)

    new_file = "{% extends 'base.html' %}\n{% load static %}\n\n"
    
    if style_content.strip():
        new_file += "{% block extra_css %}\n<style>\n" + style_content.strip() + "\n</style>\n{% endblock %}\n\n"
        
    if script_content.strip():
        new_file += "{% block extra_js %}\n<script>\n" + script_content.strip() + "\n</script>\n{% endblock %}\n\n"
        
    new_file += "{% block content %}\n" + body_content.strip() + "\n{% endblock %}\n"

    with open(filepath, 'w') as f:
        f.write(new_file)

print("Done.")
