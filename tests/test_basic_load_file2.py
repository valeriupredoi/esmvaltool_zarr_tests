import iris
import xarray as xr
import ncdata
import ncdata.iris_xarray
### imports to here need about 285M
import zarr

z = zarr.open('https://uor-aces-o.s3-ext.jc.rl.ac.uk/esmvaltool-zarr/cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2.zarr3')
ds = z["cl"]
print("Zarr chunks", ds.chunks)
print("Number of chunks", ds.nchunks)


def load_small_file():
    # file is about 500MB compressed Zarr3
    zarr_path = (
        "https://uor-aces-o.s3-ext.jc.rl.ac.uk/"
        "esmvaltool-zarr/cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2.zarr3"
    )

    time_coder = xr.coders.CFDatetimeCoder(use_cftime=True)
    zarr_xr = xr.open_dataset(
        zarr_path,
        consolidated=True,
        decode_times=time_coder,
        engine="zarr",
        backend_kwargs={},
    )
    ### API1: 320MB memory (- 285M = 35MB effective); 1.5s

    conversion_func = ncdata.iris_xarray.cubes_from_xarray
    cubes = conversion_func(zarr_xr)
    ### API2: 2.4GB memory (- 320MB = 2,100MB effective); 8.5s

    assert isinstance(cubes, iris.cube.CubeList)
    assert len(cubes) == 2
    assert cubes[0].has_lazy_data()
    print(cubes[0])
    print(cubes[1])
    print((cubes[0].data.size / 2**30) * 8)
    print((cubes[1].data.size / 2**30) * 8)

load_small_file()
# cubes data sizes in GB:
# 1.9260406494140625
# 0.00020599365234375
