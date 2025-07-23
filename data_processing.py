# This module will handle data processing tasks.


def process_poi_results(results):
    """
    Process the results from the API response.
    """
    processed_data = []
    for r in results:
        j_name = r["name"]
        j_lat = r["location"]["lat"]
        j_lon = r["location"]["lng"]
        j_area = r["area"]
        j_add = r["address"]
        j_str = f"{j_name},{j_lon},{j_lat},{j_area},{j_add}\n"
        processed_data.append(j_str)
    return processed_data
