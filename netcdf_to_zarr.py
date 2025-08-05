import xarray as xr
import netCDF4

file = "/home/valeriu/pr_Amon_CNRM-ESM2-1_02Kpd-11_r1i1p2f2_gr_200601-220112.nc"

def convert_to_zarr(file):
    """
    Unchunked
    """
    nc_xr = xr.open_dataset(
        file,
        engine="netcdf4",
    )

    print(dir(nc_xr))
    print("Xarray Dataset\n", nc_xr)
    print("Xarray Dataset Encoding\n", nc_xr.encoding)
    print("Xarray Dataset Chunks\n", nc_xr["pr"].chunksizes)

    ds = netCDF4.Dataset(file)
    print("netCDF4 Dataset Chunks\n", ds["pr"].chunking())


convert_to_zarr(file)
