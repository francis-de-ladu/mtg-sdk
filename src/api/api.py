import json
import os
import sys
import time
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional, Self, TypedDict, TypeVar
from uuid import UUID

import requests
from loguru import logger
from typing_extensions import NotRequired, Unpack

from src.base import Base

from .endpoints import CardsEndpoint, Endpoint, SetsEndpoint


class PathVars(TypedDict):
    id: NotRequired[UUID | str | int]
    set: NotRequired[str]


class LogLevel(Enum):
    TRACE = "TRACE"
    DEBUG = "DEBUG"
    INFO = "INFO"
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


logger.remove()
logger.add(sys.stderr, level=LogLevel.DEBUG.value)


U = TypeVar("U", bound=Base)


class ApiClient:
    _base_url = "https://api.scryfall.com"
    _instance: Optional[Self] = None  # the api client singleton instance

    _previous_at = -1.0  # time when last request was sent
    _min_wait_time = 0.1  # wait time between requests in seconds

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ApiClient, cls).__new__(cls)
        return cls._instance

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def min_wait_time(self) -> float:
        return self._min_wait_time

    @property
    def previous_at(self) -> float:
        return self._previous_at

    def _create_url(self, endpoint: Endpoint, path_vars: PathVars) -> str:
        if isinstance(endpoint, CardsEndpoint):
            raw_path = f"cards/{endpoint.value}"
        elif isinstance(endpoint, SetsEndpoint):
            raw_path = f"sets/{endpoint.value}"
        else:
            raise NotImplementedError(f"Unhandled endpoint type `{type(endpoint)}`")

        path = raw_path.format(**path_vars)
        return os.path.join(self.base_url, path)

    def _wait_delay(self) -> None:
        delta = time.time() - self.previous_at

        if delta < self.min_wait_time:
            sleep_time = self.min_wait_time - delta
            logger.info(f"Sleeping for {round(1000 * sleep_time)} ms...")
            time.sleep(sleep_time)

        self._previous_at = time.time()

    def get(self, endpoint: Endpoint, output: type[U], params: dict, /, **path_vars: Unpack[PathVars]) -> U:
        self._wait_delay()

        url = self._create_url(endpoint, path_vars)
        resp = requests.get(url, params)
        logger.info(f"{resp} --- {path_vars=} --- {params=}")

        try:
            content = resp.json()
            return output.from_dict(content)
        except Exception as e:
            logger.error(f"{type(e).__name__}: {e}")

            out_path = Path("errors") / f"{datetime.now()}.json"
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with out_path.open("w") as fp:
                json.dump(content, fp, indent=4)

            raise e

    def post(
        self,
        endpoint: Endpoint,
        output: type[U],
        params: dict,
        payload: dict,
        /,
        **path_vars: Unpack[PathVars],
    ) -> U:
        self._wait_delay()

        url = self._create_url(endpoint, path_vars)
        resp = requests.post(url, params=params, json=payload)
        logger.info(f"{resp} --- {path_vars=} --- {params=}")

        try:
            content = resp.json()
            print(len(content["not_found"]))
            print(len(content["data"]))
            print(content["not_found"])
            return output.from_dict(content)
        except Exception as e:
            # logger.error(f"{type(e).__name__}: {e}")

            # out_path = Path("errors") / f"{datetime.now()}.json"
            # out_path.parent.mkdir(parents=True, exist_ok=True)
            # with out_path.open("w") as fp:
            #     json.dump(content, fp, indent=4)

            raise e
