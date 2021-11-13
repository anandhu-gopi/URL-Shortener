from modules.dao import dao
from errors import (
    MaxRetriesExceededForUrlCreation,
    OriginalURLNotFoundError,
    ShortURLAlreadyExistError,
    ShortURLNotFoundError,
)
import shortuuid
from datetime import datetime, time
from random import randint
from flask import request


class URLShortner:
    def __init__(self, original_url="") -> None:
        self.original_url = original_url

    def _original_url_already_exists(self) -> bool:
        with dao.connection as conn:
            row = conn.execute(
                "SELECT id FROM urls" " WHERE original_url= (?)", (self.original_url,)
            ).fetchone()
            if not row:
                return False
            return True

    def _generate_unique_code_for_url(self) -> str:

        uuid = shortuuid.uuid(
            name=f"{self.original_url}_"
            f"{randint(1,99999)}"
            f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
        )
        return uuid[:8]

    def _short_url_already_exists(self, short_url) -> bool:
        with dao.connection as conn:
            row = conn.execute(
                "SELECT id FROM urls" " WHERE short_url= (?)", (short_url,)
            ).fetchone()
            if not row:
                return False
            return True

    def create_short_url(self) -> None:

        if self._original_url_already_exists():
            raise ShortURLAlreadyExistError()
        retry_counter = 3
        short_url = request.host_url + self._generate_unique_code_for_url()
        while self._short_url_already_exists(short_url) and retry_counter > 0:
            time.sleep(1)
            short_url = request.host_url + self._generate_unique_code_for_url()
            retry_counter -= 1
        if self._short_url_already_exists(short_url):
            raise MaxRetriesExceededForUrlCreation()
        with dao.connection as conn:
            conn.execute(
                "INSERT INTO urls (original_url,short_url) VALUES(?,?)",
                (self.original_url, short_url),
            )

    def get_short_url(self) -> str:
        with dao.connection as conn:
            row = conn.execute(
                "SELECT short_url FROM urls" " WHERE  original_url= (?)",
                (self.original_url,),
            ).fetchone()
            if not row:
                raise ShortURLNotFoundError()
            return row[0]

    def get_original_url_from_short_url_id(self, short_url_id) -> str:
        short_url = request.host_url + short_url_id
        with dao.connection as conn:
            row = conn.execute(
                "SELECT original_url FROM urls" " WHERE  short_url= (?)", (short_url,)
            ).fetchone()
            if not row:
                raise OriginalURLNotFoundError()
            return row[0]
