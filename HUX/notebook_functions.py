import numpy as np
import astropy.units as u


def convert_from_x_to_v(X_ROM, r, p, m, b, shift_function, method="cce"):
    V_ROM = np.zeros(X_ROM.shape)
    V_ROM[:, 0] = X_ROM[:, 0]
    for jj in range(1, len(r)):
        # find shift based on linear fit.
        shift = shift_function(r[jj].to(u.AU).value, r_idx=jj, m=m, b=b, method=method)
        # interpolate over shifted coords.
        V_ROM[:, jj] = np.interp(p - shift*(np.pi/180), p, X_ROM[:, jj], period=2*np.pi)
    return V_ROM


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

