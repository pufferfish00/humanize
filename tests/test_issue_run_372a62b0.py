import pytest
import humanize


def test_naturalsize_noninteger_below_base():
    # Non‑integer values below the base should be formatted using the default format
    assert humanize.naturalsize(1.5) == "1.5 Bytes"
    assert humanize.naturalsize(1.5, gnu=True) == "1.5B"
