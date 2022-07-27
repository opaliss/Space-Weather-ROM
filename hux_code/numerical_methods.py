""" Numerical methods other than the 1st order upwind scheme. """

import numpy as np


def apply_numerical_method(r_initial, dr_vec, dp_vec, r0=30 * 695700, alpha=0.15, rh=50 * 695700, add_v_acc=True,
                           omega_rot=(2 * np.pi) / (25.38 * 86400), numerical_method="upwind_first_maccormack",
                           flux_function="vanleer"):
    """Apply a numerical method to solve the solar wind problem.
    r/phi grid. return and save all radial velocity slices.

    :param r_initial: 1d array, initial condition (vr0). units = (km/sec).
    :param dr_vec: 1d array, mesh spacing in r. units = (km)
    :param dp_vec: 1d array, mesh spacing in p. units = (radians)
    :param alpha: float, hyper parameter for acceleration (default = 0.15).
    :param rh: float, hyper parameter for acceleration (default r=50*695700). units: (km)
    :param r0: float, initial radial location. units = (km).
    :param add_v_acc: bool, True will add acceleration boost.
    :param omega_rot: differential rotation.
    :param numerical_method: specify the numerical method used (str).
    :param flux_function: a flux-limiter function for high-low res solutions.
    :return: velocity matrix dimensions (nr x np)
    """
    v = np.zeros((len(dr_vec) + 1, len(dp_vec) + 1))  # initialize array vr.
    v[0, :] = r_initial

    if add_v_acc:
        v_acc = alpha * (v[0, :] * (1 - np.exp(-r0 / rh)))
        v[0, :] = v_acc + v[0, :]

    for i in range(len(dr_vec)):
        for j in range(len(dp_vec) + 1):

            if j == len(dp_vec):  # force periodicity
                v[i + 1, j] = v[i + 1, 0]

            else:
                if (omega_rot * dr_vec[i]) / (dp_vec[j] * v[i, j]) > 1:
                    print(dr_vec[i] - dp_vec[j] * v[i, j] / omega_rot)
                    print(i, j)  # courant condition

                elif numerical_method == "second_order_upwind":
                    if j == len(dp_vec) - 1:
                        frac1 = (4 * v[i, j + 1] - 3 * v[i, j] - v[i, -1]) / (v[i, j])
                    else:
                        frac1 = (4 * v[i, j + 1] - 3 * v[i, j] - v[i, j + 2]) / (v[i, j])
                    frac2 = (omega_rot * dr_vec[i]) / (2 * dp_vec[j])
                    v[i + 1, j] = v[i, j] + frac1 * frac2

                elif numerical_method == "second_order_upwind_conservative":
                    if j == len(dp_vec) - 1:
                        frac1 = (4 * np.log(v[i, j + 1]) - 3 * np.log(v[i, j]) - np.log(v[i, -1]))
                    else:
                        frac1 = (4 * np.log(v[i, j + 1]) - 3 * np.log(v[i, j]) - np.log(v[i, j + 2]))
                    frac2 = (omega_rot * dr_vec[i]) / (2 * dp_vec[j])
                    v[i + 1, j] = v[i, j] + frac1 * frac2

                elif numerical_method == "third_order_upwind":
                    if j == len(dp_vec) - 1:
                        frac1 = (-v[i, -2] + 6 * v[i, -1] - 3 * v[i, j] - 2 * v[i, j - 1]) / (v[i, j])
                    elif j == len(dp_vec) - 2:
                        frac1 = (-v[i, -1] + 6 * v[i, j + 1] - 3 * v[i, j] - 2 * v[i, j - 1]) / (v[i, j])
                    else:
                        frac1 = (-v[i, j + 2] + 6 * v[i, j + 1] - 3 * v[i, j] - 2 * v[i, j - 1]) / (v[i, j])
                    frac2 = (omega_rot * dr_vec[i]) / (6 * dp_vec[j])
                    v[i + 1, j] = v[i, j] + frac1 * frac2

                elif numerical_method == "third_order_upwind_conservative":
                    if j == len(dp_vec) - 1:
                        frac1 = (-np.log(v[i, -2]) + 6 * np.log(v[i, -1]) - 3 * np.log(v[i, j]) - 2 * np.log(
                            v[i, j - 1]))
                    elif j == len(dp_vec) - 2:
                        frac1 = (-np.log(v[i, -1]) + 6 * np.log(v[i, j + 1]) - 3 * np.log(v[i, j]) - 2 * np.log(
                            v[i, j - 1]))
                    else:
                        frac1 = (-np.log(v[i, j + 2]) + 6 * np.log(v[i, j + 1]) - 3 * np.log(v[i, j]) - 2 * np.log(
                            v[i, j - 1]))
                    frac2 = (omega_rot * dr_vec[i]) / (6 * dp_vec[j])
                    v[i + 1, j] = v[i, j] + frac1 * frac2

                elif numerical_method == "conservative_upwind":
                    frac1 = (np.log(v[i, j + 1]) - np.log(v[i, j]))
                    frac2 = (omega_rot * dr_vec[i]) / (dp_vec[j])
                    v[i + 1, j] = v[i, j] + frac2 * frac1

                elif numerical_method == "maccormack":
                    nu = (omega_rot * dr_vec[i]) / (dp_vec[j])
                    v_star_curr = v[i, j] + nu * (np.log(v[i, j + 1]) - np.log(v[i, j]))
                    v_star_prev = v[i, j - 1] + nu * (np.log(v[i, j]) - np.log(v[i, j - 1]))
                    v[i + 1, j] = 0.5 * (v[i, j] + v_star_curr) + (nu / 2) * (np.log(v_star_curr) - np.log(v_star_prev))

                elif numerical_method == "lax_wendroff":
                    # coefficient
                    nu = (omega_rot * dr_vec[i]) / (dp_vec[j])
                    # v(j + 1/2)
                    v_star_curr = 0.5 * (v[i, j + 1] + v[i, j]) + (nu / 2) * (np.log(v[i, j + 1]) - np.log(v[i, j]))
                    # v(j - 1/2)
                    v_star_prev = 0.5 * (v[i, j] + v[i, j - 1]) + (nu / 2) * (np.log(v[i, j]) - np.log(v[i, j - 1]))
                    v[i + 1, j] = v[i, j] + nu * (np.log(v_star_curr) - np.log(v_star_prev))

                elif numerical_method == "lax_friedrichs":
                    nu = (omega_rot * dr_vec[i]) / (dp_vec[j])
                    v[i + 1, j] = 0.5 * (v[i, j - 1] + v[i, j + 1]) + \
                                  (nu / 2) * (np.log(v[i, j + 1]) - np.log(v[i, j - 1]))

                elif numerical_method == "upwind_first_maccormack":
                    # first order upwind method (conservative)
                    f_lower_curr = -omega_rot * np.log(v[i, j + 1])
                    f_lower_prev = -omega_rot * np.log(v[i, j])

                    # McCormack's method
                    nu = (omega_rot * dr_vec[i]) / (dp_vec[j])
                    v_star_curr = v[i, j] + nu * (np.log(v[i, j + 1]) - np.log(v[i, j]))
                    v_star_prev = v[i, j - 1] + nu * (np.log(v[i, j]) - np.log(v[i, j - 1]))

                    f_upper_curr = 0.5 * (f_lower_curr - omega_rot * np.log(v_star_curr))
                    f_upper_prev = 0.5 * (f_lower_prev - omega_rot * np.log(v_star_prev))

                    # evaluate the smoothness of the current wave.
                    theta = (v[i, j] - v[i, j - 1]) / (v[i, j + 1] - v[i, j])

                    # limiter function
                    phi = limiter_function(theta=theta, limiter=flux_function)

                    final_flux_curr = f_lower_curr + phi * (f_upper_curr - f_lower_curr)
                    final_flux_prev = f_lower_prev + phi * (f_upper_prev - f_lower_prev)

                    v[i + 1, j] = v[i, j] - (dr_vec[i] / dp_vec[j]) * (final_flux_curr - final_flux_prev)

                elif numerical_method == "upwind_first_lax_wendroff":
                    # first order upwind method (conservative)
                    f_lower_curr = -omega_rot * np.log(v[i, j + 1])
                    f_lower_prev = -omega_rot * np.log(v[i, j])

                    # Lax-Wendroff method
                    nu = (omega_rot * dr_vec[i]) / (dp_vec[j])
                    # v(j + 1/2)
                    v_star_curr = 0.5 * (v[i, j + 1] + v[i, j]) + (nu / 2) * (np.log(v[i, j + 1]) - np.log(v[i, j]))
                    # v(j - 1/2)
                    v_star_prev = 0.5 * (v[i, j] + v[i, j - 1]) + (nu / 2) * (np.log(v[i, j]) - np.log(v[i, j - 1]))
                    f_upper_curr = -omega_rot * np.log(v_star_curr)
                    f_upper_prev = -omega_rot * np.log(v_star_prev)

                    # evaluate the smoothness of the current wave.
                    theta = (v[i, j] - v[i, j - 1]) / (v[i, j + 1] - v[i, j])

                    # limiter function "superbee"
                    phi = limiter_function(theta=theta, limiter=flux_function)

                    final_flux_curr = f_lower_curr + phi * (f_upper_curr - f_lower_curr)
                    final_flux_prev = f_lower_prev + phi * (f_upper_prev - f_lower_prev)

                    v[i + 1, j] = v[i, j] - (dr_vec[i] / dp_vec[j]) * (final_flux_curr - final_flux_prev)

    return v


def limiter_function(theta, limiter="minmod"):
    """ return a flux-limiter-function result."""
    if limiter == "vanleer":
        return (np.abs(theta) + theta) / (1 + np.abs(theta))
    elif limiter == "minmod":
        return max(0., min(1., theta))
    elif limiter == "superbee":
        return max(0., min(1., 2*theta), min(theta, 2))
    elif limiter == "mc":
        return max(0., min((1 + theta)/2, 2, 2*theta))

