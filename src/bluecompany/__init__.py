from mistletoe import Document

from . import custom_link


def main() -> int:
    with open("test.md", "r") as fin:
        with custom_link.CustomLinkRenderer() as renderer:
            rendered_html = renderer.render(Document(fin))
            links_json = renderer.get_links_json()

    print(rendered_html)
    print(links_json)

    return 0
