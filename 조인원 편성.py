import numpy as np
from scipy.sparse import dok_matrix
n_players = 20
team_size = 4
max_iterations = 10000
def update_adjacency_matrix(adjacency_matrix, team_membership, ex='-'):
    total_weight=0
    for i in range(n_players):
        for j in range(i + 1, n_players):
            if team_membership[i] == team_membership[j]:
                if ex=='-' :
                    if adjacency_matrix[j, i] > 0 and adjacency_matrix[i, j] > 0:
                        adjacency_matrix[i, j] -= 10
                        adjacency_matrix[j, i] -= 10
                    if adjacency_matrix[j, i] <=0 and adjacency_matrix[i, j] <=0 :
                        adjacency_matrix[j, i], adjacency_matrix[i, j]=-9999,-9999
                    total_weight+=adjacency_matrix[i,j]

                else :
                    adjacency_matrix[i, j] += 10
                    adjacency_matrix[j, i] += 10
    if ex=='-' :
        return adjacency_matrix, total_weight
    else :
        return adjacency_matrix

def create_random_teams(n_players, team_size):
    return np.random.permutation(n_players) % (n_players // team_size)

def optimize_teams(n_players, team_size, adjacency_matrix, members):
    min_weight = 0
    best_team_membership = None

    for _ in range(max_iterations):
        team_membership = create_random_teams(n_players, team_size)
        #print(team_membership)
        adjacency_matrix, total_weight = update_adjacency_matrix(adjacency_matrix, team_membership)
        adjacency_matrix = update_adjacency_matrix(adjacency_matrix, team_membership, ex="+")
        if total_weight > min_weight:
            print(f"갱신된 최적값 : {total_weight}")
            min_weight = total_weight
            best_team_membership = team_membership
    adjacency_matrix = update_adjacency_matrix(adjacency_matrix, team_membership)
    return min_weight, best_team_membership

def print_teams(team_membership, members):
    teams = [[] for _ in range(5)]
    for i, member in enumerate(members):
        teams[team_membership[i]].append(member)

    for i, team in enumerate(teams, start=1):
        print(f"팀{i} : {team}")

def main():
    members = ["ㄱㅇㅇ", "ㄱㅎㅇ", "ㅂㅎㅈ", "ㄱㅇㅅ", "ㄱㅁㅅ", "ㅇㅎㅇ" "ㅇㅅㅁ", "ㄱㄱㄹ", "ㅇㅅㅇ", "ㅇㅅㅁ",
               "ㅂㅈㅇ", "ㅅㅇㄹ", "ㅇㅎㅇ", "ㅇㅅㅇ", "ㅇㅇㅅ", "ㅈㅈㅇ", "ㅇㅎㄱ", "ㅁㄴㅇ", "ㅇㅇㅅ", "ㄱㄷㅎ"]
    adjacency_matrix = dok_matrix((n_players, n_players), dtype=int)
    for i in range(n_players):
        for j in range(i + 1, n_players):
                adjacency_matrix[i, j] = 30
                adjacency_matrix[j, i] = 30
    for i in range(20):
        min_weight, best_team_membership = optimize_teams(n_players, team_size, adjacency_matrix, members)

        print("최적화 팀 생성:")
        print_teams(best_team_membership, members)
        print(adjacency_matrix.toarray())
        print(f"팀 가중치 (가중치 최소값 {min_weight})")

if __name__ == "__main__":
    main()
