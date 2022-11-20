# This is a comment
"""
Another comment 
""" 
"Comment!"

# ARITHMETIC OPERATIONS ======================================

a = 2 ** 3
b = 2 + 3 
c = 3 - 4
d = 22/8 
e = 22//8   # Divisão inteira 
f = 23%2    # Resto da divisão de 23 por 2 eh 1
g = 23*2
h = 23*(2+1)
# print(h) 


# STRING OPERATIONS ======================================

alice = "Alice"
safada = 'safada'
safada_size = len(safada)       # Quantas letras tem safada

soma = alice + " " + safada     # add strings 
mult = alice * 5 
# mult_string = alice * safada  # ERROR!
# soma_int = alice + 42         # ERROR!
soma_int = alice + str(a) 
print(safada_size)

# FORMAT STRINGS =========================================

flotao = 82.25454654564684685
posicao = 2.3123123
n = 1 
format_ = "{} {}".format(alice, safada)
format_ = "{:.2f}".format(flotao)   
formatao = "%s %s" %(alice, safada)
formatao_float = "%.2f" %(flotao)
formatao = "%f %d" %(flotao, n)
formatao = "Posicao: %.2f" %(posicao)
formatao = f'Posicao {posicao:.2f}'

#print(soma_int)
#print(mult)
#print(soma)
#print(format_)
#print(formatao)
#print(formatao_float)

# INPUTS ==================================================

# Get string ---
#name = input("What's your name?\n")
#print(name)

# Get integer ---
#person_age = int(input("What's your age?\n"))
#print("{} age is {}".format(name,person_age))

# Get float ----
#person_age = float(input("What's your age?\n"))
#print("{} age is {}".format(name,person_age))