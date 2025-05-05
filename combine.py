import os
import sys

ANSII_FG_GREEN = "\033[92m"
ANSII_FG_RED = "\033[91m"
ANSII_FG_CYAN = "\033[96m"
ANSII_FG_BLUE = "\033[94m"
ANSII_RESET = "\033[0m"


def errprint(*args, **kwargs):
    print(ANSII_FG_RED, *args, ANSII_RESET, file=sys.stderr, **kwargs)


def cleanup(data: str):
    # Filter to keep only printable characters and newlines
    printable_content = "".join(c for c in data if c.isprintable() or c == "\n")

    # NOTE: This is unnecessary since we switched to `pdftotext -layout ...` as it generates
    # much better output by default

    # # Remove lines with a few characters
    # lines = printable_content.splitlines()
    # lines = [str(line) for line in lines if len(line) > 2 or len(line) == 0]
    #
    # i = len(lines) - 1
    # while i >= 0:
    #     if i >= 2:
    #         prev_newline = lines[i - 1] == ""
    #         prev_prev_newline = lines[i - 2] == ""
    #         if prev_newline and prev_prev_newline:
    #             lines.pop(i)
    #     i -= 1
    #
    # filtered_content = "\n".join(lines)
    # return filtered_content

    return printable_content


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 combine.py <start_number> <end_number>", file=sys.stderr)
        print(
            "Combine all the text files into one, including the endpoints",
            file=sys.stderr,
        )
        print("Example: python3 combine.py 3 20", file=sys.stderr)
        return

    start = int(sys.argv[1])
    end = int(sys.argv[2])

    all_files = os.listdir("./txts/")
    all_files = sorted(all_files)

    files = dict()
    for file_path in all_files:
        parts = file_path.split("-", maxsplit=1)
        if len(parts) != 2:
            errprint(f"File {file_path} does not match the expected format")
            continue
        num, _ = parts
        num = int(num)
        files[num] = file_path

    for num in range(start, end + 1):
        if num not in files:
            errprint(f"File with number {num} is missing")
            continue

        file_path = files[num]
        with open(f"./txts/{file_path}", "r", encoding="utf-8", errors="ignore") as f:
            print(f"======================= {file_path} =======================")
            content = cleanup(f.read())
            print(content)
            print()
            print()
            print()


if __name__ == "__main__":
    main()
