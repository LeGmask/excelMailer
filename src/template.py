import re

from pandas import Timestamp


class TemplateManager:
    def __init__(self, config):
        self.template = None
        self.data = None
        self.config = config

        self.load_template()

    def load_template(self):
        self.template = open(self.config.get(['TEMPLATE', 'filepath']), 'r').read()

    def replace_match(self, match):
        content = self.data[match.group(1)]

        if isinstance(content, Timestamp):
            content = content.strftime('%d/%m/%Y')

        return str(content)

    def populate_template(self, data):
        self.data = data
        regex = self.config.get(['TEMPLATE', 'regex'])

        # sub all regex matches in template
        return re.sub(regex, self.replace_match, self.template)