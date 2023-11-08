## langdt: timestamps from natural language

## What is langdt
langdt is a Python library designed for natural language processing of time-related text. It translates various expressions and phrases that describe time into machine-readable datetime objects. langdt can interpret phrases like "yesterday", "last month", "since last year", and many more, providing a convenient way to work with time expressions in a human-friendly manner.

## Features
- Converts natural language to `datetime` objects.
- Supports a wide range of time expressions.
- Handles both specific dates and relative timeframes.

## Installation

To install `langdt`, simply run:

```bash
pip install git+https://github.com/zozoheir/langdt.git@main
```

## Usage

Here are a few examples of how `langdt` can be used:

### Example 1: Yesterday

To get the datetime range for 'yesterday':

```python
from langdt import get_timeframe

start_time, end_time = get_timeframe("yesterday")
print(f"Start: {start_time}, End: {end_time}")
```

### Example 2: Last Month

To get the datetime range for 'last month':

```python
from langdt import get_timeframe

start_time, end_time = get_timeframe("last month")
print(f"Start: {start_time}, End: {end_time}")
```

### Example 3: Custom Range

To get the datetime range between two specific dates:

```python
from langdt import get_timeframe

start_time, end_time = get_timeframe("from 2022-01-01 to 2022-12-31")
print(f"Start: {start_time}, End: {end_time}")
```

## Contributions

Contributions are welcome! If you have an idea for an improvement or have found a bug, please open an issue or submit a pull request.

## License

`langdt` is released under the MIT License. See the LICENSE file for more details.