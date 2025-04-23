class SignalError(Exception):
    def __init__(self, channel: str, message: str):
        self.__channel = channel
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"SignalError on channel '{self.__channel}': {self.message}"


class ReceiverStateError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"ChannelStateError: {self.message}"
