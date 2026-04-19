from pathlib import Path

def next_magic_num(num_str: str) -> str:
    n = len(num_str)

    if set(num_str) == {"9"}:
        return "1" + ("0" * (n - 1)) + "1"

    def mirror(left, middle, odd):
        if odd:
            return left + middle + left[::-1]
        return left + left[::-1]

    half = n // 2
    odd = n % 2

    left = num_str[:half]
    middle = num_str[half:half + odd]

    candidate = mirror(left, middle, odd)

    if candidate > num_str:
        return candidate

    if odd:
        new_center = str(int(left + middle) + 1)
        new_left = new_center[:-1]
        new_middle = new_center[-1]
    else:
        new_center = str(int(left) + 1)
        new_left = new_center
        new_middle = ""

    if len(new_left) > len(left):
        return "1" + ("0" * (n - 1)) + "1"

    return mirror(new_left, new_middle, odd)


def main():
    data = Path("magic_numbers/input.txt").read_text(encoding="utf-8").strip()

    numbers = data.split()

    results = []
    for num in numbers:
        results.append(next_magic_num(num))

    print("\n".join(results))


if __name__ == "__main__":
    main()
