# Argument Parsing with `getopt`

This example demonstrates how to handle **command-line arguments** in Python using the `getopt` module.

---

## What is Argument Parsing?

Argument parsing is the process of reading values passed to a script when it is executed from the command line.  
It allows developers to:
- Control program behavior without changing the source code.
- Pass dynamic values such as filenames, configuration options, or parameters.
- Create flexible and reusable scripts that can handle different use cases.

For example, instead of hardcoding a file path or username, you can pass them as arguments when running the script.

---

## Key Concepts in This Example

1. **Default Values**
   - The script starts by setting default values for `name` and `size`.
   - These can be overridden by passing arguments when running the script.

2. **Using `getopt.getopt`**
   - The function `getopt.getopt(sys.argv[1:], "n:s:", ["name=", "size="])` is used to parse options.
   - Here:
     - `"n:s:"` means the script expects `-n` (with a value) and `-s` (with a value).
     - `["name=", "size="]` means the script also accepts `--name` and `--size`.

3. **Looping Through Options**
   - The script iterates through parsed options:
     - `-n` or `--name` updates the `name` variable.
     - `-s` or `--size` updates the `size` variable (converted to integer).

4. **Additional Arguments**
   - Any values not matching the defined options are treated as **extra arguments** and printed separately.

5. **Accessing Script Name**
   - `sys.argv[0]` gives the script name itself.

---

## Example Usage

Run the script with:

```bash
python script.py -n Faiyaz -s 50 extra1 extra2
