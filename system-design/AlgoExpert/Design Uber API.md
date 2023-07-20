
**Video Explanation** 

![[Design The Uber API (540p with 29.98fps).mp4]]

1. Gathering Requirements

As with any API design interview question, the first thing that we want to do is to gather API requirements; we need to figure out what API we're building exactly.

We're designing the core ride-hailing service that Uber offers. Passengers can book a ride from their phone, at which point they're matched with a driver; they can track their driver's location throughout the ride, up until the ride is finished or canceled; and they can also see the price of the ride as well as the estimated time to destination throughout the trip, amongst other things.

The core taxiing service that Uber offers has a passenger-facing side and a driver-facing side; we're going to be designing the API for both sides.

2. Coming Up With A Plan

It's important to organize ourselves and to lay out a clear plan regarding how we're going to tackle our design. What are the major, potentially contentious parts of our API? Why are we making certain design decisions?

We're going to center our API around a _Ride_ entity; every Uber ride will have an associated _Ride_ containing information about the ride, including information about its passenger and driver.

Since a normal Uber ride can only have one passenger (one passenger account--the one that hails the ride) and one driver, we're going to cleverly handle all permissioning related to ride operations through passenger and driver IDs. In other words, operations like _GetRide_ and _EditRide_ will purely rely on a passed userId, the userId of the passenger or driver calling them, to return the appropriate ride tied to that passenger or driver.

We'll start by defining the _Ride_ entity before designing the passenger-facing API and then the driver-facing API.

3. Entities

**Ride**

The _Ride_ entity will have a unique id, info about its passenger and its driver, a status, and other details about the ride.

- rideId: _string_
- passengerInfo: _PassengerInfo_
- driverInfo?: _DriverInfo_
- rideStatus: _RideStatus_ - enum CREATED/MATCHED/STARTED/FINISHED/CANCELED
- start: _GeoLocation_
- destination: _GeoLocation_
- createdAt: _timestamp_
- startTime: _timestamp_
- estimatedPrice: _int_
- timeToDestination: _int_

We'll explain why the _driverInfo_ is optional when we get to the API endpoints.

  
**PassengerInfo**

- id: _string_
- name: _string_
- rating: _int_

**DriverInfo**

- id: _string_
- name: _string_
- rating: _int_
- ridesCount: _int_
- vehicleInfo: _VehicleInfo_

**VehicleInfo**

- licensePlate: _string_
- description: _string_

4. Passenger API

The passenger-facing API will be fairly straightforward. It'll consist of simple CRUD operations around the _Ride_ entity, as well as an endpoint to stream a driver's location throughout a ride.

CreateRide(userId: string, pickup: Geolocation, destination: Geolocation)
  => Ride

Usage: called when a passenger books a ride; a _Ride_ is created with no _DriverInfo_ and with a **CREATED** _RideStatus_; the Uber backend calls an internal _FindDriver_ API that uses an algorithm to find the most appropriate driver; once a driver is found and accepts the ride, the backend calls _EditRide_ with the driver's info and with a **MATCHED** _RideStatus_.

GetRide(userId: string)
  => Ride

Usage: polled every couple of seconds after a ride has been created and until the ride has a status of **MATCHED**; afterwards, polled every 20-90 seconds throughout the trip to update the ride's estimated price, its time to destination, its _RideStatus_ if it's been canceled by the driver, etc..

EditRide(userId: string, [...params?: all properties on the Ride object that need to be edited])
  => Ride

CancelRide(userId: string)
  => void

Wrapper around _EditRide_ -- effectively calls _EditRide(userId: string, rideStatus: CANCELLED)_.

StreamDriverLocation(userId: string)
  => Geolocation

Usage: continuously streams the location of a driver over a long-lived websocket connection; the driver whose location is streamed is the one associated with the _Ride_ tied to the passed _userId_.

5. Driver API

The driver-facing API will rely on some of the same CRUD operations around the _Ride_ entity, and it'll also have a _SetDriverStatus_ endpoint as well as an endpoint to push the driver's location to passengers who are streaming it.

SetDriverStatus(userId: string, driverStatus: DriverStatus)
  => void

DriverStatus: enum UNAVAILABLE/IN RIDE/STANDBY

Usage: called when a driver wants to look for a ride, is starting a ride, or is done for the day; when called with **STANDBY**, the Uber backend calls an internal _FindRide_ API that uses an algorithm to enqueue the driver in a queue of drivers waiting for rides and to find the most appropriate ride; once a ride is found, the ride is internally locked to the driver for 30 seconds, during which the driver can accept or reject the ride; once the driver accepts the ride, the internal backend calls _EditRide_ with the driver's info and with a **MATCHED** _RideStatus_.

GetRide(userId: string)
  => Ride

Usage: polled every 20-90 seconds throughout the trip to update the ride's estimated price, its time to destination, whether it's been canceled, etc..

EditRide(userId: string, [...params?: all properties on the Ride object that need to be edited])
  => Ride

AcceptRide(userId: string)
  => void

Calls _EditRide(userId, MATCHED)_ and _SetDriverStatus(userId, IN_RIDE)_.

CancelRide(userId: string)
  => void

Wrapper around _EditRide_ -- effectively calls _EditRide(userId, CANCELLED)_.

PushLocation(userId: string, location: Geolocation)
  => void

Usage: continuously called by a driver's phone throughout a ride; pushes the driver's location to the relevant passenger who's streaming the location; the passenger is the one associated with the _Ride_ tied to the passed _userId_.

6. UberPool

As a stretch goal, your interviewer might ask you to think about how you'd expand your design to handle UberPool rides.

UberPool rides allow multiple passengers (different Uber accounts) to share an Uber ride for a cheaper price.

One way to handle UberPool rides would be to allow _Ride_ objects to have multiple _passengerInfo_s. In this case, _Ride_s would also have to maintain a list of all destinations that the ride will stop at, as well as the relevant final destinations for individual passengers.

Perhaps a cleaner way to handle UberPool rides would be to introduce an entirely new entity, a _PoolRide_ entity, which would have a list of _Ride_s attached to it. Passengers would still call the _CreateRide_ endpoint when booking an UberPool ride, and so they would still have their own, normal _Ride_ entity, but this entity would be attached to a _PoolRide_ entity with the rest of the UberPool ride information.

Drivers would likely have an extra _DriverStatus_ value to indicate if they were in a ride but still accepting new UberPool passengers.

Most of the other functionality would remain the same; passengers and drivers would still continuously poll the _GetRide_ endpoint for updated information about the ride, passengers would still stream their driver's location, passengers would still be able to cancel their individual rides, etc..


