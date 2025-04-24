Feature: Validate Signal Receiver

    As a signal engineer
    I want to recevie signals with a receiver
    So that I can collect signals programatically

    Scenario: Check receiver init
        Given I have a receiver with 2 channels
        Then the receiver has 2 channels
        And the receiver has channel "channel1"
        And the receiver has channel "channel2"

    Scenario: Check receiver is enabled automatically
        Given I have a receiver with 3 channels
        Then the receiver is on

    Scenario: Check receiver power cycling
        Given I have a receiver with 3 channels
        When I deactivate the receiver
        Then the receiver is off
