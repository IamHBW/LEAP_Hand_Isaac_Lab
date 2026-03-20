# Repository Guidelines

## Project Structure & Module Organization
Root-level docs live in `README.md`, while runnable entrypoints are under `scripts/`. Use `scripts/rl_games/` for training and checkpoint playback, and `scripts/rsl_rl/` only when working on the alternate trainer. The installable package is `source/LEAP_Isaaclab/LEAP_Isaaclab`: `tasks/` defines environments, `assets/` stores USD and hand assets, `deployment_scripts/` contains sim-to-real runners, and `utils/` holds shared helpers. Keep generated artifacts out of reviews; `logs/`, `outputs/`, and `wandb/` are runtime output, not source.

## Build, Test, and Development Commands
Activate the `LEAP_Hand` conda environment before running any Python command in this repository:

```bash
conda activate LEAP_Hand
python -m pip install -e source/LEAP_Isaaclab
python scripts/list_envs.py
python scripts/rl_games/train.py --task Isaac-Reorient-Cube-Leap --headless
python scripts/rl_games/play.py --task Isaac-Reorient-Cube-Leap --num_envs 1 --use_last_checkpoint
pre-commit run --all-files
pyright
```

`list_envs.py` confirms task registration, `train.py` is the main smoke test, and `play.py` is the quickest checkpoint validation pass.

## Coding Style & Naming Conventions
Use Python 3.10, 4-space indentation, and Black formatting with a 120-character line limit. Imports are sorted with `isort --profile black`; linting uses `flake8`, `pyupgrade`, and `codespell` through pre-commit. Follow the existing naming pattern: packages and config roots keep the repository's `LEAP_Isaaclab` casing, while module files, functions, and config keys use `snake_case`.

## Testing Guidelines
This repository does not currently ship a `tests/` suite, so every code change needs a focused smoke test. At minimum, run `pre-commit run --all-files`, then execute the affected workflow: training changes should launch `scripts/rl_games/train.py`, inference changes should run `scripts/rl_games/play.py`, and deployment changes should be validated from `source/LEAP_Isaaclab/LEAP_Isaaclab/deployment_scripts/`. When adding tests later, place them in a top-level `tests/` package and name files `test_<feature>.py`.

## Commit & Pull Request Guidelines
Recent history uses short, imperative subjects such as `Added camera cfg` and `Adjusted training params`. Keep commits focused, use one-line subjects in that style, and separate formatting-only changes from behavior changes. PRs should explain the scenario changed, list verification commands, link any related issue, and include screenshots or videos for environment, rendering, or sim-to-real behavior changes.

## Configuration & Asset Notes
Package metadata lives in `source/LEAP_Isaaclab/config/extension.toml`. Avoid committing large binary asset edits, trained checkpoints, logs, or local experiment outputs unless the PR is explicitly about those files.
