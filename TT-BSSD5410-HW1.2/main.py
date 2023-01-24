#############################################
# 1. Combine the distance code with the selection sort implementation in one project. You can
# use a single file or multiple files if you know how.
# 2. Programmatically find the distance from the Natural History Museum in Albuquerque to 5
# other locations of your choosing. Save those locations into a list, and sort the list using
# selection sort so that the shortest distance is first and the rest are in order.
# 3. Print out the names of the places in ascending order, starting with the closest location to
# the chosen origin.
#############################################

import math

import requests

import sort

URL_PATH = "https://nominatim.openstreetmap.org/search.php"


def get_lat_lon(location):
    PARAMS = {"q": location, "format": "jsonv2"}
    response = requests.get(url=URL_PATH, params=PARAMS)
    data = response.json()
    latitude = float(data[0]["lat"])
    longitude = float(data[0]["lon"])
    return [latitude, longitude]


# end def get_lat_lon(location)

def calculate_distance(origin, destination, destination_name):
    latitude_difference = destination[0] - origin[0]
    longitude_difference = destination[1] - origin[1]
    a = (math.sin(math.radians(latitude_difference / 2))) ** 2 + \
        math.cos(math.radians(origin[0])) * \
        math.cos(math.radians(destination[0])) * \
        (math.sin(math.radians(longitude_difference / 2))) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    earthRadius = 3961
    distance = earthRadius * c
    return distance, destination_name


# end def calculate_distance(origin, destination):


def main():
    origin = "New Mexico Museum of Natural History & Science"
    destination_1 = "New Mexico Highlands University"
    destination_2 = "Georgia Institute of Technology"
    destination_3 = "Tennessee State University"
    destination_4 = "University of Maine"
    destination_5 = "Western Illinois University"

    distancesArray = []

    origin_lat_lon = get_lat_lon(origin)
    destination_1_lat_lon = get_lat_lon(destination_1)
    destination_2_lat_lon = get_lat_lon(destination_2)
    destination_3_lat_lon = get_lat_lon(destination_3)
    destination_4_lat_lon = get_lat_lon(destination_4)
    destination_5_lat_lon = get_lat_lon(destination_5)

    distancesArray.append(calculate_distance(origin_lat_lon, origin_lat_lon, origin))
    distancesArray.append(calculate_distance(origin_lat_lon, destination_1_lat_lon, destination_1))
    distancesArray.append(calculate_distance(origin_lat_lon, destination_2_lat_lon, destination_2))
    distancesArray.append(calculate_distance(origin_lat_lon, destination_3_lat_lon, destination_3))
    distancesArray.append(calculate_distance(origin_lat_lon, destination_4_lat_lon, destination_4))
    distancesArray.append(calculate_distance(origin_lat_lon, destination_5_lat_lon, destination_5))

    sort.selection_sort(distancesArray)

    print(f"Below is the list of closest locations to {origin} in ascending order:")
    count = 1
    while count < len(distancesArray):
        print(f"{distancesArray[count][1]}")
        count += 1


if __name__ == "__main__":
    main()
