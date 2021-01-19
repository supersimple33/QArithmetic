from math import pi
from qiskit import QuantumRegister, QuantumCircuit, AncillaRegister
from qft import qft, iqft, cqft, ciqft, ccu1

################################################################################
# Bitwise Operators
################################################################################

# bit-wise operations
def bitwise_and(qc, a, b, c, N):
    for i in range(0, N):
        qc.ccx(a[i], b[i], c[i])

def bitwise_or(qc, a, b, c, N):
    for i in range(0, N):
        qc.ccx(a[i], b[i], c[i])
        qc.cx(a[i], c[i])
        qc.cx(b[i], c[i])

def bitwise_xor(qc, a, b, c, N):
    for i in range(0, N):
        qc.cx(a[i], c[i])
        qc.cx(b[i], c[i])

def bitwise_not(qc, a, c, N):
    for i in range(0, N):
        qc.cx(a[i], c[i])
        qc.x(c[i])

# Cyclically left-shifts a binary string "a" of length n.
# If "a" is zero-padded, equivalent to multiplying "a" by 2.
def lshift(circ, a, n):
    # Iterate through pairs and do swaps.
    for i in range(n,1,-1):
        circ.swap(a[i-1],a[i-2])

# Cyclically right-shifts a binary string "a" of length n.
# If "a" is zero-padded, equivalent to dividing "a" by 2.
def rshift(circ, a, n):
    # Iterate through pairs and do swaps.
    for i in range(n-1):
        circ.swap(a[i],a[i+1])

################################################################################
# Controlled-Toffoli, or Controlled-Controlled-Controlled-NOT
################################################################################

# Define a controlled Toffoli gate
def cccx(circ,ctrl,a,b,c):
    anc = QuantumRegister(1)
    circ.add_register(anc[0])
    circ.ccx(ctrl,a,anc[0])
    circ.ccx(b,anc[0],c)
    circ.ccx(ctrl,a,anc[0])
    circ.ccx(b,anc[0],c)

################################################################################
# Addition Circuits
################################################################################

# Define some functions for the ripple adder.
def sum(circ, cin, a, b):
    circ.cx(a,b)
    circ.cx(cin,b)

def carry(circ, cin, a, b, cout):
    circ.ccx(a, b, cout)
    circ.cx(a, b)
    circ.ccx(cin, b, cout)

def carry_dg(circ, cin, a, b, cout):
    circ.ccx(cin, b, cout)
    circ.cx(a, b)
    circ.ccx(a, b, cout)

# Draper adder that takes |a>|b> to |a>|a+b>.
# |a> has length x and is less than or equal to n
# |b> has length n+1 (left padded with a zero).
# https://arxiv.org/pdf/quant-ph/0008033.pdf
def add(circ, a, b, n):
    # move n forward by one to account for overflow
    n += 1

    # Take the QFT.
    qft(circ, b, n)

    # Compute controlled-phases.
    # Iterate through the targets.
    for i in range(n,0,-1):
        # Iterate through the controls.
        for j in range(i,0,-1):
            # If the qubit a[j-1] exists run ccu, if not assume the qubit is 0 and never existed
            if len(a) - 1 >= j - 1:
                circ.cu1(2*pi/2**(i-j+1), a[j-1], b[i-1])

    # Take the inverse QFT.
    iqft(circ, b, n)

# Draper adder that takes |a>|b> to |a>|a+b>, controlled on |c>.
# |a> has length x and is less than or equal to n
# |b> has length n+1 (left padded with a zero).
# |c> is a single qubit that's the control.
def cadd(circ, c, a, b, n):
    # move n forward by one to account for overflow
    n += 1

    # Take the QFT.
    cqft(circ, c, b, n)

    # Compute controlled-phases.
    # Iterate through the targets.
    for i in range(n,0,-1):
        # Iterate through the controls.
        for j in range(i,0,-1):
            # If the qubit a[j-1] exists run ccu, if not assume the qubit is 0 and never existed
            if len(a) - 1 >= j - 1:
                ccu1(circ, 2*pi/2**(i-j+1), c, a[j-1], b[i-1])

    # Take the inverse QFT.
    ciqft(circ, c, b, n)

