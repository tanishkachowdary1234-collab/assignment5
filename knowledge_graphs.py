
knowledge_graph = {

    "Hyderabad": {
        "has_place": [
            "Charminar",
            "Golconda Fort",
            "Hussain Sagar"
        ],

        "has_food": [
            "Hyderabadi Biryani",
            "Irani Chai"
        ],

        "has_transport": [
            "Metro",
            "Bus",
            "Cab"
        ]
    },

    "Bengaluru": {
        "has_place": [
            "Cubbon Park",
            "Lalbagh",
            "Bangalore Palace"
        ],

        "has_food": [
            "Masala Dosa",
            "Filter Coffee"
        ],

        "has_transport": [
            "Metro",
            "Bus",
            "Cab"
        ]
    },

    "Visakhapatnam": {
        "has_place": [
            "RK Beach",
            "Kailasagiri",
            "Yarada Beach"
        ],

        "has_food": [
            "Seafood",
            "Fish Curry"
        ],

        "has_transport": [
            "Bus",
            "Cab",
            "Train"
        ]
    }
}


def show_knowledge_graph(city):

    if city not in knowledge_graph:
        print("City not found in Knowledge Graph")
        return

    print("\nKNOWLEDGE GRAPH FOR", city)

    print("\nTourist Places:")
    for place in knowledge_graph[city]["has_place"]:
        print("-", place)

    print("\nFood Recommendations:")
    for food in knowledge_graph[city]["has_food"]:
        print("-", food)

    print("\nTransport Options:")
    for transport in knowledge_graph[city]["has_transport"]:
        print("-", transport)


# Example
city = "Hyderabad"

show_knowledge_graph(city)


print("\nTOOLS USED TO BUILD KNOWLEDGE GRAPHS")
print("1. Neo4j")
print("2. RDFLib (Python)")
print("3. Protégé")
print("4. GraphDB")
print("5. NetworkX")
