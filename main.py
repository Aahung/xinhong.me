import os
import sys
import jinja2


os.system("rm -Rf ./production && mkdir -p ./production")


template_env = jinja2.Environment(loader=jinja2.FileSystemLoader('source'))


def render(directory, path, homepage=False):
    template = template_env.get_template('pages%s' % (path,))
    os.system("mkdir -p ./production%s" % (directory,))
    with open("./production%s" % (path,), 'w') as f:
        f.write(template.render(homepage=homepage))
        f.close()


PAGE_DIR = 'source/pages'
for root, subdirs, files in os.walk(PAGE_DIR):
    for file in files:
        if not file.endswith(".html"):
            continue
        directory = root.replace(PAGE_DIR, "")
        path = "%s/%s" % (directory, file)
        render(directory, path, directory == "")


os.system("bash compile.sh")