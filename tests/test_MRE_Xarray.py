import xarray as xr

from xarray.backends.common import WritableCFDataStore


def encode_zarr_file():
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

    variables = zarr_xr.variables
    dts = WritableCFDataStore()
    dts.encode(variables, {})


encode_zarr_file()
