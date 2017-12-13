import nba_py
from nba_py import team, game, constants, player
import json
import os
from datetime import date, timedelta
import time
import sys

FILE_PATHES = ['scoreboards', 'games', 'logs']
GAME_CONFIGS = ['PlayByPlay', 'HustleStats', 'PlayByPlayV2']
PLAYER_CONFIGS = {
    "PlayerSummary": {
        "params": ["player_id"],
        "path": ["season", "player_name"]
    },
    "PlayerCareer": {
        "params": ["player_id"],
        "path": ["season", "player_name"]
    },
    "PlayerProfile": {
        "params": ["player_id"],
        "path": ["season", "player_name"]
    },
    "PlayerGameLogs": {
        "params": ["player_id", "season"],
        "path": ["season", "player_name"]
    },
    "PlayerGeneralSplits": {
        "params": ["player_id", "season", "season_type", "measure_type"],
        "path": ["season", "player_name", "season_type"]
    },
    "PlayerOpponentSplits": {
        "params": ["player_id", "season", "season_type", "measure_type"],
        "path": ["season", "player_name", "season_type"]
    },
    "PlayerLastNGamesSplits": {
        "params": ["player_id", "season", "season_type", "measure_type"],
        "path": ["season", "player_name", "season_type"]
    },
    "PlayerInGameSplits": {
        "params": ["player_id", "season", "season_type", "measure_type"],
        "path": ["season", "player_name", "season_type"]
    },
    "PlayerClutchSplits": {
        "params": ["player_id", "season", "season_type", "measure_type"],
        "path": ["season", "player_name", "season_type"]
    },
    "PlayerShootingSplits": {
        "params": ["player_id", "season", "season_type", "measure_type"],
        "path": ["season", "player_name", "season_type"]
    },
    "PlayerPerformanceSplits": {
        "params": ["player_id", "season", "season_type", "measure_type"],
        "path": ["season", "player_name", "season_type"]
    },
    "PlayerYearOverYearSplits": {
        "params": ["player_id", "season", "season_type", "measure_type"],
        "path": ["season", "player_name", "season_type"]
    },
    "PlayerShotTracking": {
        "params": ["player_id", "season", "season_type", "measure_type"],
        "path": ["season", "player_name", "season_type"]
    },
    "PlayerReboundTracking": {
        "params": ["player_id", "season", "season_type", "measure_type"],
        "path": ["season", "player_name", "season_type"]
    },
    "PlayerPassTracking": {
        "params": ["player_id", "season", "season_type", "measure_type"],
        "path": ["season", "player_name", "season_type"]
    },
    "PlayerDefenseTracking": {
        "params": ["player_id", "season", "season_type", "measure_type"],
        "path": ["season", "player_name", "season_type"]
    },
    "PlayerShotLogTracking": {
        "params": ["player_id", "season", "season_type", "measure_type"],
        "path": ["season", "player_name", "season_type"]
    },
    "PlayerReboundLogTracking": {
        "params": ["player_id", "season", "season_type", "measure_type"],
        "path": ["season", "player_name", "season_type"]
    },
}
TEAM_CONFIGS = {
    "TeamSummary": {
        "params": ["team_id", "season", "season_type"],
        "path": ["team_abbr", "season", "season_type"]
    },
    "TeamDetails": {
        "params": ["team_id"],
        "path": ["team_abbr"]
    },
    "TeamCommonRoster": {
        "params": ["team_id", "season"],
        "path": ["team_abbr", "season"]
    },
    "TeamGeneralSplits": {
        "params": ["team_id", "season", "season_type", "measure_type"],
        "path": ["team_abbr", "season", "season_type"]
    },
    "TeamOpponentSplits": {
        "params": ["team_id", "season", "season_type", "measure_type"],
        "path": ["team_abbr", "season", "season_type"]
    },
    "TeamLastNGamesSplits": {
        "params": ["team_id", "season", "season_type", "measure_type"],
        "path": ["team_abbr", "season", "season_type"]
    },
    "TeamInGameSplits": {
        "params": ["team_id", "season", "season_type", "measure_type"],
        "path": ["team_abbr", "season", "season_type"]
    },
    "TeamClutchSplits": {
        "params": ["team_id", "season", "season_type", "measure_type"],
        "path": ["team_abbr", "season", "season_type"]
    },
    "TeamShootingSplits": {
        "params": ["team_id", "season", "season_type", "measure_type"],
        "path": ["team_abbr", "season", "season_type"]
    },
    "TeamPerformanceSplits": {
        "params": ["team_id", "season", "season_type", "measure_type"],
        "path": ["team_abbr", "season", "season_type"]
    },
    "TeamLineups": {
        "params": ["team_id", "season", "season_type", "measure_type"],
        "path": ["team_abbr", "season", "season_type"]
    },
    "TeamPlayers": {
        "params": ["team_id", "season", "season_type", "measure_type"],
        "path": ["team_abbr", "season", "season_type"]
    },
    "TeamPlayerOnOffDetail": {
        "params": ["team_id", "season", "season_type", "measure_type"],
        "path": ["team_abbr", "season", "season_type"]
    },
    "TeamPlayerOnOffSummary": {
        "params": ["team_id", "season", "season_type", "measure_type"],
        "path": ["team_abbr", "season", "season_type"]
    },
    "TeamShotTracking": {
        "params": ["team_id", "season", "season_type", "measure_type"],
        "path": ["team_abbr", "season", "season_type"]
    },
    "TeamReboundTracking": {
        "params": ["team_id", "season", "season_type", "measure_type"],
        "path": ["team_abbr", "season", "season_type"]
    },
    "TeamPassTracking": {
        "params": ["team_id", "season", "season_type", "measure_type"],
        "path": ["team_abbr", "season", "season_type"]
    }
}jkkku


