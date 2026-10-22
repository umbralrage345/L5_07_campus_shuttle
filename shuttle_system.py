"""Campus shuttle timetable and fleet tracking system."""

import json
import secrets
from datetime import datetime


routes = {
    "R1": {"name": "Main Gate - Library", "trips": []},
    "R2": {"name": "Hostel - Sports Complex", "trips": []},
    "R3": {"name": "Admin Block - Metro", "trips": []},
}
MIN_CAPACITY = 10


def add_trip_log(route_id, passenger_count, logs=None):
    """Record a trip and append its entry to the supplied log list."""
    if route_id not in routes:
        raise KeyError(f"Unknown route: {route_id}")

    if isinstance(passenger_count, bool) or not isinstance(
        passenger_count, int
    ):
        raise TypeError("Passenger count must be a non-negative integer.")

    if passenger_count < 0:
        raise ValueError("Passenger count cannot be negative.")

    if logs is None:
        logs = []

    routes[route_id]["trips"].append(passenger_count)
    logs.append(
        f"{datetime.now()}: {route_id} carried {passenger_count}"
    )
    return logs


def remove_route(route_id):
    """Remove a route from the fleet."""
    if route_id not in routes:
        raise KeyError(f"Unknown route: {route_id}")
    del routes[route_id]


def average_load(route_id):
    """Calculate the average passenger count for a route."""
    trips = routes[route_id]["trips"]
    if not trips:
        return 0.0
    return sum(trips) / len(trips)


def underused_routes():
    """Identify routes with average loads below the minimum capacity."""
    flagged = []

    for route_id in routes:
        try:
            if average_load(route_id) < MIN_CAPACITY:
                flagged.append(route_id)
        except (KeyError, TypeError) as exc:
            print(
                f"Skipping route {route_id}: "
                f"cannot calculate average load: {exc}"
            )

    return flagged


def assign_driver():
    """Randomly select a driver from the available drivers."""
    drivers = ["Prakash", "Leela", "Imran", "Tom"]
    return secrets.choice(drivers)


def sync_fleet_data(filename="fleet.json"):
    """Save route data and reload it from the JSON file."""
    with open(filename, "w", encoding="utf-8") as fleet_file:
        json.dump(routes, fleet_file, indent=4)

    with open(filename, "r", encoding="utf-8") as fleet_file:
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

    remove_route("R3")

    reloaded_routes = sync_fleet_data()
    routes.clear()
    routes.update(reloaded_routes)

    choice = (
        input("Route to look up (Enter for R2): ").strip().upper()
        or "R2"
    )

    if choice not in routes:
        print(
            f"Unknown route: {choice}. "
            f"Available routes: {', '.join(routes)}"
        )
        return

    print("Trips on", choice, ":", routes[choice]["trips"])


if __name__ == "__main__":
    main()
