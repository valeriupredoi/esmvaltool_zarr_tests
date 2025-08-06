import iris
import xarray as xr
import ncdata
import ncdata.iris_xarray
### imports need about 285M
import zarr


z = zarr.open('https://uor-aces-o.s3-ext.jc.rl.ac.uk/esmvaltool-zarr/pr_Amon_CNRM-ESM2-1_02Kpd-11_r1i1p2f2_gr_200601-220112.zarr3')
ds = z["pr"]
print("Zarr chunks", ds.chunks)
print("Number of chunks", ds.nchunks)


def load_small_file():
    zarr_path = (
        "https://uor-aces-o.s3-ext.jc.rl.ac.uk/"
        "esmvaltool-zarr/pr_Amon_CNRM-ESM2-1_02Kpd-11_r1i1p2f2_gr_200601-220112.zarr3"
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
    ### API2: 1GB memory (- 320MB = 680MB effective); 8.5s

    assert isinstance(cubes, iris.cube.CubeList)
    assert len(cubes) == 1
    assert cubes[0].has_lazy_data()
    # d = cubes[0].data
    print((cubes[0].data.size / 2**30) * 8)

load_small_file()