def load_json(file_name):
    with open(file_name) as json_data:
        d = json.load(json_data)
        return d


def write_json(file_name, json_data):
    print 'writting:' + file_name
    with open(file_name, 'w') as outfile:
        json.dump(json_data, outfile)
        return json_data
    print 'writting done:' + file_name


def get_all_scoreboards():
    log_path = 'logs/scoreboards.json'
    if not os.path.exists(log_path):
        logs = {}
    else:
        logs = load_json(log_path)
    end_date = date.today()
    start_date = date(2017, 8, 1)
    day_count = (end_date - start_date).days + 1
    for single_date in [
            d for d in (end_date - timedelta(n) for n in range(day_count))
            if d > start_date
    ]:
        day, month, year = (single_date.timetuple().tm_mday,
                            single_date.timetuple().tm_mon,
                            single_date.timetuple().tm_year)
        key = '-'.join([str(year), str(month), str(day)])
        path = 'scoreboards/' + key + '.json'
        if logs.has_key(key):
            continue
        if os.path.exists(path):
            logs[key] = 'Done'
            continue
        try:
            print((day, month, year))
            write_json(path,
                       nba_py.Scoreboard(month=month, day=day, year=year).json)
            logs[key] = 'Done'
            time.sleep(4)
        except Exception as e:
            print e
            logs[key] = e.message
        write_json(log_path, logs)


def get_all_games():
    log_path = 'logs/games.json'
    if not os.path.exists(log_path):
        logs = {}
    else:
        logs = load_json(log_path)
    end_date = date.today()
    start_date = date(2017, 8, 1)
    day_count = (end_date - start_date).days + 1
    for single_date in [
            d for d in (end_date - timedelta(n) for n in range(day_count))
            if d > start_date
    ]:
        day, month, year = (single_date.timetuple().tm_mday,
                            single_date.timetuple().tm_mon,
                            single_date.timetuple().tm_year)
        key = '-'.join([str(year), str(month), str(day)])
        scoreboard_path = 'scoreboards/' + key + '.json'
        scoreboard = load_json(scoreboard_path)
        headers = scoreboard['resultSets'][0]['headers']
        for row in scoreboard['resultSets'][0]['rowSet']:
            game_id, season, home, away = row[2], row[8], row[6], row[7]
            game_path = os.path.join('games', str(season))
            if not os.path.exists(game_path):
                os.makedirs(game_path)
            for method in GAME_CONFIGS:
                try:
                    file_path = os.path.join(game_path, '-'.join(
                        [str(game_id),
                         str(home), str(away), method]) + '.json')
                    if os.path.exists(file_path):
                        continue
                    print file_path
                    write_json(
                        file_path, getattr(game, method)(game_id=game_id).json)
                    time.sleep(3)
                except Exception as e:
                    print e
                    logs[key] = 'Error!'
        write_json(log_path, logs)


