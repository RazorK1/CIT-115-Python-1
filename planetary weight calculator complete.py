#  Kyle Harris
#  CIT-115/115L Python
#  Inter Planetary Weights 


#  1. Declare Named Constants for each of the planet Surface Gravity Factors
MERCURY_GRAVITY = 0.38
VENUS_GRAVITY = 0.91
MOON_GRAVITY = 0.165
MARS_GRAVITY = 0.38
JUPITER_GRAVITY = 2.34
SATURN_GRAVITY = 0.93
URANUS_GRAVITY = 0.92
NEPTUNE_GRAVITY = 1.12
PLUTO_GRAVITY = 0.066


#  2. Ask the user for a Name and their Earth Weight
sName = input("What is your name: ")
#  Spacer
print()


#  3. Converts the entered Weight to the appropriate data type
nEarthWeight = float(input("What is your weight: "))
#  Spacer
print()


#  4. Multiply the Earth Weight by each of the planet’s Surface Gravity Factor
nWeightMercury = nEarthWeight * MERCURY_GRAVITY
nWeightVenus = nEarthWeight * VENUS_GRAVITY
nWeightMoon = nEarthWeight * MOON_GRAVITY
nWeightMars = nEarthWeight * MARS_GRAVITY
nWeightJupiter = nEarthWeight * JUPITER_GRAVITY
nWeightSaturn = nEarthWeight * SATURN_GRAVITY
nWeightUranus = nEarthWeight * URANUS_GRAVITY
nWeightNeptune = nEarthWeight * NEPTUNE_GRAVITY
nWeightPluto = nEarthWeight * PLUTO_GRAVITY


#  5. Output the inputted name and computed weights
print(f"{sName}, here are your weights on our Solar System's planets:")
#  Spacer
print()
print(f"{'Mercury':<10}: {nWeightMercury:10.2f}")
print(f"{'Venus':<10}: {nWeightVenus:10.2f}")
print(f"{'Moon':<10}: {nWeightMoon:10.2f}")
print(f"{'Mars':<10}: {nWeightMars:10.2f}")
print(f"{'Jupiter':<10}: {nWeightJupiter:10.2f}")
print(f"{'Saturn':<10}: {nWeightSaturn:10.2f}")
print(f"{'Uranus':<10}: {nWeightUranus:10.2f}")
print(f"{'Neptune':<10}: {nWeightNeptune:10.2f}")
print(f"{'Pluto':<10}: {nWeightPluto:10.2f}")
#  Spacer
print()


#  Does nothing
sResult = input("Are you satisfied with the results? (Y/N): ")
#  Spacer
print()


#  Prevents the program from closing.
input("Press Enter to exit...")