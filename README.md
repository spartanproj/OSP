# OSP

The pre-build package manager for NerdOS.

*Note: this is currently a work in progress.*

## Installation

There are two ways to install OSP.

### With a command

Installing OSP is easy.

Run this in a terminal:

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/spartanproj/OSP/main/install.sh)"
```

The script does not download a binary, but instead downloads the source code and then compiles it.

### From source

If you're planning to develop on OSP or scared that we'll install a virus or something, you can build OSP from source.

1. Clone the repository:
   ```shell
   git clone https://github.com/spartanproj/OSP
   ```
2. Install `nuitka`:
   ```shell
   pip install nuitka
   ```
3. Build using Nuitka.
   ```shell
   python3 -m nuitka --standalone|--onefile <path/to/main.py>
   ```
   Note: using `--standalone` compiles a binary in `main.dist` and the libraries in `main.build`, requiring them both. Using `--onefile` allows you to have one file, `main.bin`, but is slower as it has to unarchive the libraries into your temporary folder. The script uses the `--standalone` parameter for performance.

4. Move the file(s) to your desired location.

## Developer Notes/Make a package/To-do list/Lorenzo's icons/User manual

See the wiki [here](https://github.com/spartanproj/OSP/wiki)!