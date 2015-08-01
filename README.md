pyprototype
===========
Attempt to make a small roguelike game with python. Now done:
  * levgen.py - creates a single level with rectangular rooms, sometimes not connected to each other
  * locations.py - storage for special rooms, such as dungeon entrance hall, etc.

Changelog
----------
  
  * 2015-06-13 levgen.py: now creates more than one room. rooms are still only rectangular. I also don't know when to stop creating rooms. Now it creates certain number of them.
  * 2015-07-30 levgen.py: creates rooms of different types (rectangular rooms, corridors), mostly connected to each other
  * 2015-08-01 levgen.py: now place_room methods adds list of tiles to map instead of rewriting existing tiles; "facelifting" - renamed methods and variables according to PEP-8 and pankshok advice.
