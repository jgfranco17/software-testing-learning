# Software Testing Learning

Just a playground space for practicing software testing concepts.

## Setup

### Pre-requisites

- [Python3](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/)
- [Just](https://github.com/casey/just) (optional)

### Development environment

To get started, clone the repository and navigate inside the project directory.

```bash
git clone https://github.com/jgfranco17/software-testing-learning.git
cd software-testing-learning
```

Once inside, you can run the installation.

```bash
poetry install
```

## Running Tests

After completing the installation, you can now begin to run the tests. This playground repository
provides two main types of tests: unit testing and feature testing.

```bash
# To run unit tests with Pytest
poetry run pytest

# To run feature tests with Behave
poetry run behave tests/bdd/
```
