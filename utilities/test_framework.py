"""Object of this framework is to make the test automatic and warn me that the resulting real run
does not produce a correct answer.
"""
from enum import Enum
import os
import io
import re
# import typing as t
from colorama import Fore
from collections import defaultdict
from collections.abc import Callable
from contextlib import redirect_stdout
from .alias_type import Mode

class Star(Enum):
    SILVER = "silver"
    GOLD = "gold"

def test(fun: Callable[[Mode, str], None], file_name: str, *expected_results: list[tuple[int | None, int | None]]):
    if len(expected_results) == 0:
        print("No expected_results was given: No test")
        return

    year, day = re.findall(r"\d+", file_name)

    dir = f"/home/totti/Advent_of_code/{year}/data"
    base_file = f"day{day}_test"
    all_files = os.listdir(dir)
    test_files = [file for file in all_files if file.startswith(base_file)]

    # Filter out empty test files
    test_files = [file for file in test_files if os.stat(f"{dir}/{file}").st_size]
    test_results = defaultdict(lambda: dict())
    # As the main function does not output anything other than prints, let's capture those
    tested, passed, failed = 0, 0, 0
    for test_file in test_files:
        test_name = test_file.split("_")[1]
        if not test_name[-1].isdigit():
            result_idx = 0
        else:
            result_idx = int(re.findall(r'\d+', test_name)[0]) - 1

        expected_value, expected_gold = expected_results[result_idx]
        if expected_value is None and expected_gold is not None:
            mode_type = "gold"
        elif expected_value is not None and expected_gold is None:
            mode_type = "silver"
        elif expected_value is not None and expected_gold is not None:
            mode_type = "both"
        else:
            assert False, "Both expected results can't be 'None'!"
        writer = io.StringIO()
        with redirect_stdout(writer):
            fun(mode=mode_type, data_type=test_name)
        output = writer.getvalue()

        test_results[test_name]["tests"] = 2 if mode_type == "both" else 1
        current_pass_count = 0
        for expected_value, star in zip(expected_results[result_idx], [Star.SILVER, Star.GOLD]):
            if expected_value is None:
                continue
            tested += 1
            value = re.search(fr'{star.value}\s?=\s?(\d+)', output)
            if value is not None:
                value = int(value.groups()[0])
                if value != expected_value:
                    test_results[test_name][star] = (False, f"Expected = {expected_value}, Got = {value}")
                    failed += 1
                else:
                    test_results[test_name][star] = (True, "Passed!")
                    passed += 1
                    current_pass_count += 1
            else:
                test_results[test_name][star] = (False, "Result not found!")
                failed += 1

        test_results[test_name]["passes"] = current_pass_count

    if not failed and tested == passed:
        print(Fore.GREEN + f"All tests ({tested}) passed!" + Fore.RESET)
    else:
        print(f"All tests: {tested}")
        print(Fore.RED + f"{failed} test(s) failed" + Fore.RESET)
        print(Fore.GREEN + f"{passed} test(s) passed" + Fore.RESET)

        for name, tests in test_results.items():
            if tests["passes"] == 0:
                print(Fore.RED, end="")
            elif tests["passes"] == 1 and tests["tests"] == 2:
                print(Fore.YELLOW, end="")
            elif tests["passes"] == 1 and tests["tests"] == 1:
                print(Fore.GREEN, end="")
            elif tests["passes"] == 2:
                print(Fore.GREEN, end="")

            print(f"\n{name}:" + Fore.RESET)
            for star, results in tests.items():
                if star in ["passes", "tests"]:
                    continue
                (passed, text) = results
                if star == Star.SILVER:
                    print(Fore.LIGHTWHITE_EX + "\tSilver: " + Fore.RESET, end="")
                else:
                    print(Fore.LIGHTYELLOW_EX + "\tGold:   " + Fore.RESET, end="")

                if passed:
                    mark = Fore.GREEN + '\N{check mark}' + Fore.RESET
                    color = Fore.GREEN
                else:
                    mark = "\N{cross mark}"
                    color = Fore.LIGHTRED_EX
                print(f"{mark} " + color + text + Fore.RESET)
