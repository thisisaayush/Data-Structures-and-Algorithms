filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.\
newfilenames = []
for x in filenames:
    if x.endswith("hpp"):
        x = x.replace('hpp','h')
    newfilenames.append(x)

print(newfilenames)
