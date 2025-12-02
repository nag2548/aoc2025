import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

session = os.getenv("AOC_SESSION")

day = input("Enter the day: ")

response = requests.get(
    f"https://adventofcode.com/2025/day/{day}/input", cookies={"session": session}
)
open(Path(__file__).parent.parent / "inputs" / f"day{day}.txt", "wb").write(
    response.content
)
