def display_digits(my_tuple):
  digits = "".join(str(x) for x in my_tuple if str(x).isdigit())
  print("Digits:", digits)

# Example usage
my_tuple = ("hello", 123, "world", 456)
display_digits(my_tuple)
