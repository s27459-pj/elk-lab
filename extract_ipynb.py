import json
import sys


def main() -> None:
    infile = sys.argv[1]
    outfile = sys.argv[2]

    with open(infile, "r") as f:
        data = json.load(f)

    cells = data["cells"]
    output = ""
    for cell in cells:
        if cell["cell_type"] != "code":
            continue

        source_lines = cell["source"]
        source = "".join(source_lines)
        output += f"# %%\n{source}\n\n"

    with open(outfile, "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
