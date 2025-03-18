from typing import Callable


def hex_to_rgb(value: str) -> tuple[int, int, int, int]:
    # #ff0000
    if len(value) < 9:
        to_match = list(["0"] * (9 - len(value)))
        value = f'{value}{"".join(to_match)}'

    xtract_hex: Callable[[str], int] = lambda x: int(f"{x}", 16)
    return (
        xtract_hex(value[1:3]),
        xtract_hex(value[3:5]),
        xtract_hex(value[5:7]),
        xtract_hex(value[7:]),
    )
