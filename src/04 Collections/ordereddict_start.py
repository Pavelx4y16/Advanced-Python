# Demonstrate the usage of OrderedDict objects

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    # create an ordered dictionary of the teams
    teams = OrderedDict(sortedTeams)

    # Use popitem to remove the top item
    top_team = teams.popitem(last=False)
    print(top_team)
    print(teams)

    # What are next the top 4 teams?
    for i, team in enumerate(teams, start=1):
        if i <= 4:
            print(team)
        else:
            break

    # test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "b": 2, "c": 3})
    print(a == b)

    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    print(a == b)


if __name__ == "__main__":
    main()
