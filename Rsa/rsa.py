from random import randint as cryforhelp


def set_of_random_ints(hero):
    """
    finds two different numbers from 0 to hero (inclusive)
    param: int
    return: int, int
    """
    a = cryforhelp(0, hero)
    b = cryforhelp(0, hero)
    if a is b:
        a, b = set_of_random_ints(hero)
    return a, b


def is_prime(x):
    """
    True if prime, else False
    param: int
    return: Boolean
    """
    for i in range(2, int(x/2), 1):
        if x % i == 0:
            return False
    return True


def generate_primes(x):
    """
    finds all primes with x digits and selects two at random
    param: int
    return: int, int
    """
    sol = []
    for i in range(pow(10, x), pow(10, x+1), 1):
        if is_prime(i):
            sol.append(i)
    a, b = set_of_random_ints(len(sol)-1)
    return sol[a], sol[b]


def gcd(a, b):
    """
    eucledian algorithm
    param: int, int
    return: int
    """
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def extgcd(a, b):
    """
    extended eucledian algorithm
    solves: gcd(a,b) = s * a + t * b, returns gcd(a,b), s, t
    param: int, int
    return: int, int, int 
    """
    if b == 0:
        return a, 1, 0
    else:
        g, u, v = extgcd(b, a % b)
        q = a//b
        return g, v, u-q*v


def find_that_e(phi_of_N):
    """
    finds an random int with 1 < int < phi_of_N and where greatest common divisor of int and phi_of_N = 1
    param: int
    return: int
    """
    e = []
    for i in range(2, phi_of_N, 1):
        if gcd(i, phi_of_N) == 1:
            e.append(i)
    return e[cryforhelp(0, len(e)-1)]


def gim_e_the_D(e, phi_of_N):
    """
    solve e * x - y * phi_of_N = 1 and return x
    param: int, int
    return: int
    """
    gcd, s, t = extgcd(e, phi_of_N)
    return s


def rsa_keys(unlimited_power):
    """
    takes in digits of prime numbers to be used
    public key: {N, e}, private key: {q, p, N, phi_of_N, e, d}
    param: int
    return: dict, dict
    """
    q, p = generate_primes(unlimited_power)
    N, phi_of_N = q * p, (q-1) * (p-1)
    e = find_that_e(phi_of_N)
    d = gim_e_the_D(e, phi_of_N)
    return {"N": N, "e": e}, {"q": q, "p": p, "N": N, "phi_of_N": phi_of_N, "e": e, "d": d}


public, private = rsa_keys(3)

message = 2

secret = pow(message, public["e"]) % public["N"]
message = pow(secret, private["d"]) % private["N"]

print("secret: " + str(secret))
print("message: " + str(message))
