def greet(name):
    print(f"WELCOME TO PARTY, {name}!!")

def talk(name):
    print(f"Hey, {name}! How are you?")

def invite_to_dinner():
    print('We are having a dinner tonight. Please come over.')

def goodbye(name, score):
    print(f"Thanks for coming, see you next time, {name}.")
    if score > 5:
        return True
    else:
        return False


def test_review_dinner():
    greet("John")
    talk("John")
    invite_to_dinner()
    satisfied = goodbye("John", 6) 
    assert satisfied == True
 
def test_review_dinner_negative():
    greet("John")
    talk("John")
    invite_to_dinner()
    satisfied = goodbye("John", 4) 
    assert satisfied == True

