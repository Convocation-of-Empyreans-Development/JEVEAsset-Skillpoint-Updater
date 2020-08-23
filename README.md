## JEVEAsset skillpoint updater

This tool is used to backfill a character's JEVEAsset data with approximated values for their skillpoints.
JEVEAsset recently added functionality for tracking SP, so data collected before the change
 has SP set to zero. To fix this, we estimate the character's SP value at those points in time, and rewrite the data
 file with the new values.
 
This application is built with Python 3.8 and [PyInstaller](https://www.pyinstaller.org).

### Usage

The tool takes three required arguments:

| Short | Long          | Description                                           |
|-------|---------------|-------------------------------------------------------|
| -f    | --file        | Path to JEVEAsset data file (JSON)                    |
| -c    | --character   | The character name for which data is to be backfilled |
| -s    | --starting-sp | The starting amount of skillpoints for the character  |

(Running the program with no arguments will also display this in your terminal.)

The tool will write a new file, updated_{filename}.json, in the same directory as the given file, for safety reasons.
You will have to import this data into JEVEAsset manually. Your original data file will not be modified.