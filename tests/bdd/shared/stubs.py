from pathlib import Path
from typing import List, Union

from behave.runner import Context

from system_under_test.software import Receiver


class TestContext(Context):
    """File context interface for development and testing."""

    receiver: Receiver
    last_exception: Union[Exception, None]
    files_created: List[Path]
    dirs_created: List[Path]
