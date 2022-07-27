import numpy as np
import astropy.units as u
import matplotlib

def convert_from_x_to_v(X_ROM, p, r, m, b, shift_function):
    V_ROM = np.zeros(X_ROM.shape)
    V_ROM[:, 0] = X_ROM[:, 0]
    for jj in range(1, len(r)):
        # find shift based on linear fit.
        shift = shift_function(r[jj].to(u.AU).value, m=m, b=b)
        # interpolate over shifted coords.
        V_ROM[:, jj] = np.interp(p - shift*(np.pi/180), p, X_ROM[:, jj], period=2*np.pi)
    return V_ROM


def compute_phi_shift_forward(p, r, v, omega=2 * np.pi / 25.38, method=None):
    # initialize phi shift matrix.
    phi_shift_mat = np.zeros((len(r), len(p)))

    # phi at index 0 is original phi grid
    phi_shift_mat[0, :] = p

    # delta r.
    dr = np.mean(r[1:] - r[:-1])

    # compute the phi shift for each idx in r.
    for ii in range(len(r) - 1):
        if method == "ballistic":
            phi_shift = -(omega / v[:, 0]) * dr
        else:
            phi_shift = -(omega / v[:, ii]) * dr
        phi_shift_mat[ii + 1, :] = phi_shift_mat[ii, :] + phi_shift

    return phi_shift_mat

def cmap(p):
    # an array of parameters, each of our curves depend on a specific value of parameters.
    parameters = np.linspace(0,2*np.pi,len(p))
    # norm is a class which, when called, can normalize data into the [0.0, 1.0] interval.
    norm = matplotlib.colors.Normalize(vmin=np.min(parameters), vmax=np.max(parameters))
    # create a ScalarMappable and initialize a data structure
    arr = matplotlib.cm.ScalarMappable(cmap=matplotlib.cm.hsv, norm=norm)
    arr.set_array([])
    return arr

def cdf(data, ax, label, ls):
    data_size=len(data)
    # Set bins edges
    data_set=sorted(set(data))
    bins=np.append(data_set, data_set[-1]+1)
    # Use the histogram function to bin the data
    counts, bin_edges = np.histogram(data, bins=bins, density=False)
    counts=counts.astype(float)/data_size
    # Find the cdf
    cdf = np.cumsum(counts)
    # Plot the cdf
    ax.plot(bin_edges[:-1], cdf, ls=ls, label=label)

def regularizer(r, λ1, λ2):
    """Return the regularizer that penalizes all operator elements by λ1,
    except for the quadratic operator elements, which are penalized by λ2.
    Parameters
    ----------
    r : int
        Dimension of the ROM.
    λ1 : float
        Regularization hyperparameter for the non-quadratic operators.
    λ2 : float
        Regularization hyperparameter for the quadratic operator.

    Returns
    -------
    diag(𝚪) : (d,) ndarray
        Diagonal entries of the dxd regularizer 𝚪.
    """
    r1 = 1 + r
    r2 = r + r * (r + 1) // 2

    diag𝚪 = np.full(r2 + 1, λ1)
    diag𝚪[r1:-1] = λ2
    return diag𝚪