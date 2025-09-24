# .interpreter
import sys
from flux.core import FluxInterpreter
from pathlib import Path

def run(flux_file: str):
    path = Path(flux_file)
    code = path.read_text(encoding="utf-8")

    interp = FluxInterpreter()
    return interp.run(code)

def main():
    if len(sys.argv) < 2:
        print("Usage: python .interpreter <file.flux>")
        sys.exit(1)

    result = run(sys.argv[1])
    if result:
        for r in result:
            print(r)

if __name__ == "__main__":
    main()
