class Hotel(object):

    def __init__(self, tour_key, title, stars, price, description, picture):
        self.tour_key = tour_key
        self.title = title
        self.stars = stars
        self.price = price
        self.description = description
        self.picture = picture

    def __lt__(self, other):
        return self.price > other.price

def get_tours_by_departure(data, departure):

    tours_by_departure = []

    for tour_key, tour in data.tours.items():
        if tour['departure'] == departure:
            tour['tour_key'] = tour_key
            tours_by_departure.append(tour)

    return tours_by_departure

def sorted_hotels_by_price(tours):

    hotels = []

    for tour_key, tour_data in tours.items():

        hotel = Hotel(int(tour_key),
                      tour_data['title'],
                      tour_data['stars'],
                      tour_data['price'],
                      tour_data['description'],
                      tour_data['picture'])

        hotels.append(hotel)

    hotels.sort()

    return hotels