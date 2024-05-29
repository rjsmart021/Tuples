from typing import List, Tuple


def get_itinerary_details(flight_itineraries: List[Tuple[str, str, str]]) -> str:
    """

    :param flight_itineraries: List of tuples. Each tuple is having traveller_name, origin and destination
    :return: return formatted itinerary details.
    """
    traveller_number = 1
    itinerary_details = []
    for itinerary in flight_itineraries:
        traveller_name, source, destination = itinerary
        itinerary_formatted_detail = f"itinerary {traveller_number}: {traveller_name} - From {source} to {destination}"
        itinerary_details.append(itinerary_formatted_detail)
        traveller_number += 1
    return '\n'.join(itinerary_details)


# test input argument for get_itinerary_detail function.
flight_itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
print(get_itinerary_details(flight_itineraries))
