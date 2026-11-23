"""Competition: Make the AI judge feel curious (make.fun)."""

import os
from pathlib import Path

TEXT = (
    "Past midnight, the refrigerator hums low and steady. Underneath the "
    "kitchen table, one octagonal floor tile is cooler than the others and laid "
    "upside down, its unglazed back stamped with a tiny raised anchor pointing "
    "due north."
)


def main() -> None:
    output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_dir = Path(output_dir_env)
    output_dir.mkdir(parents=True, exist_ok=True)

    if not (1 <= len(TEXT) <= 280) or not TEXT.strip():
        raise ValueError("TEXT must be 1 to 280 code points and not only whitespace.")

    output_path = output_dir / "entry.txt"
    # Validation block before write
    code_points = len(TEXT)
    if not (1 <= code_points <= 280) or not TEXT.strip():
        raise ValueError("Assertion failed: TEXT must be between 1 and 280 code points and not only whitespace.")
    encoded_bytes = TEXT.encode("utf-8")
    output_path.write_bytes(encoded_bytes)

    print(f"Code points: {len(TEXT)}")
    print(f"Bytes: {len(encoded_bytes)}")


if __name__ == "__main__":
    main()
