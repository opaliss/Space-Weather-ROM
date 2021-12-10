""" Read in MAS results from PSI (Predictive Science inc.) website"""
from pathlib import Path
from parfive import Downloader


def get_mas_path(cr, folder="hmi_mast_mas_std_0201"):
    """Get MAS website results.

    :param cr: carrington rotation. ex: 2210
    :return: mas_path
    """
    download_dir = Path.cwd() / '..' / '..' / 'data'
    
    cr_string = 'mas_helio/cr' + str(cr)
    mas_helio_dir = download_dir / cr_string 
    mas_helio_dir.mkdir(parents=True, exist_ok=True)

    base_url = 'http://www.predsci.com/data/runs/cr' + str(cr) + '-medium/' + folder + '/helio/{var}002.hdf'

    # Create a downloader to queue the files to be downloaded
    dl = Downloader()

    for var in ['rho', 'vr', 'br']:
        file = mas_helio_dir / f'{var}002.hdf'
        if file.exists():
            continue
        else:
            remote_file = base_url.format(var=var)
            dl.enqueue_file(remote_file, path=mas_helio_dir)

    # Download the files
    if dl.queued_downloads > 0:
        dl.download()
    return mas_helio_dir.resolve()