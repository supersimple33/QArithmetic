# QArithmetic
Arithmetic library for IBM Qiskit

This is our great, awesome, extremely impressive, daunting, inspiring arithmetic library.

List of operations implemented:


## Bit-wise operations

#### Logical AND (qc, a, b, c, N)

    qc->quantum circuit, a->input1, b->input2, c->output, N->bit-string length

#### Logical OR (qc, a, b, c, N)

    qc->quantum circuit, a->input1, b->input2, c->output, N->bit-string length

#### Logical XOR (qc, a, b, c, N)

    qc->quantum circuit, a->input1, b->input2, c->output, N->bit-string length

#### Logical NOT (qc, a, c, N)

    qc->quantum circuit, a->input, c->output, N->bit-string length

#### Shift right (qc,reg,N,shift)

    qc->quantum circuit, reg->shift register, N->shift register bit-length, shift->shift amount

#### Shift left (qc,reg,N,shift)

    qc->quantum circuit, reg->shift register, N->shift register bit-length, shift->shift amount


## Arithmetic operations

#### QFT-based add (Draper adder)

> *Source*: [Khosropour, A., Aghababa, H., & Forouzandeh, B. (2011). Quantum Division Circuit Based on Restoring Division Algorithm. 2011 Eighth International Conference on Information Technology: New Generations. doi:10.1109/itng.2011.177 ](https://www.researchgate.net/publication/220840968_Quantum_Division_Circuit_Based_on_Restoring_Division_Algorithm)


#### Ripple carry add

> *Source*: [Vedral, V., Barenco, A., & Ekert, A. (1996). Quantum networks for elementary arithmetic operations. Physical Review A, 54(1), 147](https://arxiv.org/abs/quant-ph/9511018).


#### QFT-based sub

Uses the QFT-based adder and the fact that

    a - b = ~(~a + b)

#### Ripple carry sub

Uses the ripple-carry adder and the fact that

    a - b = ~(~a + b)

#### Multiply & Controlled Multiply

> *Source*: [Nguyen, A. Q. (2004). TR-2004010: Optimal Reversible Quantum Circuit for Multiplication](https://pdfs.semanticscholar.org/9c3e/9f842537c1375ba80412b42f3e8868ebd2ba.pdf).


#### Divide

> *Source*: [Khosropour, A., Aghababa, H., & Forouzandeh, B. (2011). Quantum Division Circuit Based on Restoring Division Algorithm. 2011 Eighth International Conference on Information Technology: New Generations. doi:10.1109/itng.2011.177](https://www.researchgate.net/publication/220840968_Quantum_Division_Circuit_Based_on_Restoring_Division_Algorithm)

#### Square (qc, a, b)

Uses a custom implementation of QFT-based controlled adder

  a ^ 2 = a\*2<sup>0</sup> + a\*2<sup>1</sup> + .... + a\*2<sup>n-2</sup> + a\*2<sup>n-1</sup>

#### Power (qc, a, b, c)

Uses the QFT-adder based cmult and the fact that

  a ^ b = a<sub>0</sub> * a<sub>1</sub> * .... * a<sub>b-2</sub> * a<sub>b-1</sub>
