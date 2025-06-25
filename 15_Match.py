def match_day(day):
    match day:
        case "Monday":
            return "Start of the work week."
        case "Friday":
            return "Almost weekend!"
        case "Saturday" | "Sunday":
            return "Weekend vibes!"
        case _:
            return "Just another weekday."

# Test the function
for d in ["Monday", "Wednesday", "Friday", "Saturday", "Tuesday"]:
    print(f"{d}: {match_day(d)}")

