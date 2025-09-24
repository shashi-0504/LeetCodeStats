remainder_to_position = {}  # Track where each remainder first appears
decimal_digits = []         # Build decimal part digit by digit

while remainder != 0 and remainder not in remainder_to_position:
    remainder_to_position[remainder] = len(decimal_digits)  # Mark position
    remainder *= 10           # Shift for next division step
    decimal_digits.append(str(remainder // denominator))   # Get next digit
    remainder = remainder % denominator                     # Update remainder