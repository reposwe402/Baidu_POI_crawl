import time
from api import fetch_poi_data
from data_processing import process_poi_results
from file_handler import ensure_directory_exists, open_log_and_data_files, write_to_file


def get_baidu_poi(roi_key, city_str, baidu_ak, output):
    """
    inputs:
        roi_key: poi name
        city_str: city name
        baidu_ak: baidu web API AK
        output: file save path
    """
    page_num = 0
    ensure_directory_exists(output)
    logfile, datafile = open_log_and_data_files(output)
    while True:
        try:
            res = fetch_poi_data(roi_key, city_str, baidu_ak, page_num)
            if len(res["results"]) == 0:
                write_to_file(logfile, time.strftime("%Y-%m-%d-%H-%M-%S") + " " + city_str + " " + str(page_num) + "\n")
                break
            else:
                processed_data = process_poi_results(res["results"])
                write_to_file(datafile, processed_data)
            page_num += 1
            time.sleep(1)
        except Exception as e:
            print("Exception occurred:", e)
            write_to_file(logfile, time.strftime("%Y-%m-%d-%H-%M-%S") + " " + city_str + " " + str(page_num) + "\n")
            break
