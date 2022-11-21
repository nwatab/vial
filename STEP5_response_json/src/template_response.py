from .response import Response

class TemplateResponse(Response):
    default_content_type = 'text/html; charset=utf-8'

    def __init__(self, filename, status=200, headers=None, charset='utf-8', **tpl_args):
        self.filename = filename
        self.tpl_args = tpl_args
        super().__init__(body='', status=status, headers=headers, charset=charset)

    def render_body(self, jinja2_environment):
        template = jinja2_environment.get_template(self.filename)
        return [template.render(**self.tpl_args).encode(self.charset)]