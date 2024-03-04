# AirBnB Clone

## Overview
This project is a simplified version of the AirBnB backend system. It allows users to manage various objects such as users, states, cities, amenities, places, and reviews.

## Installation
1. Clone the repository:
git clone https://github.com/your_username/AirBnB_clone.git


2. Navigate to the project directory:
cd AirBnB_clone
3. Run the console application:
./console.py


## Usage
Once the console is running, you can use the following commands:
- `create`: Create a new object.
- `show`: Display details of a specific object.
- `destroy`: Delete an object.
- `update`: Update attributes of an object.
- `all`: List all objects of a certain type.

Example usage:
```bash
(hbnb) create User
(hbnb) show User 1234-5678
(hbnb) destroy User 1234-5678
(hbnb) update User 1234-5678 first_name "John"
(hbnb) all User
```
## Supported Classes
User

State

City

Amenity

Place

Review



## File Structure
1.models/: Contains Python classes representing different object types.

2.models/engine/: Contains the storage engine for the project.

3.tests/: Contains unit tests for the project.
## Authors
Yassine Lazhari

github: https://github.com/Yassinelaz1
