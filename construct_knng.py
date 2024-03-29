import sys
import random
import numpy as np
from globals import *
from zvalue import *
import datetime


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
        zindex_tmp[data_i] = (data_i, z_value(lookup_table, P, z_dimensions))

    print("START Z-value based sorting")
    zindex_tmp.sort(lambda x, y: y)
    print("END Z-value based sorting")

    for data_i in range(len(zindex_tmp)):
        zindex[data_i] = zindex_tmp[data_i][0]


def debug_zindex(data, zindex, head):
    data_i = 0
    while data_i < data.size and data_i < head:
        print(zindex[data_i])

def sliding_window_search(data, knng, zindex, window_width):
    update_count = 0
    for data_i in range(data.size - window_width):
        for w in range(window_width):
            update_count += update(knng, data, zindex[data_i], zindex[data_i+w])
            g_dist_count++

    return update_count

def z_search(data, knng, num_curves, K, window_width, z_dimensions):
    lookup_table = generate_lookup_table(z_dimensions)
    precision = calc_precision(data.dimensionality, z_dimensions, data.elem_min, data.elem_max, 1.1)
    zindex [0] * data.size
    projDS = data
    update_count = 0
    update_count_nndes = 0
    update_portion = 0
    update_portion_nndes = 0
    randpoints 
    new_knn = [[]] * data.size
    old_knn = [[]] * data.size
    print(f'min: {data.elem_min}, max: {data.elem_max}, precision: {precision}')
    print("Start generate rand projection points")
    # the heterogenous_rand_points is not yet written
    if g_options.randp_distance_project > 0:
        # rp = generate_heterogenous_rand_points(data, 500, 100)
    print("End generate rand projection points")
    randpoints = rp
    proj_dim = z_dimensions
    nndes_start_k = g_options.recall_K
    nndes_max_k = K
    nndes_k = nndes_start_k
    run_nndes = 0
    k_increment = 2

    if g_options.nndes_k > 0:
        nndes_max_k = nndes_k = g_options.nndes_k

    projDS.find_min_max()

    i_curve = 0
    while True:
        print("="*50)
        print(f"START iteration={i_curve+1} time={datetime.datetime.now()}")
        if g_options.randp_distance_project > 0:
            print("randp_distance_project")
            proj_dim = g_options.randp_distance_project
            projDS = randp_distance_project(knng, data, projDS, i_curve, randpoints, proj_dim)
            projDS.find_min_max()
        if g_options.randp_distance_project > 0:
            stat = [None]*proj_dim
            for i in range(proj_dim):
                stat[i] = Stat()

            for i_dim in range(proj_dim):
                i_data = 0
                while i_data < projDS.size:
                    val = projDs.get_val(i_data, i_dim)
                    stat[i_dim].push_stat(val)
                    i_data+=1
            for i_dim in range(proj_dim):
                print(f"dim: {i_dim}")
                stat[i_dim].debug_stat()

            for i_dim in range(proj_dim):
                if stat[i_dim].mean < -0.2 || stat[i_dim].mean > 0.2:
                    print(f"Mean center data for dim: {i_dim}")
                    projDS.mean_center_data(stat[i_dim], i_dim)

            projDS.find_min_max()

            generate_z_index(projDS, proj_dim, lookup_table, zindex, precision)
            debug_zindex(projDS, zindex)

            update_count = sliding_window_search(data, knng, zindex, window_width)
            update_portion = update_count / (data.size * knng.k)
            print(f"Z-order update count: {update_count}, {update_portion}")


        i_curve+=1












