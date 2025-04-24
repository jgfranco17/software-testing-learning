import logging
import os
import shutil

from behave.model import Scenario

from tests.bdd.shared.stubs import TestContext

logger = logging.getLogger(__name__)


def before_scenario(context: TestContext, scenario: Scenario):
    """Initialize shared context data."""
    context.last_exception = None
    logger.debug(f"Starting scenario: {scenario.name}")


def after_scenario(context: TestContext, scenario: Scenario):
    """Clean up shared context data after a scenario."""
    context.last_exception = None
    logger.debug(f"Scenario '{scenario.name}' ran in {scenario.duration:.2f}s")
