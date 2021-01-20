# QArithmetic
Arithmetic library for IBM Qiskit

This is our great, awesome, extremely impressive, daunting, inspiring arithmetic library.

List of operations implemented:


## Bit-wise operations

#### Controlled Toffoli gate (qc,ctrl,a,b,c)

    qc->quantum circuit, ctrl->control bit, a->toffoli control input1, b->toffoli control input2, c->target qubit


> *Source*: [O. Scott, Nathan & Dueck, G.W.. (2008). Pairwise decomposition of toffoli gates in a quantum circuit. 231-236. 10.1145/1366110.1366168](https://www.researchgate.net/publication/220904774_Pairwise_decomposition_of_toffoli_gates_in_a_quantum_circuit). 

#### Multiple Controlled Not gate (qc,ctrl,a...n, z)

    qc->quantum circuit, ctrl->control bit, a->toffoli control input ... n->toffoli control input, z->target qubit


> *Source*: [Barenco, Adriano and Bennett, Charles H. and Cleve, Richard and DiVincenzo, David P. and Margolus, Norman and Shor, Peter and Sleator, Tycho and Smolin, John A. and Weinfurter, Harald. (1995). Elementary gates for quantum computation. 3457–3467. 10.1103/physreva.52.3457](http://dx.doi.org/10.1103/PhysRevA.52.3457). 
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

#### Power (qc, a, b, c)

Uses the QFT-adder based cmult and the fact that

  a ^ b = a<sub>0</sub> * a<sub>1</sub> * .... * a<sub>b-2</sub> * a<sub>b-1</sub>
