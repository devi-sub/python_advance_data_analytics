class python_advanced_data_analytics:

    def team_alpha(self):
        print("\n--- Team Alpha ---")
        print("1. Sourav | Roll No: 101 | Favourite: Cricket")
        print("2. Arpitha | Roll No: 102 | Favourite: Music")

    def team_beta(self):
        print("\n--- Team Beta ---")
        print("1. Aiswarya | Roll No: 103 | Favourite: Dancing")
        print("2. Neha     | Roll No: 104 | Favourite: Reading")

    def team_gamma(self):
        print("\n--- Team Gamma ---")
        print("1. Shweta   | Roll No: 105 | Favourite: Painting")
        print("2. Rahul    | Roll No: 106 | Favourite: Coding")

    def team_delta(self):
        print("\n--- Team Delta ---")
        print("1. Priya    | Roll No: 107 | Favourite: Singing")
        print("2. Karthik  | Roll No: 108 | Favourite: Football")


class managements(python_advanced_data_analytics):

    def show_management(self):
        print("\n=== Management Class ===")

obj = managements()

obj.show_management()

obj.team_alpha()
obj.team_beta()
obj.team_gamma()
obj.team_delta()
