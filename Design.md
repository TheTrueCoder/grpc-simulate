# Architecture
The simulation will involve a grid which balls can move around in at a constant rate and bounce off the walls.
This simulation will be subdivided into tiles which can run on seperate nodes.

The cluster will contain
- One Controller node that syncronises the cluster and assign tiles.
- An arbitrary number of workers that can process tiles.

# Coordinates
Up is +y and Right is +x.