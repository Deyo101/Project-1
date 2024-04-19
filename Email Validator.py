import re
def fun(s):
    while True:
        user = None
        web = None
        ext = None
        valid = None
        if "@" in s:
            user_and_dom = s.split("@")
            user = user_and_dom[0]
            dom = user_and_dom[1]
            if "." in dom:
                web_and_ext = dom.split(".")
                web = web_and_ext[0]
                ext = web_and_ext[1]
            else:
                valid = False
        else:
            valid = False
    
        pattern = r'^[a-zA-Z0-9_-]+$'
        pattern2 = r'^[a-zA-Z0-9]+$'

        if (re.search(pattern, user)):
            if (re.search(pattern2, web)):
                if len(ext) <= 3 and ext.isalpha():
                    valid = True
                else:
                    valid = False
            else:
                valid = False
        else:
            valid = False
        return valid


    # return True if s is a valid email, else return False



def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


