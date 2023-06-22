import math
def randp_distance_project(knn, data, projDS, i_proj, randpoints, num_proj_points):
    d = 0.0
    print(f'randp_distance_project3: i_proj:{i_proj}')
    if i_proj == 0:
        projDS = Dataset(data.size, num_proj_points)

    dim_id = 0
    for i_point in range(num_proj_points):
        randpoint_i = i_proj + i_point
        randind = randpoints[randpoint_i]

        dim_id = i_point
        if i_proj > 0:
            dim_id = i_proj % num_proj_points
            randind = randpoints[i_proj + num_proj_points]
        for i_data in range(data.size):
            d = distance(data, randind, i_data)
            projDS.set_val(i_data, dim_id, math.sqrt(d))
    
        if i_proj > 0:
            break

    return projDS

    
