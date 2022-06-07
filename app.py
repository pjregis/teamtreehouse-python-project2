import constants
import string


def main():
    print("BASKETBALL TEAM STATS TOOL")
    balance_teams()
    main_menu()


def main_menu():
    while True:
        menu_options = ["1", "Q"]
        print("\n\n<<< MAIN MENU >>>\n\n")
        print("Select an option below:\n")
        print("  1) Display Team Stats")
        print("  Q) Quit")
        print("")
        menu_selection = input("Enter an option >> ").upper()
        if menu_selection not in menu_options:
            print("Invalid selection, try again.")
            continue
        else:
            menu_choice(menu_selection)


def menu_choice(selection):
    if selection == "1":
        team_selection_menu()
    if selection == "Q":
        print("Exiting application...")
        quit()


def team_selection_menu():
    while True:
        menu_options = {}
        selected_team = {}
        options = [str(x) for x in list(range(1, 101))]
        print("")
        print("Select a team to view:")
        print("")
        for index, team in enumerate(rosters):
            menu_options[options[index]] = team
            print("{}) {}".format(options[index], team))
        print("")
        print("{}) {}".format("M", "Main Menu"))
        print("{}) {}".format("Q", "Quit"))

        print("")
        menu_selection = input("Enter an option >> ").upper()
        if menu_selection == "M":
            main_menu()
            break
        if menu_selection == "Q":
            print("Exiting application...")
            quit()
        if menu_selection not in menu_options:
            print("Invalid selection, try again.")
            continue
        else:
            selected_team[menu_options[menu_selection]] = rosters[menu_options[menu_selection]]
            display_team(selected_team)
            input("Press ENTER to continue...")
            continue


def balance_teams():
    teams = load_teams_data()
    players = load_players_data()
    players_per_team = (len(players) // len(teams))
    experienced_players = [d for d in players if d['experience']]
    inexperienced_players = [d for d in players if not d['experience']]

    for team in teams:
        temp_players = []
        while len(temp_players) < players_per_team:
            temp_players.append(experienced_players.pop())
            temp_players.append(inexperienced_players.pop())
        rosters[team] = temp_players
    return rosters


def display_team(team):
    team_name = list(team.keys())[0]
    players = ", ".join([player["name"] for player in team[team_name]])
    guardians = ", ".join([x for l in [player["guardians"] for player in team[team_name]] for x in l])
    avg_height = round(
        sum([player["height"] for player in team[team_name]]) / len([player["name"] for player in team[team_name]]), 2)
    experienced_count = sum([player["experience"] for player in team[team_name]])
    inexperienced_count = len(team[team_name]) - experienced_count
    print("")
    header = f"Team: {team_name} Stats"
    print(header)
    print("-" * len(header))
    print("Total players: {}".format(len(team[team_name])))
    print("Total experienced: {}".format(experienced_count))
    print("Total inexperienced: {}".format(inexperienced_count))
    print("Average height: {}".format(avg_height))
    print("")
    print("Players on Team:")
    print("    {}".format(players))
    print("")
    print("Guardians:")
    print("    {}".format(guardians))
    print("")


def load_teams_data():
    teams = []
    teams = constants.get_teams()
    return teams


def load_players_data():
    players = []
    players = constants.get_players()
    cleaned_players = clean_players(players)
    return cleaned_players


def clean_players(data):
    cleaned = []
    for player in data:
        fixed = {"name": player["name"], "guardians": player["guardians"].split(" and ")}
        if player["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        fixed["height"] = int(player["height"].split(" ")[0])
        cleaned.append(fixed)
    return cleaned


if __name__ == "__main__":
    rosters = {}
    main()
