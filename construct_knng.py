import sys
import random
def project_sjs(data, v, p, z_dimensions, rand_vector, dimension_permutation, elem_min, elem_max, precision):
    for i_dim in range(data.dimensionality):
        proj_dim = i_dim % z_dimensions
        if i_dim < z_dimensions:
            p[proj_dim] = 0
        shift_val = rand_vector[i_dim]
        coord = v[dimension_permutation[i_dim]]
        coord = ((coord - elem_min)/(elem_max - elem_min) + shift_val) * precision
        if coord < 0 || p[proj_dim]+coord > sys.maxsize):
            print(f'elem_min:{elem_min}, elem_max:{elem_max}')
            print(f'coord:{p[proj_dim]+coord} > elem_min:{sys.maxsize}(elem_min:{elem_min}, elem_max:{elem_max})')

def project_min_adjust(data, v, p, z_dimensions, rand_vector, dimension_permutation, elem_min, elem_max, precision):
    for i_dim in range(data.dimensionality):
        coord = 0
        proj_dim = i_dim

        coord = v[dimension_permutation[i_dim]]
        coord = coord + sys.maxsize/2.0
        p[proj_dim] = coord

        if (coord < 0 || coord > sys.maxsize):
            print(f'min:{elem_min}, max:{elem_max}')
            print(f'coord:{coord} > {sys.maxsize} (elem_min:{elem_min}, elem_max:{elem_max})')

def calc_precision(D, z_dimensions, elem_min, elem_max, scale):
    g_rand_scale = 10
    precision = sys.maxsize/(1+1*g_rand_scale)
    scale_div = D / z_dimensions + 1
    precision = precision / (scale_div)
    return precision
#
#def generate_z_index(data, z_dimensions, lookup_table, zindex, precision):
#    rand_vector = []
#    dimension_permutation = []
#    for j in range(data.dimensionality):
#        dimension_permutation[j] = j
#    zindex_tmp = data.size
#    for i_dim in range(data.dimensionality):
#        rand_vector[i_dim] = random.randrange(
