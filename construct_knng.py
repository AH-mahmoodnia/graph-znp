import sys
import random
import numpy as np
from globals import *
from dataset import Dataset


def project_sjs(
    data,
    v,
    p,
    z_dimensions,
    rand_vector,
    dimension_permutation,
    elem_min,
    elem_max,
    precision,
):
    for i_dim in range(data.dimensionality):
        proj_dim = i_dim % z_dimensions
        if i_dim < z_dimensions:
            p[proj_dim] = 0
        shift_val = rand_vector[i_dim]
        coord = v[dimension_permutation[i_dim]]
        coord = ((coord - elem_min) / (elem_max - elem_min) + shift_val) * precision
        if coord < 0 | p[proj_dim] + coord > sys.maxsize:
            print(f"elem_min:{elem_min}, elem_max:{elem_max}")
            print(
                f"coord:{p[proj_dim]+coord} > elem_min:{sys.maxsize}(elem_min:{elem_min}, elem_max:{elem_max})"
            )


def project_min_adjust(
    data,
    v,
    p,
    z_dimensions,
    rand_vector,
    dimension_permutation,
    elem_min,
    elem_max,
    precision,
):
    for i_dim in range(data.dimensionality):
        coord = 0
        proj_dim = i_dim

        coord = v[dimension_permutation[i_dim]]
        coord = coord + sys.maxsize / 2.0
        p[proj_dim] = coord

        if coord < 0 | coord > sys.maxsize:
            print(f"min:{elem_min}, max:{elem_max}")
            print(
                f"coord:{coord} > {sys.maxsize} (elem_min:{elem_min}, elem_max:{elem_max})"
            )


def calc_precision(D, z_dimensions, elem_min, elem_max, scale):
    g_rand_scale = 10
    precision = sys.maxsize / (1 + 1 * g_rand_scale)
    scale_div = D / z_dimensions + 1
    precision = precision / (scale_div)
    return precision


# generate z-index with reduce data into z_dimension
def generate_z_index(data, z_dimensions, lookup_table, zindex, precision):
    rand_vector = np.zeros(data.dimensionality).tolist()
    dimension_permutation = list(np.arange(data.dimensionality))
    random.shuffle(dimension_permutation)

    # holding pair of samples (using tuple)
    zindex_tmp = np.zeros(data.size).tolist()

    for i_dim in range(data.dimensionality):
        rand_vector[i_dim] = random.random() * g_rand_scale

    for data_i in range(data.size):
        v = data.get_vector(data_i)
        P = np.zeros(data.dimensionality).tolist()
        project_sjs(
            data,
            v,
            P,
            z_dimensions,
            rand_vector,
            dimension_permutation,
            data.elem_min,
            data.elem_max,
            precision,
        )
        # Generate Z-value for P
