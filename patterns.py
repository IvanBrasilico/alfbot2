'''Configuration of the routes, or vocabulary of the bot'''
from restapp import ch
from bottery.conf.patterns import Pattern, DefaultPattern
from botteryext.bdicttalk.patterns import (first_word,
                                           FunctionPattern,
                                           HangUserPattern)
from bottery.views import pong
from views import help_text, view, say_help

from rules import RULES
PATTERN_LIST = RULES['pattern_list']

hang_user_pattern = HangUserPattern(view)
ch.set_hang(hang_user_pattern, PATTERN_LIST[0])
ch.set_hang(hang_user_pattern, PATTERN_LIST[1])

patterns = [
    hang_user_pattern,
    FunctionPattern(PATTERN_LIST[0], view, first_word),
    FunctionPattern(PATTERN_LIST[1], view, first_word),
    Pattern('ping', pong),
    Pattern('help', help_text),
    DefaultPattern(say_help)
]
