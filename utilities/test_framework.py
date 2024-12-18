"""Object of this framework is to make the test automatic and warn me that the resulting real run
does not produce a correct answer.
"""
from enum import Enum
import os
import io
import re
import functools
from time import perf_counter
from collections import defaultdict
from collections.abc import Callable
from contextlib import redirect_stdout
from .alias_type import Mode

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

class Star(Enum):
    SILVER = "silver"
    GOLD = "gold"


Testcase = tuple[int | None, int | None]
AoCFunc = Callable[[Mode, str], None]

def test(
    func: AoCFunc,
    file_name: str,
    expected_results: Testcase,
) -> None:
    year, day = re.findall(r"\d+", file_name)

    if len(expected_results) == 0:
        print(YELLOW + "WARNING: Any 'expected_results' was not given. No test ran!" + RESET)
        return

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
            func(mode=mode_type, data_type=test_name)
        output = writer.getvalue()

        test_results[test_name]["tests"] = 2 if mode_type == "both" else 1
        current_pass_count = 0
        for expected_value, star in zip(expected_results[result_idx], [Star.SILVER, Star.GOLD]):
            if expected_value is None:
                continue
            tested += 1
            # TODO Allow to use other input types. This checks only for ints
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
        print(GREEN + f"All tests ({tested}) passed!" + RESET)
    else:
        print(RED + f"{failed} test(s) failed" + RESET)
        print(GREEN + f"{passed} test(s) passed" + RESET)

        for name, tests in test_results.items():
            if tests["passes"] == 0:
                print(RED, end="")
            elif tests["passes"] == 1 and tests["tests"] == 2:
                print(YELLOW, end="")
            elif tests["passes"] == 1 and tests["tests"] == 1:
                print(GREEN, end="")
            elif tests["passes"] == 2:
                print(GREEN, end="")

            print(f"\n{name}:" + RESET)
            for star, results in tests.items():
                if star in ["passes", "tests"]:
                    continue
                (passed, text) = results
                if star == Star.SILVER:
                    print(RESET + "\tSilver: " + RESET, end="")
                else:
                    print(YELLOW + "\tGold:   " + RESET, end="")

                if passed:
                    mark = GREEN + '\N{check mark}' + RESET
                    color = GREEN
                else:
                    mark = "\N{cross mark}"
                    color = RED
                print(f"{mark} " + color + text + RESET)

def testable(
    file_name: str,
    *expected_results: Testcase,
    before: bool = False,
    after: bool = True,
):
    def empty_fun(func):
        @functools.wraps(func)
        def empty_wrapper(*args, **kwargs):
            func(*args, **kwargs)
        return empty_wrapper

    if not before and not after:
        print(YELLOW + "WARNING: 'before' and 'after' were both disabled. No tests ran!" + RESET)
        return empty_fun

    def decorator_tester(func):
        @functools.wraps(func)
        def wrapper_test(*args, **kwargs):
            if before:
                test(func, file_name, expected_results)
            func(*args, **kwargs)
            if after:
                test(func, file_name, expected_results)
        return wrapper_test
    return decorator_tester


def time_it(func: AoCFunc):
    @functools.wraps(func)
    def timer(*args, **kwargs):
        s = perf_counter()
        func(*args, **kwargs)
        e = perf_counter()
        print(f"Aika :{e-s:10.2f}")
    return timer
