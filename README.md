# test-task-adaptiq

# Setup

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/) of version >= 0.5.24
- Create virtual environment and install dependencies:
    ```
    uv venv
    source .venv/bin/activate
    uv sync
    ```

# Tests run

- UI tests run cmd [Chrome Browser is required to be installed]
    ```
        pytest --rootdir=saucedemo saucedemo/tests
    ```
- API test
    ```
        pytest --rootdir=airport_service airport_service/tests
    ```