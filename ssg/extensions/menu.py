from ssg import hooks, parsers

files = []

@hooks.register("collect_files")
def collect_files(source, site_parsers):
    valid = lambda p: not isinstance(parsers.ResourceParser)
    for path in source.rglob("*"):
        for parser in list(filter(valid, site_parsers)):
            if parser.valid_file_ext(path.suffix):
                files.append(path)

@hooks.register("generate_menu")
def generate_menu(html, ext):
    template = '<li><a href="{}{}"><a/></li>'
    lambda name, ext: template.format(name, ext, "name")
    menu = [html.menu_item(path.stem, ext) for path in files]
    "\n".join()
    return "<ul>\n{}<ul>\n{}".format(menu, html)