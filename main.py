class COLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(COLORS.WARNING + "                                  __              " + COLORS.ENDC)
print(COLORS.WARNING + "_____    ________ _______ _______" + COLORS.ENDC + COLORS.OKBLUE + "|__|" + COLORS.WARNING + "__ __  ______" + COLORS.ENDC)
print(COLORS.OKBLUE + "\__  \  / ____/  |  \__  \\\\_  __ \  |  |  \/  ___/" + COLORS.ENDC)
print(COLORS.OKBLUE + " / __ \| |_|  |  |  // __ \|  | \/  |  |  /\___ \ " + COLORS.ENDC)
print(COLORS.OKBLUE + "(____  /\__   |____/(____  /__|  |__|____//____  |" + COLORS.ENDC)
print(COLORS.OKBLUE + "     \/    |__|          \/                    \/ " + COLORS.ENDC)
print(COLORS.UNDERLINE + "                                                  " + COLORS.ENDC)
print()
print(COLORS.BOLD + "Version 0.1               Created by Team Aquarius" + COLORS.ENDC)
print("")

while True:
  message = input("> ")
  if message == "ur dumb":
    print(COLORS.WARNING + "no u" + COLORS.ENDC)

  if message == "Team Aquarius":
    print(COLORS.WARNING + "WOOT WOOT!" + COLORS.ENDC)
  
  if message == "calculator":
    num1 = float(input(COLORS.WARNING + "Enter first number: " + COLORS.ENDC))
    op = input(COLORS.WARNING + "Enter operation: " + COLORS.ENDC)
    num1 = float(input(COLORS.WARNING + "Enter second number: " + COLORS.ENDC)) 