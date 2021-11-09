# imagine we have a list of strings and ints
stuff = [1, 4, 'two', 3, 'five']

# we can loop over these elements but we can't
# use the capitalize() method on integers! 
for thing in stuff: 
  print(thing.capitalize()) # Error