import math

# Travel knowledge base
travel_knowledge_base = {
    "Hyderabad": {
        "places": {
            "history": [
                "Charminar",
                "Golconda Fort",
                "Salar Jung Museum"
            ],
            "food": [
                "Famous Biryani Spots",
                "Irani Cafe",
                "Street Food Market"
            ],
            "nature": [
                "Hussain Sagar Lake",
                "NTR Garden"
            ],
            "shopping": [
                "Laad Bazaar",
                "Inorbit Mall"
            ]
        },

        "food_options": {
            "veg": [
                "Veg Biryani",
                "South Indian Meals",
                "Paneer Curry"
            ],
            "non-veg": [
                "Hyderabadi Chicken Biryani",
                "Mutton Biryani",
                "Kebab"
            ]
        },

        "hotel_cost_per_day": {
            "low": 1000,
            "medium": 2500,
            "high": 5000
        },

        "transport_per_day": 500
    },

    "Visakhapatnam": {
        "places": {
            "nature": [
                "RK Beach",
                "Kailasagiri",
                "Yarada Beach"
            ],
            "history": [
                "Submarine Museum",
                "Victory at Sea Memorial"
            ],
            "food": [
                "Seafood Restaurants",
                "Beach Snacks"
            ],
            "shopping": [
                "CMR Central Mall"
            ]
        },

        "food_options": {
            "veg": [
                "Vegetable Meals",
                "Dosa"
            ],
            "non-veg": [
                "Fish Curry",
                "Prawns Fry"
            ]
        },

        "hotel_cost_per_day": {
            "low": 1200,
            "medium": 3000,
            "high": 5500
        },

        "transport_per_day": 600
    },

    "Bengaluru": {
        "places": {
            "nature": [
                "Cubbon Park",
                "Lalbagh Botanical Garden"
            ],
            "history": [
                "Bangalore Palace"
            ],
            "food": [
                "Food Street",
                "South Indian Restaurants"
            ],
            "shopping": [
                "Commercial Street",
                "UB City Mall"
            ]
        },

        "food_options": {
            "veg": [
                "Idli",
                "Masala Dosa"
            ],
            "non-veg": [
                "Chicken Meals",
                "Biryani"
            ]
        },

        "hotel_cost_per_day": {
            "low": 1500,
            "medium": 3500,
            "high": 6000
        },

        "transport_per_day": 700
    }
}


def generate_travel_plan(city, budget, days, interest, food_preference):

    if city not in travel_knowledge_base:
        print("Sorry! City not available.")
        return

    city_data = travel_knowledge_base[city]

    print("\nAI TRAVEL PLAN")
    print("Destination:", city)
    print("Budget: ₹", budget)
    print("Days:", days)
    print("Interest:", interest)
    print("Food Preference:", food_preference)

    # Select hotel based on budget
    if budget < 5000:
        hotel_type = "low"

    elif budget < 10000:
        hotel_type = "medium"

    else:
        hotel_type = "high"

    hotel_cost = (
        city_data["hotel_cost_per_day"][hotel_type]
        * days
    )

    transport_cost = (
        city_data["transport_per_day"]
        * days
    )

    food_cost_per_day = 400
    total_food_cost = food_cost_per_day * days

    recommended_places = []

    # Recommend places using user interest
    if interest in city_data["places"]:
        recommended_places.extend(
            city_data["places"][interest]
        )

    # Add extra places if needed
    if len(recommended_places) < days:

        for category in city_data["places"]:

            for place in city_data["places"][category]:

                if place not in recommended_places:
                    recommended_places.append(place)

    # Food recommendation
    foods = city_data["food_options"].get(
        food_preference.lower(),
        []
    )

    # Total trip cost calculation
    total_cost = (
        hotel_cost +
        transport_cost +
        total_food_cost
    )

    print("\nRecommended Places:")

    for place in recommended_places:
        print("-", place)

    print("\nRecommended Food:")

    for item in foods:
        print("-", item)

    print("\nHotel Category Selected:", hotel_type)

    print("\nEstimated Cost:")
    print("Hotel Cost     : ₹", hotel_cost)
    print("Transport Cost : ₹", transport_cost)
    print("Food Cost      : ₹", total_food_cost)
    print("Total Cost     : ₹", total_cost)

    if total_cost > budget:
        print("\nWarning: Budget may not be sufficient.")

    else:
        print("\nTrip fits within budget.")

    print("\nPERSONALIZED TOUR PLAN")

    # Creates day wise tour plan
    places_per_day = math.ceil(
        len(recommended_places) / days
    )

    index = 0

    for day in range(1, days + 1):

        print("\nDay", day)

        for _ in range(places_per_day):

            if index < len(recommended_places):

                print(
                    "- Visit",
                    recommended_places[index]
                )

                index += 1

        if foods:
            print("- Try:", foods[0])


print("AI TRAVEL PLANNER")

city = input(
    "Enter destination city "
    "(Hyderabad/Visakhapatnam/Bengaluru): "
)

budget = int(input("Enter budget: ₹"))

days = int(input("Enter number of days: "))

interest = input(
    "Enter interest "
    "(history/food/nature/shopping): "
).lower()

food_preference = input(
    "Food preference (veg/non-veg): "
).lower()

generate_travel_plan(
    city,
    budget,
    days,
    interest,
    food_preference
)s
