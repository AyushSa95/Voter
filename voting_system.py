# CLI Voting System

def display_menu():
    print("\n--- Voting System ---")
    print("1. Add candidate")
    print("2. Cast vote")
    print("3. Show results")
    print("4. Exit")

def add_candidate(candidates):
    name = input("Enter candidate name: ").strip()
    if name in candidates:
        print("Candidate already exists!")
    else:
        candidates[name] = 0
        print(f"Candidate '{name}' added.")

def cast_vote(candidates):
    if not candidates:
        print("No candidates available to vote for.")
        return
    
    print("\nCandidates:")
    for idx, candidate in enumerate(candidates.keys(), 1):
        print(f"{idx}. {candidate}")

    try:
        choice = int(input("Enter candidate number: "))
        if 1 <= choice <= len(candidates):
            selected = list(candidates.keys())[choice - 1]
            candidates[selected] += 1
            print(f"Vote cast for '{selected}'.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

def show_results(candidates):
    if not candidates:
        print("No candidates to display.")
        return
    
    print("\n--- Voting Results ---")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} votes")
    
    winner = max(candidates, key=candidates.get)
    print(f"\nWinner: {winner} 🎉")

def main():
    candidates = {}
    while True:
        display_menu()
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            add_candidate(candidates)
        elif choice == "2":
            cast_vote(candidates)
        elif choice == "3":
            show_results(candidates)
        elif choice == "4":
            print("Exiting voting system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
