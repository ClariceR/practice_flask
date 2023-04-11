## Creating our helper functions

###How to create a function to search a specific flight?

*In order to find a flight, we need the id of the flight we are searching for.*

*In order to search a list, we can use a `for loop`.
Then we need to compare the id property of each element,
with the id we passed into the function (the `fid` we are looking for)*

*But we can't just call it `id` inside our function, we need to know the correct key name in our DB*

*Looking at the data in our temporary dummy data file `flights_data.py`, we can see the flight id is called `flight_id`*

*In order to maintain the coherence with having the data inside a list,
we create an empty list to append the result if we find one,
(or many, in case what we are looking for is not an unique value)*

*Also, if nothing is found, we will return an empty list, 
and we don't need to worry about what to return if there's no match*

```buildoutcfg
def search_flights(fid, flights):
    flights_found = []

    for flight in flights:
        if flight['flight_id'] == fid:
            flights_found.append(flight)

    return flights_found
```

