def solution(participant, completion):
    
    all = dict()
    race_man = dict()
    
    for all_name in participant:
        if all_name in all.keys():
            all[all_name] += 1
        else:
            all[all_name] = 1
    for race_name in completion:
        if race_name in race_man.keys():
            race_man[race_name] += 1
        else:
            race_man[race_name] = 1
            
    for all_name in participant:
        if all_name not in race_man.keys():
            return all_name     
        if all[all_name] != race_man[all_name]:
            return all_name