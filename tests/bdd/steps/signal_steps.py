import logging

from behave import given, when, then

from system_under_test.software import Receiver
from tests.bdd.shared.stubs import TestContext

logger = logging.getLogger(__name__)


@given("I have a receiver with {channel_count:d} channels")
def step_init_new_receiver(context: TestContext, channel_count: int):
    """Init a new Receiver instance with predefined channels."""
    channels = [f"channel{i+1}" for i in range(channel_count)]
    context.receiver = Receiver(channels)
    logger.info(f"Created new Receiver with {channel_count} channels")


@given("I activate the receiver")
@when("I activate the receiver")
def step_enable_receiver(context: TestContext):
    """Enable the reciever."""
    context.receiver.enable()


@given("I deactivate the receiver")
@when("I deactivate the receiver")
def step_disable_receiver(context: TestContext):
    """Enable the reciever."""
    context.receiver.disable()


@then("the receiver has {expected_count:d} channels")
def step_check_channel_count(context: TestContext, expected_count: int):
    """Assert that the reciever has the expected channel count."""
    channel_count = len(context.receiver.get_current_channels())
    assert (
        channel_count == expected_count
    ), f"Expected {expected_count} channels but found {channel_count}"


@then('the receiver has channel "{channel_name}"')
def step_check_receiver_disabled(context: TestContext, channel_name: str):
    """Assert that the reciever has a specifc channel."""
    channels = context.receiver.get_current_channels()
    is_channel_contained = channel_name in context.receiver.get_current_channels()
    assert (
        is_channel_contained
    ), f"Receiver did not have channel '{channel_name}': {channels}"


@then("the receiver is on")
def step_check_receiver_enabled(context: TestContext):
    """Assert that the reciever is on."""
    assert (
        context.receiver.is_enabled
    ), "Receiver was expected to be enabled but was not"


@then("the receiver is off")
def step_check_receiver_disabled(context: TestContext):
    """Assert that the reciever is off."""
    assert (
        not context.receiver.is_enabled
    ), "Receiver was expected to be disabled but was not"
