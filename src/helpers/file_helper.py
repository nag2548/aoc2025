from pathlib import Path


def read_file_as_list(filename: str) -> list[str]:
    return read(filename, lambda f: f.read().splitlines())


def read_file_as_string(filename: str) -> str:
    return read(filename, lambda f: f.read())


def read(filename: str, mapper):
    input_path = Path(__file__).parent.parent.parent / "inputs" / filename
    with open(input_path, "r", encoding="utf-8") as f:
        return mapper(f)
