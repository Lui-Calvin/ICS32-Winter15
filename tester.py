"""
class Steven(Exception):
    pass
        
class EthanError(Exception):
    def __init__(self,expr,msg):
        self.expr = expr
        self.msg = msg
try:
    raise EthanError("fdbvfbsjvds","gay")
except EthanError as e:
    print('hi')
    print(e.expr)
    print(e.msg)
    
    raise
"""


