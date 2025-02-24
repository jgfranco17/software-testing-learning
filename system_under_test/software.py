import logging

from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from system_under_test.errors import SignalError

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Signal:
    """Represents a signal in a system."""

    channel: str
    values: List[int]

    def __repr__(self):
        """String representation of the signal."""
        return f"Signal(channel='{self.channel}', values={self.values})"


class Receiver:
    """Receiver class, used to read signals."""

    def __init__(
        self, channels: List[str], auto_enabled: Optional[bool] = True
    ) -> None:
        self.__signal_channels: Dict[str, List[int]] = defaultdict(list)
        for channel in channels:
            self.__signal_channels[channel] = []
        self.__is_enabled = auto_enabled

    def __getitem__(self, key: str) -> List[int]:
        if not isinstance(key, str):
            raise SignalError(key, f"Invalid channel type ({type(key)}) on receiver")
        if key not in self.__signal_channels.keys():
            raise SignalError(key, "Channel not found in receiver")
        return self.__signal_channels[key]

    @property
    def is_enabled(self) -> bool:
        """Return current state of the receiver."""
        return self.__is_enabled

    def enable(self) -> None:
        """Enable the receiver."""
        self.__is_enabled = True

    def disable(self) -> None:
        """Disable the receiver."""
        self.__is_enabled = False

    def get_current_channels(self) -> Tuple[str]:
        """Get the current channels of the receiver.

        Returns:
            Tuple[str]: All available channelss
        """
        return tuple(self.__signal_channels.keys())

    def __update_channel(self, channel_name: str, new_values: List[int]) -> None:
        current_contents = self.__signal_channels[channel_name]
        self.__signal_channels[channel_name] = current_contents + new_values

    def receive_signal(
        self, signal: Signal, not_exist_ok: Optional[bool] = False
    ) -> None:
        """Read in an incoming signal object.

        Args:
            signal (Signal): Signal to read
            not_exist_ok (bool, default=False): If false, fail if reading to non-existent channel.

        Raises:
            SignalError: If the receiver is disabled when reading
        """
        if not self.__is_enabled:
            raise SignalError(
                channel=signal.channel,
                message=f"Receiver for channel '{signal.channel}' is disabled",
            )
        if signal.channel not in self.get_current_channels():
            if not_exist_ok:
                raise SignalError(
                    channel=signal.channel, message="Invalid signal channel"
                )
            logger.info(
                f"Channel '{signal.channel}' not in current channels, added new."
            )
        self.__update_channel(signal.channel, signal.values)
