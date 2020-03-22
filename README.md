## Archive for Morphy releases.

# Obtaining all the source code.
Install the repo tool (https://source.android.com/setup/develop)

Run the following commands to obtain all of the source from master
```
repo init -u https://github.com/mbrazeau/morphyManifest
repo sync
```

# Building Morphy
You should have python and CMake installed.

From inside the `build` directory, run `python build.py --release`. 

The Morphy executable should be in the `install/bin` folder.
