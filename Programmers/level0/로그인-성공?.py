def solution(id_pw, db):
    id_matched = False
    for row in db:
        if id_pw == row:
            return "login"
        id_matched = id_pw[0] == row[0] if id_matched is False else id_matched
    return "wrong pw" if id_matched else "fail"