# Adder that takes |a>|b> to |a>|a+b>.
# |a> has length n.
# |b> has length n+1.
# Based on Vedral, Barenco, and Ekert (1996).
def add_ripple(circ, a, b, n):
    # Create a carry register of length n.
    c = QuantumRegister(n)
    circ.add_register(c)

    # Calculate all the carries except the last one.
    for i in range(0, n-1):
        carry(circ, c[i], a[i], b[i], c[i+1])

    # The last carry bit is the leftmost bit of the sum.
    carry(circ, c[n-1], a[n-1], b[n-1], b[n])

    # Calculate the second-to-leftmost bit of the sum.
    circ.cx(c[n-1],b[n-1])

    # Invert the carries and calculate the remaining sums.
    for i in range(n-2,-1,-1):
        carry_dg(circ, c[i], a[i], b[i], c[i+1])
        sum(circ, c[i], a[i], b[i])

# Adder that takes |a>|b>|0> to |a>|b>|a+b>.
# |a> has length n. 
# |b> has length n.
# |s> = |0> has length n+1.
def add_ripple_ex(circ, a, b, s, n):
    # Copy b to s.
    for i in range(0, n):
        circ.cx(b[i],s[i])

    # Add a and s.
    add_ripple(circ, a, s, n)


################################################################################
# Subtraction Circuits
################################################################################

# Subtractor that takes |a>|b> to |a>|a-b>.
# |a> has length n+1 (left padded with a zero).
# |b> has length n+1 (left padded with a zero).
def sub(circ, a, b, n):
    # Flip the bits of a.
    circ.x(a)

    # Add it to b.
    add(circ, a, b, n - 1)

    # Flip the bits of the result. This yields the sum.
    circ.x(b)

    # Flip back the bits of a.
    circ.x(a)

# Subtractor that takes |a>|b> to |a-b>|b>.
# |a> has length n+1 (left padded with a zero).
# |b> has length n+1 (left padded with a zero).
def sub_swap(circ, a, b, n):
    # Flip the bits of a.
    circ.x(a)

    # Add it to b.
    add(circ, b, a, n - 1)

    # Flip the bits of the result. This yields the sum.
    circ.x(a)

# Subtractor that takes |a>|b> to |a>|a-b>.
# |a> has length n.
# |b> has length n+1.
def sub_ripple(circ, a, b, n):
    # We add "a" to the 2's complement of "b."
    # First flip the bits of "b."
    circ.x(b)

    # Create a carry register of length n.
    c = QuantumRegister(n)
    circ.add_register(c)

    # Add 1 to the carry register, which adds 1 to b, negating it.
    circ.x(c[0])

    # Calculate all the carries except the last one.
    for i in range(0, n-1):
        carry(circ, c[i], a[i], b[i], c[i+1])

    # The last carry bit is the leftmost bit of the sum.
    carry(circ, c[n-1], a[n-1], b[n-1], b[n])

    # Calculate the second-to-leftmost bit of the sum.
    circ.cx(c[n-1],b[n-1])

    # Invert the carries and calculate the remaining sums.
    for i in range(n-2,-1,-1):
        carry_dg(circ, c[i], a[i], b[i], c[i+1])
        sum(circ, c[i], a[i], b[i])

    # Flip the carry to restore it to zero.
    circ.x(c[0])


# Subtractor that takes |a>|b>|0> to |a>|b>|a-b>.
# |a> has length n.
# |b> has length n.
# |s> = |0> has length n+1.
def sub_ripple_ex(circ, a, b, s, n):
    # Copy b to s.
    for i in range(0, n):
        circ.cx(b[i],s[i])

    # Subtract a and s.
    sub_ripple(circ, a, s, n)

