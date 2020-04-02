# Archive for Morphy releases.

## Obtaining all the source code.
Install the repo tool (https://source.android.com/setup/develop)

Run the following commands to obtain all of the source from master
```
repo init -u https://github.com/mbrazeau/morphyManifest
repo sync
```
### If you don't have or don't want repo:
Or if you just want the latest 'bleeding edge' development version,
you can run the `getdev.py` script to clone all the current
development branches.

Clone the morphy.archive repository, then navigate into the folder
and run

`python getdev.py`

To get the latest commits run

`python getdev.py update`

## Building Morphy
You should have python and CMake installed.

From inside the `build` directory, run `python build.py --release`. 

The Morphy executable should be in the `install/bin` folder.
