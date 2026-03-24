## Q14
Which data structure would best represent average latitude and longitude for each city in a group of cities, accessible by city name?

A tuple of string city names, latitudes, and longitudes.

A list of tuples, each containing a string city name, and a float for both latitude and longitude.

A set of string city names, latitudes, and longitudes

A dict with string city name keys and tuple latitude/longitude values.


### Answer
The best choice here is **a `dict` with `string` city name keys and `tuple` latitude/longitude values.**

In the world of data structures, we often choose a "container" based on how we want to find our data. Here is a breakdown of why the dictionary (dict) wins and why the others don’t quite make the cut.

---

### Why the Dictionary is the Winner
A **dictionary** is designed specifically for "key-value" lookups. 

* **The Key:** The city name (e.g., `"Tokyo"`).
* **The Value:** The coordinates (e.g., `(35.6895, 139.6917)`).

Because dictionaries use a process called "hashing," looking up a city name is nearly instantaneous, regardless of whether you have 10 cities or 10,000. 



### Evaluating the Other Options

| Data Structure | Why it's not the "best" fit |
| :--- | :--- |
| **A tuple of strings/floats** | Tuples are immutable sequences. You'd essentially have one long, messy list of data with no clear way to separate one city from another without counting indexes. |
| **A list of tuples** | This works, but it's inefficient for searching. To find "Paris," you’d have to start at the beginning of the list and check every single tuple until you find the right name. |
| **A set of strings/floats** | Sets are unordered and don't allow duplicate values. While they are fast for checking if an item exists, they don't allow you to "map" one piece of data (the name) to another (the coordinates). |

---

### The Code Representation
In Python, the winning structure looks like this:

```python
cities = {
    "New York": (40.7128, -74.0060),
    "London": (51.5074, -0.1278),
    "Sydney": (-33.8688, 151.2093)
}

# Accessing the data is direct and readable:
coords = cities["London"] 
```

Would you like me to show you how to perform calculations with this data, such as finding the distance between two cities in this dictionary?


