def main():
  initial_height = float(input("Type the initial height of the object in meters: "))
  free_fall_simulator(initial_height)

  return 0


def free_fall_simulator(initial_height):
  gravity = 10

  time = 0
  height = initial_height

  print("\n----- Free fall simulator -----")
  print(f"Initial height: {initial_height} meters\n")

  while height > 0:
      print(f"Time: {time}s - Height: {height:.2f} meters")
      time += 1
      height = initial_height - 0.5 * gravity * (time**2)

  print(f"Time: {time}s - The object hit the ground.")


main()