# PyWorkout — Installation

PyWorkout runs on Windows, macOS, and Linux. There are four ways to install it; pick whichever suits you.

| Method | Needs Python | Best for |
| --- | --- | --- |
| [`pip`](#python-package-index-pip) | Yes | Most people |
| [Executable](#executable-package) | No | Windows users who do not want to install Python |
| [Source](#from-source) | Yes | Trying changes or contributing |
| [Docker](#docker-container) | No | Running in a container |

## Python Package Index (`pip`)

1. Install [Python](https://www.python.org/downloads/) 3.9 or newer.
2. Install PyWorkout:

   ```bash
   pip install pyworkout
   ```

3. Run it:

   ```bash
   pyworkout
   ```

## Executable Package

No Python needed — everything is bundled.

1. Download the latest `.zip` from [Releases](https://github.com/willtheorangeguy/PyWorkout/releases/latest).
2. Extract it with [7-Zip](https://www.7-zip.org/) or Windows Explorer.
3. *(Optional)* Move the folder to `C:\Program Files` and make a shortcut.
4. Run `PyWorkout.exe`.

## From Source

1. Install [Python](https://www.python.org/downloads/) 3.9 or newer and [Git](https://git-scm.com/downloads).
2. Clone and run:

   ```bash
   git clone https://github.com/willtheorangeguy/PyWorkout
   cd PyWorkout
   python main.py
   ```

No `pip install` step is required — PyWorkout uses only the standard library.

If you would rather not use Git, download the source archive from [Releases](https://github.com/willtheorangeguy/PyWorkout/releases/latest) and run `python main.py` inside the extracted folder.

## Docker Container

1. Install [Docker](https://www.docker.com/products/docker-desktop/).
2. Pull the image from GitHub Packages:

   ```bash
   docker pull ghcr.io/willtheorangeguy/pyworkout:main
   ```

3. Run it interactively — `-i -t` matters, because PyWorkout reads commands from stdin:

   ```bash
   docker run -i -t ghcr.io/willtheorangeguy/pyworkout:main python main.py
   ```

The `video` command will not work inside a container, since it has no access to your local video files or a media player.

## Next Steps

Head to [Usage](usage.md) to run your first workout, or [Configuration](configuration.md) to make it yours.
