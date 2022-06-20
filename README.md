# basic_messaging_queue

The Challenge

Develop a message queuing system.
Functional requirements of this system have been described below.
1. Create your own queue that will hold messages in the form of JSON(Standard library with queue implementation were not allowed).
2. There can be more than one queue at any given point of time.
3. There will be one publisher that can generate messages to a queue.
4. There are multiple subscribers that will listen to queues for messages.
5. Subscribers should not be tightly coupled to the system and can be added or removed at runtime.
6. When a subscriber is added to the system, It registers a callback function which makes an API call to the given end point with the json payload, this callback function will be invoked in case some message arrives.
Bonus:
There must be a retry mechanism for handling error cases when some exception occurs in listening/processing a message, that must be retried.
Things to keep in mind while submitting the code:

Coding solution should be in Java.
Working code is required.
Code is evaluated for proper domain modeling and design, need not be optimized.
Separation of concerns must be taken care.
Solution should be extensible.
Writing all the necessary Unit tests is expected.
Necessary design patterns must be implemented.
Naming variable conventions.
Input needs to be read from a text file, and output should be printed to console. Your program should execute and take the location to the test file as a parameter.
