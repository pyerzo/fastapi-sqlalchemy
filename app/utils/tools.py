"""Utils tools functions"""

import os
from typing import Any


def env(key: Any, raise_empty: bool = True) -> str:
    """Returns an environment value"""
    value = os.getenv(key, "")
    if raise_empty and not value:
        raise EnvironmentError(f"Enviroment key '{key}' not found")
    return value
