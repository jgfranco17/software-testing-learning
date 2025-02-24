import pytest

from system_under_test.software import Receiver, Signal, SignalError


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


def test_receiver_disable_method():
    receiver = Receiver(["channel1"], auto_enabled=True)
    assert receiver.is_enabled
    receiver.disable()
    assert not receiver.is_enabled, "Expected reciever to be disabled by method"


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
