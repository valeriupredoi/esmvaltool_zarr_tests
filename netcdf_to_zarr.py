import xarray as xr
import netCDF4

# file = "/home/valeriu/pr_Amon_CNRM-ESM2-1_02Kpd-11_r1i1p2f2_gr_200601-220112.nc"
file = "/home/valeriu/cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2_gn_205001-209912.nc"

import iris

cubes = iris.load(file)
print(cubes)
for cube in cubes:
    if cube.standard_name == "cloud_area_fraction_in_atmosphere_layer":
        cube = cube[0:110]
        iris.save(cube, "/home/valeriu/cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2.nc")

file = "/home/valeriu/cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2.nc"

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
    print("Xarray Dataset Chunks\n", nc_xr["cl"].chunksizes)

    ds = netCDF4.Dataset(file)
    print("netCDF4 Dataset Chunks\n", ds["cl"].chunking())

    return nc_xr


ds = convert_to_zarr(file)
ds.to_zarr("~/cl_Amon_UKESM1-0-LL_ssp370SST-lowNTCF_r1i1p1f2.zarr3")

