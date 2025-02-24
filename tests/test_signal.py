import pytest

from system_under_test.software import Signal


def test_signal_initializes_correctly():
    signal = Signal("test_channel", [1, 2, 3])
    assert signal.channel == "test_channel"
    assert signal.values == [1, 2, 3]
