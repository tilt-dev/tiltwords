# tiltwords

Hook your Tilt instance into [Cursewords](https://github.com/thisisparker/cursewords) by Parker Higgins: solve crossword puzzles on your terminal, but only when none of your builds are red!

## How to use
1. pull this repo down
2. `pip install -r requirements.txt`
3. maybe you need to `cd cursewords/tilt/gen; pip install -e .`? Unclear.
4. in `cursewords/tilt/status_checker.py`, make sure `CONFIG_PATH` points to your Tilt API config (will live at `~/.windmill/config` or `~/.tilt/config` or `~/.tilt-dev/config`)
5. in another window, start Tilt with whatever project you want
6. invoke Tiltwords with: `python cursewords/__main__.py test.puz` (or a `.puz` file of your choice; you can find some here: http://code.maiamccormick.com/crosswords/)
7. enjoy this additional motivation to fix your builds! 


