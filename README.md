## Testing performance of Zarr support in ESMValTool


This is a follow-up from the initial PR where we include Zarr support in ESMValTool,
https://github.com/ESMValGroup/ESMValCore/pull/2785 and contains a number of tests that
are useful to understanding performance of Zarr/ncdata/Iris and ESMValTool.

Run these tests in a modern ``esmvaltool`` conda environment.