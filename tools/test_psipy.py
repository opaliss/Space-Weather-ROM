import matplotlib.pyplot as plt

from heliopy.data import psp
from heliopy.data import omni
from heliopy.data import solo

import heliopy.data.spice as spicedata
import heliopy.spice as spice
import heliopy.models
from scipy.interpolate import interpn
from astropy.coordinates import SkyCoord
from astropy.coordinates import SkyOffsetFrame
from cdasws import CdasWs
from psipy.model import MASOutput
import astropy.coordinates as astrocoords
from psipy.model.variable import Variable
from psipy.data import sample_data

import pyspedas
from pytplot import tplot

from pathlib import Path
from parfive import Downloader
import datetime as dt

test1 = False
test2 = True

if test1:
    # ======================================================================================================================
    # LOAD OMNI DATASET.
    # ======================================================================================================================

    starttime = dt.datetime(year=2018, month=10, day=26)
    endtime = dt.datetime(year=2018, month=11, day=23)

    omni_data = omni.h0_mrg1hr(starttime, endtime)
    # ======================================================================================================================
    # LOAD MAS RESULTS CR2210
    # ======================================================================================================================
    download_dir = Path(__file__).parent / '..' / '..' / 'data'

    # mas_path = sample_data.mas_helio()

    mas_helio_dir = download_dir / 'mas_helio'
    mas_helio_dir.mkdir(parents=True, exist_ok=True)
    base_url = 'http://www.predsci.com/data/runs/cr2210-medium/hmi_mast_mas_std_0201/helio/{var}002.hdf'

    # Create a downloader to queue the files to be downloaded
    dl = Downloader()

    vars = ['rho', 'vr', 'br']
    for var in vars:
        file = mas_helio_dir / f'{var}002.hdf'
        if file.exists():
            continue
        else:
            remote_file = base_url.format(var=var)
            dl.enqueue_file(remote_file, path=mas_helio_dir)

    # Download the files
    if dl.queued_downloads > 0:
        dl.download()
    mas_path = mas_helio_dir.resolve()

    model = MASOutput(mas_path)
    print(model.variables)

    vr_model = model['vr']

    print(vr_model)

    # ======================================================================================================================
    # Load PSP observations for CR2210
    # ======================================================================================================================
    starttime = '2018-10-26'
    endtime = '2018-11-23'
    psp_data = psp.merged_mag_plasma(starttime, endtime)


    print(psp_data.columns)

    times = psp_data.index

    spicedata.get_kernel('psp')
    spicedata.get_kernel('psp_pred')
    psp_traj = spice.Trajectory('SPP')
    psp_traj.generate_positions(times, 'Sun', 'IAU_SUN')
    psp_coords = psp_traj.coords

    vr_model = model['vr']
    vr_sampled = vr_model.sample_at_coords(psp_coords.lon,
                                           psp_coords.lat,
                                           psp_coords.radius)

    # ======================================================================================================================
    # Save HUX results as MHD results datatype
    # ======================================================================================================================
    import copy
    hux_model = copy.deepcopy(vr_model)
    print(hux_model)


# ======================================================================================================================
# Solar Orbiter (SOLO) data
# ======================================================================================================================
if test2:
    starttime = '2020-09-04 00:00:00'
    endtime = '2020-09-05 00:00:00'
    # example MAG-RTN-NORMAL or SWA-PAS-MOM
    solo_data = solo.download(starttime, endtime, 'SWA-PAS-MOM', 'L1')
