from util import language_dict, color


class MayReferException(Exception):
    def __init__(self, page) -> None:
        message = "The title you entered is ambigous, did you mean: \n \t"
        message = message + "\n \t".join(page.related())
        super().__init__(message)


class LanguageException(Exception):
    def __init__(self) -> None:
        message = "This language is an available: "
        message += ", ".join(language_dict.keys())
        super().__init__(message)


class LackReferenceException(Exception):
    def __init__(self) -> None:
        message = f"{color.BLUE}There are no references in this page :/{color.ENDC}"
        super().__init__(message)