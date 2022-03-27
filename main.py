# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

number_of_teams = 17

def create_team_name_json_map(name):
    # Use a breakpoint in the code line below to debug your script.
    f = open('races/bahrain/bahrain.json')
    d = json.load(f)
    teams = d['leaderboard']['leaderboard_entrants']
    print(teams)
    idx = 0
    dick = {}
    for team in teams:
        dick[team['team_name']] = idx
        idx += 1

    print(dick)


def create_list_of_teams():
    # Use a breakpoint in the code line below to debug your script.
    f = open('races/bahrain/bahrain.json')
    d = json.load(f)
    teams = d['leaderboard']['leaderboard_entrants']
    dick = []
    for team in teams:
        dick.append(team['team_name'])

    return dick


def create_score_mapping():
    scores = [0] * number_of_teams
    for team in teams:
        scores[team_mapping[team['team_name']]] = team['score']

    return scores


def write_scores_to_file():
    file_dir = 'races' + '/' + race + '/' + race + '_scores' + '.json'
    print(file_dir)
    f = open(file_dir, "w")
    for score in race_scores:
        f.write(str(score) + '\n')


def get_total_from_races_json():
    file_dir = 'stuff/race_mapping_json.json'
    f = open(file_dir, 'r')
    lines = f.readlines()
    total_scores = [0] * number_of_teams
    for line in lines:
        race_scores2 = get_scores_from_race(line.strip()[1:-1])
        for idx, score in enumerate(race_scores2):
            total_scores[idx] += score

    return total_scores


def get_scores_from_race(race_name):
    scores_list = []
    file_dir = 'races' + '/' + race_name + '/' + race_name + '_scores' + '.json'
    print(file_dir)
    f = open(file_dir, 'r')
    lines = f.readlines()
    for line in lines:
        scores_list.append(int(line.strip()))

    return scores_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    race = 'bahrain'
    race_json = open('races/bahrain/bahrain.json')
    team_mapping_json = open('stuff/team_name_order_mapping.json')
    race_data = json.load(race_json)
    teams = race_data['leaderboard']['leaderboard_entrants']
    team_mapping = json.load(team_mapping_json)
    race_scores = create_score_mapping()
    write_scores_to_file()
    teams_list = create_list_of_teams()
    print(teams_list)
    da_scores = get_total_from_races_json()
    print(da_scores)
    # d = {"col": da_scores}

    df = pd.DataFrame({'scores': da_scores, 'teams': teams_list})
    x_pos = [i for i, _ in enumerate(teams_list)]

    colors = ['#B0171F',
              '#EEA2AD',
              '#B452CD',
              '#0000FF',
              '#C6E2FF',
              '#00C5CD',
              '#00FA9A',
              '#00EE00',
              '#CDCD00',
              '#EEB422',
              '#B3B3B3',
              '#050505',
              '#C67171',
              '#9C661F',
              '#8B8989',
              '#F5F5DC',
              '#9A32CD']

    plt.figure(figsize=(20, 10))
    plt.barh(x_pos, da_scores[::-1], color=colors)

    plt.ylabel("team names")
    plt.xlabel("scores")
    plt.title("Bahrain")
    plt.yticks(x_pos, teams_list[::-1])
    plt.savefig("test")
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
