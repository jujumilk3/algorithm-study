def solution(spell, dic):
    spell_set = set(spell)
    for d in dic:
        if spell_set.issubset(set(d)):
            return 1
    return 2
