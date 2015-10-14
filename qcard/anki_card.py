class AnkiCard:
    def __init__(self, fields):
        self.fields = fields

    def generate(self, **opts):
        return "\t".join(self.format_field(f, **opts) for f in self.fields)

    @staticmethod
    def format_field(field, **opts):
        f = field
        if opts.get('format') == 'latex':
            f = '[latex]' + f + '[/latex]'
        if '"' in f:
            f = f.replace('"', '&quot;')
        if "\t" in f or "\n" in f:
            f = '"' + f + '"'
        return f
