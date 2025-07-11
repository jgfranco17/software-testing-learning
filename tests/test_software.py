from typing import List

import pytest

from system_under_test.errors import ReceiverStateError, SignalError
from system_under_test.software import Receiver, Signal


@pytest.mark.parametrize(
    "channels",
    [
        [],
        ["channel1", "channel2", "channel3"],
    ],
)
def test_receiver_init(channels: List[str]):
    receiver = Receiver(channels)
    loaded_channels = tuple(channels)
    assert (
        receiver.get_current_channels() == loaded_channels
    ), f"Expected {len(channels)} but got {len(receiver.get_current_channels())}"


def test_receiver_initializes_default_correctly():
    receiver = Receiver(["channel1", "channel2", "channel3"])
    assert receiver.is_enabled, "Expected receiver to be enabled but was not"
    assert receiver.get_current_channels() == ("channel1", "channel2", "channel3")
    assert receiver.is_enabled, "Expected reciever to be enabled by default"


def test_receiver_enable_method_success():
    receiver = Receiver(["channel1"], auto_enabled=False)
    receiver.enable()
    assert receiver.is_enabled, "Expected reciever to be enabled by method"


def test_receiver_enable_method_fail():
    receiver = Receiver(["channel1"], auto_enabled=True)
    with pytest.raises(ReceiverStateError):
        receiver.enable()


def test_receiver_disable_method_success():
    receiver = Receiver(["channel1"], auto_enabled=True)
    assert receiver.is_enabled
    receiver.disable()
    assert not receiver.is_enabled, "Expected reciever to be disabled by method"


def test_receiver_disable_method_fail():
    receiver = Receiver(["channel1"], auto_enabled=False)
    with pytest.raises(ReceiverStateError):
        receiver.disable()


def test_receiver_signal_read_same_channel_ok():
    receiver = Receiver(["channel1", "channel2", "channel3"])
    first_signal = Signal("channel1", [1, 2, 3])
    receiver.receive_signal(first_signal)
    assert receiver["channel1"] == [1, 2, 3]
    assert not receiver["channel2"]
    assert not receiver["channel3"]
    second_signal = Signal("channel1", [4, 5])
    receiver.receive_signal(second_signal)
    assert receiver["channel1"] == [1, 2, 3, 4, 5]


def test_receiver_signal_read_when_disabled():
    receiver = Receiver(["channel1", "channel2", "channel3"], auto_enabled=False)
    assert not receiver.is_enabled
    first_signal = Signal("channel1", [1, 2, 3])
    with pytest.raises(SignalError):
        receiver.receive_signal(first_signal)


def test_receiver_signal_lookup_non_string_channel():
    receiver = Receiver(["channel1", "channel2", "channel3"])
    with pytest.raises(SignalError):
        _ = receiver[1]


def test_receiver_signal_lookup_non_existent_channel():
    receiver = Receiver(["channel1", "channel2", "channel3"])
    with pytest.raises(SignalError):
        _ = receiver["channel4"]
