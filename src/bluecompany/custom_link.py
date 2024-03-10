import json
import re

from mistletoe.html_renderer import HtmlRenderer
from mistletoe.span_token import SpanToken

__all__ = ["CustomLink", "CustomLinkRenderer"]


class CustomLink(SpanToken):
    pattern = re.compile(
        r"""
        \[\[
        (.+?)
        (?:
            \|
            (.+?)
        )?
        \]\]
        """,
        re.VERBOSE,
    )

    def __init__(self, match):
        self.target = match.group(1).strip()
        self.text = match.group(2).strip() if match.group(2) else self.target


class CustomLinkRenderer(HtmlRenderer):
    def __init__(self):
        super().__init__(CustomLink)
        self.links = []

    def render_custom_link(self, token):
        template = '<a href="{target}">{text}</a>'
        target = token.target
        text = token.text

        # Extract the components from the target
        match = re.match(
            r"""
            (
                [^#]*
            )
            (?:
                \#
                (.*)
            )?
            """,
            target,
            re.VERBOSE,
        )
        page = match.group(1)
        section = match.group(2) if match.group(2) else ""

        # Append the link to the list of dictionaries with separated components
        link_dict = {"target": target, "text": text, "page": page, "section": section}
        self.links.append(link_dict)

        return template.format(target=target, text=text)

    def render(self, *args, **kwargs):
        rendered = super().render(*args, **kwargs)

        # Convert the list of links to JSON format
        links_json = json.dumps(self.links)

        return rendered

    def get_links_json(self):
        return json.dumps(self.links, indent=2)
