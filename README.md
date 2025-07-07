# Rainy Day Algorithms: Python
This repository contains solutions for coding practice problems. Additionally, you 
will find some unit tests to accompany the solutions.

# Setup
This project uses Python. If you don't have Python already installed on your machine, you will need to do that.
Setup varies depending on if you have a Mac or PC, but you can get information on how to do this setup with a 
quick web search.

# Unit Testing
For unit testing, this project uses `unittest`.

## Unit Testing in Visual Studio Code
1. Open the Test Explorer (the flask icon on the left menu)
2. Select Configure Python Tests
3. Select `unittest`
4. When prompted, select the directory containing tests (`rainyday`)
5. When prompted, choose the pattern to identify test files (`test_*.py`)

Here is what your `settings.json` file should look:
```
{
  "python.testing.unittestArgs": [
    "-v",
    "-s",
    "./rainyday",
    "-p",
    "test_*.py"
  ],
  "python.testing.pytestEnabled": false,
  "python.testing.unittestEnabled": true
}
```

After you enter these settings, if you need to make any changes, you can do them in `.vscode/settings.json`.

Once you are ready, go to the Test Explorer to run the tests.