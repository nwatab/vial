import unittest
from ..request import Request


sample_environ = {'SECURITYSESSIONID': '186a5', 'USER': 'n', 'MallocNanoZone': '0', '__CFBundleIdentifier': 'com.microsoft.VSCode', 'COMMAND_MODE': 'unix2003', 'PATH': '/Users/n/work/wsgi-practice/.env/bin:/Users/n/google-cloud-sdk/bin:/Users/n/.nodebrew/current/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin:/Library/Apple/usr/bin:/Users/n/work/wsgi-practice/.env/bin:/Users/n/google-cloud-sdk/bin:/Users/n/.nodebrew/current/bin:/Users/n/flutter/bin:/Users/n/Library/Android/sdk/platform-tools:/Applications/Android Studio.app/Contents/jre/jdk/Contents/Home/bin:/Users/n/flutter/bin:/Users/n/Library/Android/sdk/platform-tools:/Applications/Android Studio.app/Contents/jre/jdk/Contents/Home/bin', 'SHELL': '/bin/zsh', 'HOME': '/Users/n', '__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0x0', 'LaunchInstanceID': '128206F3-D8B4-416A-B2F6-480783331D07', 'XPC_SERVICE_NAME': '0', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.YFywm2fn9f/Listeners', 'XPC_FLAGS': '0x0', 'LOGNAME': 'n', 'TMPDIR': '/var/folders/8_/sb4zq2kx6v5bwlrnl4zvz8nh0000gn/T/', 'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 'GREP_COLORS': 'mt=37;45', 'PWD': '/Users/n/work/wsgi-practice', 'VIRTUAL_ENV_DISABLE_PROMPT': '12', 'LESS_TERMCAP_se': '\x1b[0m', 'LS_COLORS': 'di=34:ln=35:so=32:pi=33:ex=31:bd=36;01:cd=33;01:su=31;40;07:sg=36;40;07:tw=32;40;07:ow=33;40;07:', 'LC_CTYPE': 'UTF-8', 'LESS_TERMCAP_me': '\x1b[0m', 'TERM': 'xterm-256color', 'CONDA_CHANGEPS1': 'no', 'TERM_SESSION_ID': '15AD7A38-1F1B-4843-9C91-5FC18953CFB7', 'SHLVL': '3', 'TERM_PROGRAM_VERSION': '1.72.2', 'LESS_TERMCAP_md': '\x1b[01;31m', 'LESS_TERMCAP_us': '\x1b[01;32m', 'LESS_TERMCAP_so': '\x1b[00;47;30m', 'LESS_TERMCAP_ue': '\x1b[0m', 'LSCOLORS': 'exfxcxdxbxGxDxabagacad', 'TERM_PROGRAM': 'vscode', 'GREP_COLOR': '37;45', 'JAVA_HOME': '/Applications/Android Studio.app/Contents/jre/jdk/Contents/Home', 'LESS_TERMCAP_mb': '\x1b[01;31m', 'LANG': 'en_US.UTF-8', 'COLORTERM': 'truecolor', 'GIT_ASKPASS': '/Applications/Visual Studio Code.app/Contents/Resources/app/extensions/git/dist/askpass.sh', 'VSCODE_GIT_ASKPASS_NODE': '/Applications/Visual Studio Code.app/Contents/Frameworks/Code Helper.app/Contents/MacOS/Code Helper', 'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '--ms-enable-electron-run-as-node', 'VSCODE_GIT_ASKPASS_MAIN': '/Applications/Visual Studio Code.app/Contents/Resources/app/extensions/git/dist/askpass-main.js', 'VSCODE_GIT_IPC_HANDLE': '/var/folders/8_/sb4zq2kx6v5bwlrnl4zvz8nh0000gn/T/vscode-git-d87fb4994a.sock', 'VSCODE_INJECTION': '1', 'ZDOTDIR': '/Users/n', 'USER_ZDOTDIR': '/Users/n', 'OLDPWD': '/Users/n/work/wsgi-practice/routing-basic', 'PROMPT_EOL_MARK': '', 'VIRTUAL_ENV': '/Users/n/work/wsgi-practice/.env', '_': '/Users/n/work/wsgi-practice/.env/bin/python', 'SERVER_NAME': 'womenzaichidaiqumaihuoguodiliaoranhouquzaixinsuchihuoguo.local', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'POST', 'PATH_INFO': '/user/', 'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': '127.0.0.1:8000', 'HTTP_USER_AGENT': 'curl/7.79.1', 'HTTP_ACCEPT': '*/*', 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': False, 'wsgi.multiprocess': False}
#  'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>
#  'wsgi.input': < _io.BufferedReader name = 4 > , 'wsgi.errors': < _io.TextIOWrapper name = '<stderr>' mode = 'w' encoding = 'utf-8' >

class RequestTest(unittest.TestCase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.environ = sample_environ
        self.request = Request(self.environ)
    
    def test_path(self):
        self.assertEqual(
            self.request.path,
            self.environ['PATH_INFO']
        )
    
    def test_method(self):
        self.assertEqual(self.request.method, 'POST')
    
    def test_body(self):
        self.assertEqual(self.request.body, b'')
    
    def test_text(self):
        self.assertEqual(self.request.text, '')
    
    def test_query(self):
        self.assertEqual(self.request.query, {})
    
    def test_json(self):
        pass


if __name__ == '__main__':
    unittest.main()