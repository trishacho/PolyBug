import string

def slugify(_string):
        valid_chars = frozenset("_{}{}".format(string.ascii_letters, string.digits))
        if _string[0].isdigit():
            _string = "_" + _string
        return "".join(c if c in valid_chars else "_" for c in _string)