language_dict = {"English": "en", "Arabic": "ar", "French": "fr"}


class color:

    _format = '\033[{};{};40m'

    colors = {
        'red': 31,
        'green': 32,
        'yellow': 33,
        'purple': 35,
        'blue': 94,
        'cyan': 34
    }

    styles = {
        'bold': 1,
        'italic': 3,
        'underline': 4,
    }

    RED = '\033[0;31;40m'
    GREEN = '\033[0;32;40m'
    YELLOW = '\033[0;33;40m'
    PURPLE = '\033[0;35;40m'
    BLUE = '\033[0;94;40m'
    CYAN = '\033[0;34;40m'

    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

    @staticmethod
    def format(colors, style):

        return color._format.format(color.styles[style], color.colors[colors])