################################################################################
# Multiplication Circuit
################################################################################

# Controlled operations

# Take a subset of a quantum register from index x to y, inclusive.
def sub_qr(qr, x, y):
    sub = []
    for i in range (x, y+1):
        sub = sub + [(qr[i])] # I think this was supposed to point to specific qubits
    return sub

def full_qr(qr):
    return sub_qr(qr, 0, len(qr) - 1)

# Computes the product c=a*b.
# a has length n.
# b has length n.
# c has length 2n.
def mult(circ, a, b, c, n):
    for i in range (0, n):
        cadd(circ, a[i], b, sub_qr(c, i, n+i), n)

# Computes the product c=a*b if and only if control.
# a has length n.
# b has length n.
# control has length 1.
# c has length 2n.
def cmult(circ, control, a, b, c, n):
    qa = QuantumRegister(len(a))
    qb = QuantumRegister(len(b))
    qc = QuantumRegister(len(c))
    tempCircuit = QuantumCircuit(qa, qb, qc)
    mult(tempCircuit, qa, qb, qc, n)
    tempCircuit = tempCircuit.control(1) #Add Decomposition after pull request inclusion #5446 on terra
    print("Remember To Decompose after release >0.16.1")
    circ.compose(tempCircuit, qubits=full_qr(control) + full_qr(a) + full_qr(b) + full_qr(c), inplace=True)

################################################################################
# Division Circuit
################################################################################

# Divider that takes |p>|d>|q>.
# |p> is length 2n and has n zeros on the left: 0 ... 0 p_n ... p_1.
# |d> has length 2n and has n zeros on the right: d_2n ... d_{n+1) 0 ... 0.
# |q> has length n and is initially all zeros.
# At the end of the algorithm, |q> will contain the quotient of p/d, and the
# left n qubits of |p> will contain the remainder of p/d.
def div(circ, p, d, q, n):
    # Calculate each bit of the quotient and remainder.
    for i in range(n,0,-1):
        # Left shift |p>, which multiplies it by 2.
        lshift(circ, p, 2*n)

        # Subtract |d> from |p>.
        sub_swap(circ, p, d, 2*n)

        # If |p> is positive, indicated by its most significant bit being 0,
        # the (i-1)th bit of the quotient is 1.
        circ.x(p[2*n-1])
        circ.cx(p[2*n-1], q[i-1])
        circ.x(p[2*n-1])

        # If |p> is negative, indicated by the (i-1)th bit of |q> being 0, add D back
        # to P.
        circ.x(q[i-1])
        cadd(circ, q[i-1], d, p, 2*n - 1)
        circ.x(q[i-1])

################################################################################
# Expontential Circuit
################################################################################

# a has length n
# b has length v
# finalOut has length n*((2^v)-1), for safety
def power(circ, a, b, finalOut): #Because this is reversible/gate friendly memory blooms to say the least
    # Track Number of Qubits
    n = len(a)
    v = len(b)

    # Left 0 pad a, to satisfy multiplication function arguments
    aPad = AncillaRegister(2)
    circ.add_register(aPad)
    padAList = full_qr(aPad)
    aList = full_qr(a)
    a = aList + padAList

    # Create a register d for mults and init with state 1
    d = AncillaRegister(len(finalOut)) # Unsure of where to Anciallas these
    circ.add_register(d)

    # Set d to 1
    circ.x(d[0])
    
    # Create zero bits
    num_recycle = 2
    permaZeros = []
    if num_recycle > 0:
        permaZeros = AncillaRegister(num_recycle) #8
        circ.add_register(permaZeros)
        permaZeros = full_qr(permaZeros)
        finalOut = full_qr(finalOut) + permaZeros

    r = 2
    # iterate through every qubit of b
    for i in range(0,v): # for every bit of b 
        cmult(circ, [b[i]], a[:r], d[:r], finalOut[:r * 2], r)
        circ.cswap([b[i]], d[:r*2], finalOut[:r * 2])

        r *= 2