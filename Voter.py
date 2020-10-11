from faker import Factory
import mechanize
import time
import sys

#Constants used for a particular voting website. Change as needed
URL = "https://poll.fm/10615673"
FORM_ID = 10615673
VOTE_FIELD = ".vote-button"
VOTE_ID = "d568756848e685381de4757ead24dc93"
#EMAIL_ID = ''
#End constants

def main():
    if len(sys.argv) == 1:
        print("Please provide an argument for the number of votes")
        exit(1)

    MAX_VOTES = int(sys.argv[1])
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [("User-agent","Mozilla/5.0")]
    for i in range(0,MAX_VOTES):
        faker = Factory.create()
        votebot = br.open(URL)
        br.select_form(nr=FORM_ID)
        control = br.form.find_control(VOTE_FIELD)
        for item in control.items:
            if item.name == VOTE_ID:
                item.selected = True
        email = faker.email()
        br.form[EMAIL_ID] = email
        print("%s (%d)"%(email,i+1))
        result = br.submit()

if __name__=="__main__":
    main()