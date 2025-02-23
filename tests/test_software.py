import pytest

from system_under_test.software import Receiver, Signal


def test_signal_initializes_correctly():
    signal = Signal("test_channel", [1, 2, 3])
    assert signal.channel == "test_channel"
    assert signal.values == [1, 2, 3]


def test_receiver_initializes_default_correctly():
    receiver = Receiver(["channel1", "channel2", "channel3"])
    assert receiver.is_enabled, "Expected receiver to be enabled but was not"
    assert receiver.get_current_channels() == ("channel1", "channel2", "channel3")
    assert receiver.is_enabled, "Expected reciever to be enabled by default"


def test_receiver_enable_method():
    receiver = Receiver(["channel1"], auto_enabled=False)
    assert not receiver.is_enabled
    receiver.enable()
    assert receiver.is_enabled, "Expected reciever to be enabled by method"
