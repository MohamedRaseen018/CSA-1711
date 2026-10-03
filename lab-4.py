def solve_cryptarithmetic(words, result):
    # Gather all unique letters across the puzzle
    all_words = words + [result]
    unique_letters = list(set("".join(all_words)))
    
    # Cryptarithmetic is impossible if there are more than 10 unique letters
    if len(unique_letters) > 10:
        return None

    # Track leading letters because they cannot be assigned the digit 0
    leading_letters = {word[0] for word in all_words if len(word) > 1}
    
    # Maps to track current assignments
    letter_to_digit = {}
    digit_assigned = [False] * 10

    def word_to_value(word):
        """Converts a word to its numerical value based on current letter mapping."""
        return int("".join(str(letter_to_digit[char]) for char in word))

    def check_equation():
        """Validates if the sum of words equals the result."""
        return sum(word_to_value(w) for w in words) == word_to_value(result)

    def backtrack(index):
        # Base case: All letters have been assigned a digit
        if index == len(unique_letters):
            return check_equation()

        char = unique_letters[index]

        for digit in range(10):
            # Enforce constraints: digit must be unused, and no leading zeros
            if not digit_assigned[digit]:
                if digit == 0 and char in leading_letters:
                    continue  

                # Assign digit
                letter_to_digit[char] = digit
                digit_assigned[digit] = True

                # Recurse to next letter
                if backtrack(index + 1):
                    return True

                # Backtrack (Undo assignment)
                del letter_to_digit[char]
                digit_assigned[digit] = False

        return False

    if backtrack(0):
        return letter_to_digit
    return None

# --- Example Usage ---
if __name__ == "__main__":
    # Puzzle: SEND + MORE = MONEY
    puzzle_words = ["SEND", "MORE"]
    puzzle_result = "MONEY"
    
    print(f"Solving: {' + '.join(puzzle_words)} = {puzzle_result}...\n")
    solution = solve_cryptarithmetic(puzzle_words, puzzle_result)
    
    if solution:
        print("🎉 Solution Found!")
        # Sort alphabetically for nice display
        for letter, digit in sorted(solution.items()):
            print(f"{letter} = {digit}")
            
        # Display equation verification
        send_val = "".join(str(solution[c]) for c in "SEND")
        more_val = "".join(str(solution[c]) for c in "MORE")
        money_val = "".join(str(solution[c]) for c in "MONEY")
        print(f"\nEquation: {send_val} + {more_val} = {money_val}")
    else:
        print("No solution exists for this puzzle.")
