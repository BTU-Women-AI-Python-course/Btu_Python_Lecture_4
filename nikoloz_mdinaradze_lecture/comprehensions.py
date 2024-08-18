# [<expression> for <item> in <iterable> if <condition>]
list1 = [n**2 for n in range(100) if n % 2==0]

# {<key_expression>: <value_expression> for <item> in <iterable> if <condition>}
dict1 = {"key"+str(n):"value"+str(n) for n in range(10) if n%2==1}
