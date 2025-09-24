# .interpreter (root of Flux project)
import sys
from flux import stdlib
from pathlib import Path

def transpile_to_python(code: str) -> str:
    """
    Minimal Flux -> Python transpiler:
      - 'fn' -> 'def'
      - 'let' -> assignment
    This is intentionally tiny; expand parser later.
    """
    lines = []
    for line in code.splitlines():
        # keep indent behavior: replace leading tabs with 4 spaces (optional)
        line = line.replace("\t", "    ")
        # fn -> def
        if line.strip().startswith("fn "):
            line = line.replace("fn ", "def ", 1)
        # let -> assignment
        if line.strip().startswith("let "):
            line = line.replace("let ", "", 1)
        lines.append(line)
    return "\n".join(lines)

def run(flux_file: str):
    path = Path(flux_file)
    if not path.exists():
        raise FileNotFoundError(f"Flux file not found: {flux_file}")

    flux_code = path.read_text(encoding="utf-8")
    py_code = transpile_to_python(flux_code)

    # Prepare environment: inject standard library exports
    env = {}
    # add builtins and stdlib
    env.update(stdlib.EXPORTS)
    # Provide a convenience 'std' namespace
    env["std"] = stdlib.EXPORTS

    # Execute the transpiled Python
    exec(compile(py_code, str(path), "exec"), env)

    # If main exists, call it
    if "main" in env and callable(env["main"]):
        return env["main"]()

def main():
    if len(sys.argv) < 2:
        print("Usage: python .interpreter <file.flux>")
        sys.exit(1)
    flux_file = sys.argv[1]
    result = run(flux_file)
    if result is not None:
        print(result)

if __name__ == "__main__":
    main()
