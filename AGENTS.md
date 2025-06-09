# AGENTS Instructions for Codex

This repository contains short Python programs that demonstrate probability-related concepts.

## Code style
- Use Python 3.8 or newer.
- Format all Python files with `black --line-length 79`.
- Include module and function docstrings.
- Prefer type hints for function signatures when practical.

## Example guidelines
- Place new examples under `examples/` and keep them self-contained.
- Provide a brief explanation either at the top of the script or in `examples/README.md`.
- Ensure each script can run directly via `python examples/<script>.py`.

## Tests
- Use `pytest` for any tests. Run tests with `pytest -q` from the repository root.
- If tests cannot run due to missing dependencies or other environment limitations, state this in the PR testing section.

## Pull request instructions
- Summaries must cite the relevant file lines for any changes made.
- The testing section should show the `pytest` results or explain any limitations.
