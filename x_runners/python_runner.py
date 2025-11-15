import os
import inspect
import json


def get_input(filename="input.json"):
    """
    Reads input cases from a JSON file and returns them with proper typing.

    Returns:
        list[dict]: List of test cases with typed input and expected output
    """
    # Get the file path of the calling script
    caller_frame = inspect.stack()[1]
    caller_path = caller_frame.filename
    print(f"{caller_path=}")
    caller_dir = os.path.dirname(os.path.abspath(caller_path))
    print(f"{caller_dir=}")

    # Construct path to input.json
    input_path = os.path.join(caller_dir, "..", filename)
    print(f"{input_path=}")

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found at: {input_path}")

    with open(input_path, "r") as f:
        data = json.load(f)

    # Extract cases - they're already properly typed from JSON
    cases = data.get("cases", [])

    return cases
