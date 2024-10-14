def te_at_either_end(string):
    """Forgot the DS first go!"""
    if string[-2:] == "te" or string[:2] == "te":
        return True
    else:
        return False
#Test
print(te_at_either_end('Ping Pong'))
print(te_at_either_end('pattzte'))
print(te_at_either_end('tegolsr'))
