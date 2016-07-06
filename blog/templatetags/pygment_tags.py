import re

from django import template
from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters.html import HtmlFormatter
from pygments.lexers.python import PythonLexer

register = template.Library()

regex = re.compile(r'<pre><code(.*?)>(.*?)</code></pre>', re.DOTALL)


@register.filter(name='highlight_code')
def highlight_code(value):
    last_end = 0
    to_return = ''
    found = 0
    for match_obj in regex.finditer(value):
        code_class = match_obj.group(1) if match_obj.group(1) else None
        code_string = match_obj.group(2)
        if code_class:
            if code_class.find('class'):
                language = re.split(r'"|\'', code_class)[1]
                lexer = get_lexer_by_name(language)
        else:
            try:
                lexer = guess_lexer(str(code_string))
            except ValueError:
                lexer = PythonLexer()
        pygmented_string = highlight(code_string, lexer, HtmlFormatter())
        to_return = to_return + value[last_end:match_obj.start(0)] + pygmented_string
        last_end = match_obj.end(2)
        found = found + 1
    to_return = to_return + value[last_end:]
    return to_return
