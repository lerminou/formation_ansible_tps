class FilterModule(object):
    def filters(self):
        return {
            'to_camel': self.to_camel
        }

    def to_camel(self, text):
        return ''.join(x for x in text.title() if not x.isspace())
