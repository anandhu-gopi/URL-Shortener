class URLShortnerError(Exception):
    pass


class FileNotFoundError(URLShortnerError):
    pass


class MaxRetriesExceededForUrlCreation(URLShortnerError):
    pass


class ShortURLNotFoundError(URLShortnerError):
    pass


class ShortURLAlreadyExistError(URLShortnerError):
    pass


class OriginalURLNotFoundError(URLShortnerError):
    pass
