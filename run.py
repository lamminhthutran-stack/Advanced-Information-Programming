import argparse
import builtins
import contextlib
import runpy
import sys
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("script", help="Target Python script, e.g. main.py")
    parser.add_argument("--input", help="Text file containing input lines")
    parser.add_argument("--output", default="output_log.txt")
    parser.add_argument("--encoding", default="utf-8")
    return parser.parse_args()


class Tee:
    def __init__(self, terminal, log_file):
        self.terminal = terminal
        self.log_file = log_file
        self.counter = 0
        self.buf = ""

    def write(self, data):
        self.terminal.write(data)
        self.terminal.flush()
        self.buf += data
        while "\n" in self.buf:
            line, self.buf = self.buf.split("\n", 1)
            self.counter += 1
            self.log_file.write(f"[{self.counter}] {line}\n")
            self.log_file.flush()
        return len(data)

    def flush(self):
        self.terminal.flush()
        self.log_file.flush()


def main():
    args = parse_args()
    script_path = Path(args.script).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    input_log_path = Path("player_input.txt")
    using_input_log = bool(args.input)

    if not script_path.exists():
        raise FileNotFoundError(f"Script not found: {script_path}")

    original_input = builtins.input
    original_argv = sys.argv[:]
    input_lines_recorded = []

    if using_input_log:
        input_path = Path(args.input).expanduser().resolve()
        if not input_path.exists():
            raise FileNotFoundError(f"Input file not found: {input_path}")
        input_lines = input_path.read_text(encoding=args.encoding).splitlines()
        iterator = iter(input_lines)

        def logged_input(prompt=""):
            try:
                line = next(iterator)
            except StopIteration as exc:
                raise EOFError("No more lines in input file.") from exc
            input_lines_recorded.append(line)
            print(f"{prompt}{line}")
            return line
    else:
        def logged_input(prompt=""):
            line = original_input(prompt)
            input_lines_recorded.append(line)
            return line

    builtins.input = logged_input
    sys.argv = [str(script_path)]

    try:
        with output_path.open("w", encoding=args.encoding, newline="") as log_file:
            tee = Tee(sys.stdout, log_file)
            with contextlib.redirect_stdout(tee):
                try:
                    runpy.run_path(str(script_path), run_name="__main__")
                except EOFError:
                    if using_input_log:
                        print("EOF reached: input file does not contain enough lines.")
                    else:
                        raise
    finally:
        builtins.input = original_input
        sys.argv = original_argv

    with input_log_path.open("w", encoding=args.encoding) as f:
        for i, line in enumerate(input_lines_recorded, 1):
            f.write(f"[{i}] {line}\n")


if __name__ == "__main__":
    main()