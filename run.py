import sys
import os

if len(sys.argv) < 2:
    print("사용법: python run.py main.py")
    sys.exit(1)

target = sys.argv[1]
log_dir = "."

input_lines = []
output_lines = []
counter = [1] 

original_input = __builtins__.__dict__["input"] if isinstance(__builtins__, dict) else getattr(__builtins__, "input")

def logged_input(prompt=""):
    if prompt:
        line = f"[{counter[0]}] {prompt}"
        output_lines.append(line)
        print(prompt, end="")
        counter[0] += 1

    val = original_input()

    
    line = f"[{counter[0]}] 입력: {val}"
    input_lines.append(f"[{counter[0]}] {val}")
    output_lines.append(line)
    counter[0] += 1

    return val

original_print = print

def logged_print(*args, **kwargs):
    text = " ".join(str(a) for a in args)
    line = f"[{counter[0]}] {text}"
    output_lines.append(line)
    counter[0] += 1
    original_print(*args, **kwargs)

import builtins
builtins.input = logged_input
builtins.print = logged_print

with open(target) as f:
    code = f.read()

try:
    exec(compile(code, target, "exec"), {"__name__": "__main__"})
finally:
    with open("player_input.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(input_lines))

    with open("game_output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    original_print("\n✓ player_input.txt 저장 완료")
    original_print("✓ game_output.txt 저장 완료")