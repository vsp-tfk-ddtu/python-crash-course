from typing import Any


# Handle exception in the function body the way that this script works without errors
def getter(d: dict[str, Any], key: str) -> Any:
    return d[key]


# Do not modify the code below
if __name__ == "__main__":
    d = {"a": 42}

    assert getter(d, "a") == 42 # There supposed to be ([str, Any], str) not (Any)
    assert getter(d, "senseoflife") is None # There supposed to be ([str, Any], str) not (Any)
