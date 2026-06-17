# PyWorkout Test Suite

This directory contains the comprehensive test suite for PyWorkout. The tests are written using pytest and provide coverage for the CLI, the workout REPL, and the config/history modules.

## Test Structure

```
tests/
├── __init__.py          # Package initialization
├── conftest.py          # Shared fixtures (isolates ~/.pyworkout in a tmp dir)
├── test_main.py         # Tests for main.py (workout REPL + bug regressions)
├── test_cli.py          # Tests for cli.py (argparse flags)
├── test_config.py       # Tests for config.py (load/merge/init user config)
└── test_history.py      # Tests for history.py (persistence)
```

## Test Coverage

The test suite includes the following test categories:

### Main Module Tests (`test_main.py`)

1. **TestWorkoutData** - Tests workout data structures
   - Validates workout groups are defined correctly

2. **TestMuscleGroupSelection** - Tests muscle group selection
   - Selection by number (1-7)
   - Selection by name (abs, quads, glutes, etc.)
   - Invalid selection handling
   - Quit during selection

3. **TestWorkoutCommands** - Tests CLI commands
   - `list` - List exercises
   - `start` - Start workout
   - `help` - Display help
   - `license` - Display license
   - `quit` - Exit program
   - Invalid command handling

4. **TestWorkoutFlow** - Tests workout flow
   - Start → Next → End flow
   - Skip functionality
   - Stats command

5. **TestVideoFunctionality** - Tests video playback
   - Video command on different platforms

6. **TestWelcomeScreen** - Tests welcome screen
   - Welcome message display
   - Day recommendation

7. **TestIntegration** - Integration tests
   - Complete workout scenarios
   - Multiple muscle groups

8. **TestBugRegressions** - Regression tests for fixed bugs
   - Triceps `list` shows triceps (not glutes)
   - Percentage uses the correct `*100` formula
   - Five-exercise groups reach their last exercise
   - `stats` works after `skip`

### CLI Tests (`test_cli.py`)

- Argument parsing for every flag (`--group`, `--list`, `--history`,
  `--init-config`, `--config`, `--version`)
- Dispatch: no-args launches the REPL; flags run their action and exit

### Config Tests (`test_config.py`)

- Defaults load when no file exists
- Deep-merge applies partial overrides
- Malformed / non-object JSON falls back to defaults

### History Tests (`test_history.py`)

- `record_workout` appends and round-trips
- `format_history` summarises sessions
- Corrupt history files are treated as empty

## Running Tests

### Prerequisites

Install test dependencies:

```bash
pip install -r requirements.txt
```

This installs:
- pytest
- pytest-cov (coverage reporting)
- pytest-mock (mocking support)

### Running All Tests

Run all tests with coverage:

```bash
pytest tests/ -v
```

### Running Specific Test Files

Run main module tests:

```bash
pytest tests/test_main.py -v
```

Run a single module's tests (e.g. config):

```bash
pytest tests/test_config.py -v
```

### Running Specific Test Classes

```bash
pytest tests/test_main.py::TestMuscleGroupSelection -v
```

### Running Specific Tests

```bash
pytest tests/test_main.py::TestMuscleGroupSelection::test_abs_selection_by_number -v
```

## Coverage Reports

### Generate Coverage Report

```bash
pytest tests/ --cov=. --cov-report=term-missing
```

### Generate HTML Coverage Report

```bash
pytest tests/ --cov=. --cov-report=html
```

Then open `htmlcov/index.html` in your browser.

### Generate XML Coverage Report

```bash
pytest tests/ --cov=. --cov-report=xml
```

## Test Configuration

Test configuration is stored in `setup.cfg`:

```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --strict-markers
    --tb=short
    --cov=.
    --cov-report=term-missing
    --cov-report=html
    --cov-report=xml
    --cov-branch
```

## Continuous Integration

Tests are automatically run via GitHub Actions on:
- Push to `main` and `develop` branches
- Pull requests to `main` and `develop` branches

The workflow tests against multiple Python versions:
- Python 3.9
- Python 3.10
- Python 3.11
- Python 3.12

See `.github/workflows/tests.yml` for the full workflow configuration.

## Writing New Tests

When adding new tests, follow these guidelines:

1. **Naming Convention**
   - Test files: `test_*.py`
   - Test classes: `Test*`
   - Test functions: `test_*`

2. **Test Organization**
   - Group related tests in classes
   - Use descriptive test names
   - Add docstrings explaining what is being tested

3. **Mocking**
   - Use `@patch` for mocking input/output
   - Mock external dependencies (filesystem, network, etc.)

4. **Example Test**

```python
@patch('builtins.print')
@patch('builtins.input')
def test_abs_selection(mock_input, mock_print):
    """Test selecting abs muscle group."""
    mock_input.side_effect = ['abs', 'quit']
    
    with pytest.raises(SystemExit):
        main.workout()
    
    printed_output = [str(call) for call in mock_print.call_args_list]
    assert any('Ab muscle group selected' in str(call) for call in printed_output)
```

## Troubleshooting

### Import Errors

If you encounter import errors, ensure you're running tests from the project root:

```bash
cd /path/to/PyWorkout
pytest tests/
```

### Coverage Not Showing

Ensure pytest-cov is installed:

```bash
pip install pytest-cov
```

## Test Results

Current test coverage: ~78% overall (excluding the standalone, untested `gui.py`)
- Test suite: 53 tests passing across CLI, REPL, config, and history
- `gui.py` is an unfinished standalone prototype and is intentionally not tested

## Contributing

When contributing:
1. Write tests for new features
2. Ensure all tests pass before submitting PR
3. Aim for >80% code coverage for new code
4. Follow existing test patterns and conventions