def get_all_team_stats():
    log_path = 'logs/teams.json'
    if not os.path.exists(log_path):
        logs = {}
    else:
        logs = load_json(log_path)
    teams_list = team.TeamList()
    measure_types = [
        'Base', 'Advanced', 'Misc', 'Four Factors', 'Scoring', 'Opponent',
        'Usage'
    ]
    write_json('info/team_list.json', teams_list.json)
    for year in range(2016, 1900, -1):
        # if year >= 1999:
        #     continue
        for (league_id, team_id, start_year, end_year,
             team_abbr) in teams_list.info().values:
            if (not team_abbr
                ) or year < int(start_year) or year > int(end_year):
                continue
            season = str(year) + "-" + str(year + 1)[2:]
            for season_type in ['Playoffs', 'Regular Season']:
                path = os.path.join('teams', team_abbr, season, season_type)
                if not os.path.exists(path):
                    os.makedirs(path)
                print team_abbr, season, season_type, team_id
                for method, config in TEAM_CONFIGS.iteritems():
                    types = [None]
                    if 'measure_type' in config['params']:
                        types = measure_types
                    for measure_type in types:
                        file_name = '_'.join([
                            method, measure_type
                        ]) if measure_type else '_'.join([method])
                        dir_names = ['teams'] + [
                            locals()[dir_name] for dir_name in config['path']
                        ] + [file_name + '.json']
                        file_path = os.path.join(*dir_names)
                        if (not os.path.exists(file_path)
                            ) and not logs.has_key(file_path):
                            try:
                                print file_path
                                params = dict([(param, locals()[param])
                                               for param in config['params']])
                                print ', '.join(params)
                                write_json(file_path,
                                           getattr(team,
                                                   method)(**params).json)
                                time.sleep(3)
                            except Exception as e:
                                print e
                                logs[file_path] = 'Error'
                                write_json(log_path, logs)
                    write_json(log_path, logs)


def get_all_player_stats():
    log_path = 'logs/players.json'
    if not os.path.exists(log_path):
        logs = {}
    else:
        logs = load_json(log_path)
    measure_types = [
        'Base', 'Advanced', 'Misc', 'Four Factors', 'Scoring', 'Opponent',
        'Usage'
    ]
    for year in range(2016, 1900, -1):
        season = str(year) + "-" + str(year + 1)[2:]
        dir_path = os.path.join('players', season)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        player_list_path = os.path.join(dir_path, 'player_lists.json')
        player_list = player.PlayerList(season=season, only_current=1)
        write_json(player_list_path, player_list.json)
        for player_data in player_list.json['resultSets'][0]['rowSet']:
            player_id = player_data[0]
            player_name = player_data[2]
            print player_name, season
            for season_type in ['Playoffs', 'Regular Season']:
                for method, config in PLAYER_CONFIGS.iteritems():
                    types = [None]
                    if 'measure_type' in config['params']:
                        types = measure_types
                    for measure_type in types:
                        file_name = '_'.join([
                            method, measure_type
                        ]) if measure_type else '_'.join([method])
                        dir_names = ['players'] + [
                            locals()[dir_name] for dir_name in config['path']
                        ]
                        dir_path = os.path.join(*dir_names)
                        if not os.path.exists(dir_path):
                            os.makedirs(dir_path)
                        file_path = os.path.join(dir_path, file_name + '.json')
                        if (not os.path.exists(file_path)
                            ) and not logs.has_key(file_path):
                            try:
                                print file_path
                                params = dict([(param, locals()[param])
                                               for param in config['params']])
                                print params
                                write_json(file_path,
                                           getattr(player,
                                                   method)(**params).json)
                                time.sleep(3)
                            except Exception as e:
                                print e
                                logs[file_path] = 'Error'
                                write_json(log_path, logs)
                    write_json(log_path, logs)
        time.sleep(3)


if __name__ == "__main__":
    for path in FILE_PATHES:
        if not os.path.exists(path):
            os.makedirs(path)

    if len(sys.argv) > 1:
        if sys.argv[1] == 'team_stats':
            get_all_team_stats()
        elif sys.argv[1] == 'games':
            get_all_games()
        elif sys.argv[1] == 'scoreboards':
            get_all_scoreboards()
        elif sys.argv[1] == 'player_stats':
            get_all_player_stats()

# d = {
#     'player_id': 203112,
#     'season': '2016-17',
#     'measure_type': 'Opponent',
#     'season_type': 'Playoffs'
# }
# getattr(player, 'PlayerShotLogTracking')(**d)
