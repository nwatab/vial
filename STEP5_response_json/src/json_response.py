import json
from .response import Response


class JSONResponse(Response):
    default_content_type = 'text/json; charset=utf-8'
    
    def __init__(self, dic, status=200, headers=None, charset=None, **dump_args):
        self.dic = dic
        self.json_dump_args = dump_args
        super().__init__('', status, headers, charset)
    
    @property
    def body(self):
        return [json.dumps(self.dic, **self.json_dump_args).encode(self.charset)]
