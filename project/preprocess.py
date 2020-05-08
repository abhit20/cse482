"""
CSE 482: Big Data Analysis Project Script
"""
from datetime import datetime

def open_file():
    '''
    Opens the game file
    :return: The opened file
    '''
    fp = input("Input a file name: ")
    while True:
        try:
            fp = open(fp)
            return fp
        except FileNotFoundError:
            print("Error: file not found\n")
            fp = input("Input a filename: ")

def read_file(fp):
    """
    Reads the game data file and stores it in dictionary
    :param fp: The file to read
    :return: The sorted dictionaries of home team and away team games, and list of schedule
    """

    home_dict = {}      # Home team as the key and the statistics of each game as values
    away_dict = {}      # Away team as the key and the statistics of each game as values
    schedule_lst = []   # Schedule of the games

    lines = fp.readlines()

    # Iterates thorugh every line in the game data file
    for i, line in enumerate(lines):
        if i > 0:
            lst = line.strip().split(",")

            # Retrieves the home and away team names
            home_team = lst[1]
            away_team = lst[15]

            # Creates the list of home team game statistics
            temp_home_lst = lst[1:]
            temp_home_lst.append(lst[0])

            # Adds the home team game to home game dictionary and sorts it by date
            if home_team in home_dict:
                home_dict[home_team].append(temp_home_lst)
                home_dict[home_team].sort(key=lambda x: datetime.strptime(x[-1], '%m/%d/%Y'))
            else:
                home_dict[home_team] = [temp_home_lst]

            # Creates the list of away team game statistics
            temp_away_lst = lst[15:29]
            temp_away_lst.extend(lst[1:15])
            temp_away_lst.append(lst[29])
            temp_away_lst.append(lst[0])

            # Adds the away team game to away game dictionary and sorts it by date
            if away_team in away_dict:
                away_dict[away_team].append(temp_away_lst)
                away_dict[away_team].sort(key=lambda x: datetime.strptime(x[-1], '%m/%d/%Y'))
            else:
                away_dict[away_team] = [temp_away_lst]

            # Appends the home team, away team, and date to the schedule and sorts it
            schedule_lst.append([home_team,away_team,lst[0]])
            schedule_lst.sort(key=lambda x: datetime.strptime(x[-1], '%m/%d/%Y'))

    return home_dict, away_dict, schedule_lst

def calc_averages(home_dict,away_dict,schedule_lst):
    """
    Calculates the averages of the team for a game based on the previous games
    :param home_dict: The dictonary with home games of the teams
    :param away_dict: The dictonary with away games of the teams
    :param schedule_lst: List of lists with home and away teams, and game date
    :return: List of lists with the averages of the games
    """
    games_averages = []     # Contains the averages of the all the games

    # Iterates thorugh every game in the schedule
    for game_index, game in enumerate(schedule_lst):
        home_team = game[0]
        away_team = game[1]
        game_date = game[2]

        home_game_date_index = 0    # Index of the list with the game_date in home team values

        # Iterates thorugh the games of the home team
        for home_index, home_val in enumerate(home_dict[home_team]):
            # Processes if the game date is in the 8th game or higher
            if game_date in home_val and home_index > 6:
                home_game_date_index = home_index
                break
            # Stops further processing if the game date is in the first 7 games
            elif game_date in home_val and home_index <= 6:
                home_game_date_index = -1
                break;

        # If the game_date is not found, skips further processing
        if home_game_date_index == -1:
            continue

        away_game_date_index = 0    # Index of the list with the game_date in away team values

        for away_index, away_val in enumerate(away_dict[away_team]):
            # Processes if the game date is in the 8th game or higher
            if game_date in away_val and away_index > 6:
                away_game_date_index = away_index
                break
            # Stops further processing if the game date is in the first 7 games
            elif game_date in away_val and away_index <= 6:
                away_game_date_index = -1
                break;

        # If the game_date is not found, continues
        if away_game_date_index == -1:
            continue

        # Skips further processing if the game date is not in the 8th or the higher game (of away and home)
        if (home_game_date_index <= 6) and (away_game_date_index <= 6):
            continue

        home_averages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # The averages of the home team previous games
        home_opp_averages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # The averages of the home team opponent previous games

        # Calculates the sum of each home team and home team opponents stats in prev. 7 games
        for home_index, home_val in enumerate(home_dict[home_team]):
            if (home_game_date_index-7) <= home_index < home_game_date_index:
                for k in range(0, len(home_val)):
                    if k <= 12:
                        home_averages[k] += float(home_val[k + 1])
                    elif 14 <= k <= 26:
                        home_opp_averages[k-14] += float(home_val[k + 1])

        away_averages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # The averages of the away team previous games
        away_opp_averages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # The averages of the away team opponent previous games

        # Calculates the sum of each away team and away team opponents stats in prev. 7 games
        for away_index, away_val in enumerate(away_dict[away_team]):
            if (away_game_date_index - 7) <= away_index < away_game_date_index:
                for k in range(0, len(away_val)):
                    if k <= 12:
                        away_averages[k] += float(away_val[k + 1])
                    elif 14 <= k <= 26:
                        away_opp_averages[k - 14] += float(away_val[k + 1])

        # Calculates the averages of each stat and rounds to 2 decimal points
        num_games = 7
        for k in range(0, 13):
            home_averages[k] = round(home_averages[k] / num_games, 2)
            home_opp_averages[k] = round(home_opp_averages[k] / num_games, 2)
            away_averages[k] = round(away_averages[k] / num_games, 2)
            away_opp_averages[k] = round(away_opp_averages[k] / num_games, 2)

        # Create a list of the game average and appends to the master game averages list
        averages = home_averages
        averages.extend(home_opp_averages)
        averages.extend(away_averages)
        averages.extend(away_opp_averages)
        averages.append(home_dict[home_team][home_game_date_index][-2])
        games_averages.append(averages)

    return games_averages

def write_games_averages(games_averages, output_file):
    """
    Writes the averages of games into a file
    :param games_averages: List of lists with all the game averages
    :param output_file: File to write out the game averages to
    :return: None
    """
    outfile = open(output_file, "w")

    # Prints out the features rounded to 2 decimal points followed by a comma
    for g in games_averages:
        for i in range(0,len(g)):
            if i+1 != len(g):
                try:
                    print(round(float(g[i]),2), end=",",file=outfile)
                except:
                    print(g[i], end=",", file=outfile)
            elif i+1 == len(g):
                print(g[i], end="\n",file=outfile)

    outfile.close()

def main():
    """
    Processes the games, calculates the averages, and writes it out
    :return: None
    """

    # Reads the train game data, calculates the averages and writes it to train_averages file
    train_fp = open_file()
    train_home_dict,train_away_dict,train_schedule_lst = read_file(train_fp)
    train_games_averages = calc_averages(train_home_dict,train_away_dict,train_schedule_lst)
    write_games_averages(train_games_averages,"train_averages.txt")

    # Reads the test game data, calculates the averages and writes it to test_averages file
    test_fp = open_file()
    test_home_dict, test_away_dict, test_schedule_lst = read_file(test_fp)
    test_games_averages = calc_averages(test_home_dict, test_away_dict, test_schedule_lst)
    write_games_averages(test_games_averages,"test_averages.txt")

if __name__ == "__main__":
    main()
