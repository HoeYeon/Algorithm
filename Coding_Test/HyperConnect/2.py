def isLowerEng(s):
    return s.islower() and s.isalpha()


def isName(name):
    return all(isLowerEng(x) for x in name.split("."))


def isDomain(s):
    domains = ["net", "org", "com"]
    return s in domains


def isEmail(email):
    return isDomain(email[2]) and isLowerEng(email[1]) and isName(email[0])


def solution(emails):
    answer = 0
    for email in emails:
        tmp = email.split("@")
        if len(tmp) != 2 or "." not in tmp[1]:
            continue
        email = [tmp[0], *tmp[1].split(".")]
        if isEmail(email):
            answer += 1

    return answer
