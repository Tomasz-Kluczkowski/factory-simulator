# Factory Floor Simulator

[![Build Status](https://travis-ci.org/Tomasz-Kluczkowski/factory-simulator.svg?branch=master)](https://travis-ci.org/Tomasz-Kluczkowski/factory-simulator) [![codecov](https://codecov.io/gh/Tomasz-Kluczkowski/factory-simulator/branch/master/graph/badge.svg)](https://codecov.io/gh/Tomasz-Kluczkowski/factory-simulator)

In this project I am simulating a factory floor operation.

This is based on a programming task received on one of the interviews that got me interested and curious.

The rules are as follows:

- Time is discrete and no action can take less than 1 unit of time.
- In the default settings picking up from and dropping objects onto the conveyor belt takes 1 unit of time.
- In the default settings constructing the finished product takes 4 units of time.
- The conveyor belt is empty at start and all slots are free (can be operated on).
- At each slot of the conveyor belt we place a worker on both sides of it.
- Only one worker can operate on any given slot at any given time.

Default components required to make a product:
- A
- B

Default code for an empty slot on the conveyor belt:
- E

Default code for the finished product:
- P

The default layout of the factory floor:

```
            (worker) (worker) (worker)
A-B-E-E    |   A    |    E   |   E    |     E-E-E-E-P-E-E
            (worker) (worker) (worker)  

             slot0     slot1   slot2

(Feeder)        (Conveyor Belt)             (Receiver)

```
 
Basic principle of operation:
- The feeder supplies components required to make a finished product.
- Workers at the conveyor belt slots check if they need and can pickup components.
- Once a worker collected all required items he begins assembling the product.
- When the product is assembled and worker can operate on his conveyor belt slot (it is free and empty) the worker
will drop the product.


