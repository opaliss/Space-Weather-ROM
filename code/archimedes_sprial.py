import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import astropy.units as u


def compute_phi_shift_forward(p, r, v, omega=(2 * np.pi) / (25.38 * 86400)):
    # initialize phi shift matrix.
    phi_shift_vec = np.zeros(len(r))

    # phi at index 0 is original phi grid
    phi_shift_vec[0] = p

    # delta r.
    dr = np.mean(r[1:] - r[:-1])

    # compute the phi shift for each idx in r.
    for ii in range(0, len(r) - 1):
        phi_shift = -(omega / v) * dr
        phi_shift_vec[ii + 1] = phi_shift_vec[ii] + phi_shift

    return phi_shift_vec


def ballistic_approximation_ulysses(r0_vec, rf_vec, phi_vec, vr_initial, omega_rot=(2 * np.pi) / (25.38 * 86400)):
    res_ballistic_f = np.zeros(len(phi_vec))

    for ii in range(len(phi_vec)):
        # get current phi location.
        phi_location = phi_vec[ii].to(u.rad).value
        # corresponding r0 = 30rs.
        r0 = ((r0_vec[ii]).to(u.km)).value
        # final r location.
        rf = (rf_vec[ii].to(u.km)).value
        # vr0
        curr_velocity = vr_initial[ii].value
        # change in r.
        dr = rf - r0
        # change in phi.
        delta_phi = (omega_rot * dr) / curr_velocity
        # compute the phi shift
        phi_shifted = phi_location - delta_phi
        # force periodicity
        res_ballistic_f[ii] = phi_shifted % (2 * np.pi)

    return res_ballistic_f

def cmap_spiral(nphi):
    # an array of parameters, each of our curves depend on a specific value of parameters.
    parameters = np.linspace(0, 2*np.pi, nphi)
    # norm is a class which, when called, can normalize data into the [0.0, 1.0] interval.
    norm = mpl.colors.Normalize(vmin=np.min(parameters), vmax=np.max(parameters))
    # create a ScalarMappable and initialize a data structure
    arr = mpl.cm.ScalarMappable(cmap=mpl.cm.hsv, norm=norm)
    arr.set_array([])
    return arr