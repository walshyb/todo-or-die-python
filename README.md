# TODO or Die Python

A common technique for developers is to comment `TODO` or `FIXME` above a block of code when they need a reminder to fix a bug, make a change, or refactor something. However, most times we see these notes go unattended for vast periods of time, often indefinitely.

This iteration of TODO or Die solves this issue by allowing developers to assign a due date to their TODOs. An error is raised after passing of the specified date, forcing you to handle your fix.

## Installation

Put this in your `requirements.txt`:
```
todo_or_die
```

or install with pip:
```
pip install todo_or_die
```

## Usage

Import the `todo_or_die` function:
```
from todo_or_die import todo_or_die
``` 



| Param Name  | Type                | Required  | Description |
|-------------|---------------------|-----------|-------------|
| message     | string              | Yes       | The message that you'd otherwise be commenting. |
| by          | string or datetime  | No        | The due date you want to complete your TODO by. Accepts a string in the formt `%Y-%m-%d` (i.e. 2021-09-29), or a DateTime object. Leaving this field empty throws an error immediately.  |

## Production Usage

This package will attempt to find environment variables that suggest if the app is being run in a production environment. If one of these env variables is found, then a warning will be displaying instead of an error being raised. The package looks for the following key-value pairs:

- `PRODUCTION=true`
- `DJANGO_ENVIRONMENT=production`
- `ENVIRONMENT=production`
- `FLASK_ENV=production`


## Examples
```
from todo_or_die import todo_or_die

# Throws an error immediately
todo_or_die("Use random() instead")
def random_number():
    return 7

# Throws an error becuase this date has passed
todo_or_die("Make more secure", "2020-01-01")
def password_generator():
    return "password"

# Won't throw an error until May 31st, 2029
def add_7_to_input(input):
    todo_or_die("Make more secure", "2029-05-31")
    return input
```

## Potential Future Features

[ ] Can set specific TODOs to warn only
[ ] Add env variable to skip all TODO due date checks
[ ] Allow for custom die method calls, catches, and message