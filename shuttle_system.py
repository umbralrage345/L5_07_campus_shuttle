"""Campus shuttle timetable and fleet tracking system."""
import json
import secrets
from datetime import datetime

# Global state
routes = {"R1": {"name": "Main Gate - Library", "trips": []},
          "R2": {"name": "Hostel - Sports Complex", "trips": []},
          "R3": {"name": "Admin Block - Metro", "trips": []}}
MIN_CAPACITY = 10

def add_trip_log(route_id, passenger_count, logs=None):
    """Record a trip and append its entry to the supplied log list."""
    if logs is None:
        logs = []

    routes[route_id]["trips"].append(passenger_count)
    logs.append(
        f"{datetime.now()}: {route_id} carried {passenger_count}"
    )
    return logs

def remove_route(route_id):
    """Remove a route from the fleet."""
    del routes[route_id]



def average_load(route_id):
    """Calculate the average passenger count for a route."""
    trips = routes[route_id]["trips"]
    return sum(trips) / len(trips)

def underused_routes():
    """Identify routes with average loads below the minimum capacity."""
    flagged = []
    for r in routes:
        try:
            if average_load(r) < MIN_CAPACITY:
                flagged.append(r)
        except (TypeError, ZeroDivisionError) as exc:
            print(
                f"Skipping route {r}: cannot calculate average load: {exc}"
            )
    return flagged

def assign_driver():
    """Randomly select a driver from the available drivers."""
    drivers = ["Prakash", "Leela", "Imran", "Tom"]
    return secrets.choice(drivers)

def sync_fleet_data(file="fleet.json"):
    """Save route data and reload it from the JSON file."""
    with open(file, "w", encoding="utf-8") as fleet_file:
        json.dump(routes, fleet_file)

    with open(file, "r", encoding="utf-8") as fleet_file:
        return json.load(fleet_file)

def main():
    """Run the campus shuttle tracking demonstration."""
    add_trip_log("R1", 32)
    add_trip_log("R1", 28)
    add_trip_log("R2", 4)
    add_trip_log("R2", 6)
    add_trip_log("R3", 18)

    print("Driver for R1:", assign_driver())
    print("Underused:", underused_routes())
    print("R1 average:", average_load("R1"))
    print("R3 average:", average_load("R3"))

    reloaded_routes = sync_fleet_data()
    routes.clear()
    routes.update(reloaded_routes)

    remove_route("R3")

    choice = input(
        "Route to look up (Enter for R2): "
    ).strip().upper() or "R2"

    if choice not in routes:
        print(
            f"Unknown route: {choice}. "
            f"Available routes: {', '.join(routes)}"
        )
        return

    print("Trips on", choice, ":", routes[choice]["trips"])

if __name__ == "__main__":
    main()
