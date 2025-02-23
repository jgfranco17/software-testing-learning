PROJECT_NAME := "aeternum"

# Default command
default:
    @just --list --unsorted

# Set up dependencies
install:
    @poetry install
    @echo "Installed Poetry dependencies!"

# Run Pytest with arguments
pytest *args:
    poetry run pytest {{ args }}

# Run the linter
lint:
    @poetry run black .
