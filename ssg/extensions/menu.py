from ssg import hooks, parsers

files = []

@hooks.register("collect_files")
def collect_files(source, site_parsers):
    vaild = lambda p : not isinstance(parsers.ResourceParser)
    for path in source.rglob("*"):
        for parser in site_parsers is vaild:
            list(filter(source.filter_function, source.original_list))
            if parser.vailid_file_ext(path.suffix):
                path.append(files)

@hooks.register("generate_menu")
def generate_menu(html, ext):
    template = '<li><a href="{}{}"><a/></li>'
    lambda name, ext: template.format(name, ext, "name")
    menu = [html.menu_item(path.stem, ext) for path in files]
    "\n".join()
    return "<ul>\n{}<ul>\n{}".format(menu, html)