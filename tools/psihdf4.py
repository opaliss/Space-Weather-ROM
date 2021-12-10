import numpy as np
from pyhdf.SD import *

def rdhdf(hdf_filename):
    """
    Read an HDF4 file and return the scales and data values.

    str: hdf_filename
        HDF4 filename.

    tuple:
        List of scale and data values.
    """
    x = np.array([])
    y = np.array([])
    z = np.array([])
    f = np.array([])

    # Open the HDF file
    sd_id = SD(hdf_filename)

    #Read dataset.  In all PSI hdf4 files, the 
    #data is stored in "Data-Set-2":
    sds_id = sd_id.select('Data-Set-2')
    f = sds_id.get()
    
    #Get number of dimensions:
    ndims = np.ndim(f)
    
    #Get the scales:
    for i in range(0,ndims):
        dim = sds_id.dim(i)
        if i == 0:
            x = dim.getscale()
        elif i == 1:
            y = dim.getscale()
        elif i == 2: 
            z = dim.getscale()

    sd_id.end()

    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    f = np.array(f) 

    return (x,y,z,f)

def rdhdf_1d(hdf_filename):

    x,y,z,f = rdhdf(hdf_filename)

    return (x,f)

def rdhdf_2d(hdf_filename):

    x,y,z,f = rdhdf(hdf_filename)

    return (y,x,f)

def rdhdf_3d(hdf_filename):

    x,y,z,f = rdhdf(hdf_filename)

    return (z,y,x,f)


def wrhdf(hdf_filename, x, y, z, f):
    """
    Write an HDF4 file. x, y, and z are the scales. f is the data.

    str: hdf_filename
        HDF4 filename.

    """

    # Create an HDF file
    sd_id = SD(hdf_filename, SDC.WRITE | SDC.CREATE | SDC.TRUNC)

    if f.dtype == np.float32:
        ftype = SDC.FLOAT32
    elif f.dtype == np.float64:
        ftype = SDC.FLOAT64

    # Create the dataset (Data-Set-2 is the name used by the psi data)).
    sds_id = sd_id.create("Data-Set-2", ftype, f.shape)

    #Get number of dimensions:
    ndims = np.ndim(f)

    #Set the scales:
    for i in range(0,ndims):
        dim = sds_id.dim(i)
        if i == 0:
            if x.dtype == np.float32:
                stype = SDC.FLOAT32
            elif x.dtype == np.float64:
                stype = SDC.FLOAT64
            dim.setscale(stype,x)
        elif i == 1:
            if y.dtype == np.float32:
                stype = SDC.FLOAT32
            elif y.dtype == np.float64:
                stype = SDC.FLOAT64
            dim.setscale(stype,y)
        elif i == 2: 
            if z.dtype == np.float32:
                stype = SDC.FLOAT32
            elif z.dtype == np.float64:
                stype = SDC.FLOAT64
            dim.setscale(stype,z)

    # Write the data:
    sds_id.set(f)

    # Close the dataset:
    sds_id.endaccess()

    # Flush and close the HDF file:
    sd_id.end()


def wrhdf_1d(hdf_filename,x,f):

    x = np.asarray(x)
    y = np.array([])
    z = np.array([])
    f = np.asarray(f)
    wrhdf(hdf_filename,x,y,z,f)


def wrhdf_2d(hdf_filename,x,y,f):

    x = np.asarray(x)
    y = np.asarray(y)
    z = np.array([])
    f = np.asarray(f)
    wrhdf(hdf_filename,y,x,z,f)


def wrhdf_3d(hdf_filename,x,y,z,f):

    x = np.asarray(x)
    y = np.asarray(y)
    z = np.asarray(z)
    f = np.asarray(f)
    wrhdf(hdf_filename,z,y,x,f)



