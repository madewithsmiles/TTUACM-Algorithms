class Solution:
    # Number := Exponent | Decimal
    # Exponent := Decimal e SignedInt
    # Decimal := SignedInt | SignedInt . Integer | +-.Integer | .Integer | SignedInt.
    # SignedInt := Integer | + Integer | - Integer
    # Integer := ' '* [0-9]+ ' '*

    def integer(self, s):
        if not s: return False
        return all([c in '0123456789' for c in s])
    
    def signed_int(self, s):
        if not s: return False
        if self.integer(s): return True
        if s.find(' ') != -1: return False
        return s[0] in '+-' and self.integer(s[1:])
    
    def decimal(self, s):
        s = s.strip()
        if self.signed_int(s): return True
        if s.find(' ') != -1: return False
        p = s.find('.')
        if p == -1: return False
        if p == 0: return self.integer(s[1:])
        if s[0] in '+-' and p == 1: return self.integer(s[2:])
        if s[-1] == '.': return self.signed_int(s[:-1])
        return self.signed_int(s[:p]) and self.integer(s[p+1:])
    
    def exponent(self, s):
        s = s.strip()
        if s.find(' ') != -1: return False
        e = s.find('e')
        if e <= 0: return False
        return self.decimal(s[:e]) and self.signed_int(s[e+1:])
        
    
    def isNumber(self, s):
        return self.exponent(s) or self.decimal(s)
        
