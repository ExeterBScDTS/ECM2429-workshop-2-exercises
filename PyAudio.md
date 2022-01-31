# Installing PyAudio

Installing the PyAudio package for use with one of the latest versions of Python (3.9 or 3.10) is not quite as simple as the usual ```pip install PyAudio```.   So please follow these instructions.

## Installing on Windows

Installing in a virtual environment is recommended. e.g.

```sh
python -m venv .venv
```

To install on Windows 10 (or 11) you will need a pre-compiled *wheel*.  Installing a wheel is very simple, but first we need the correct wheel, which depends on the version of Python you are using.

For Python 3.9 use ```PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl```

For Python 3.10 use ```PyAudio‑0.2.11‑cp310‑cp310‑win_amd64.whl```

These files can be downloaded from <https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio>

The pip command to install a wheel is simply **pip install** *wheel-name*

```sh
pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl
```
or

```sh
pip install PyAudio‑0.2.11‑cp310‑cp310‑win_amd64.whl
```

## Installing on Mac

Installing in a virtual environment is recommended. e.g.

```sh
python -m venv .venv
```

(from <http://people.csail.mit.edu/hubert/pyaudio/>)

 Use Homebrew to install the prerequisite portaudio library, then install PyAudio using pip:

    brew install portaudio
    pip install pyaudio 

Notes:

 * If not already installed, download [Homebrew](brew.sh).
 * pip will download the PyAudio source and build it for your version of Python.
 * Homebrew and building PyAudio also require installing the Command Line Tools for Xcode ([more information](https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Installation.md)).



