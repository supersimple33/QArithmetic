# QArithmetic
Arithmetic library for IBM Qiskit

This is our great, awesome, extremely impressive, daunting, inspiring arithmetic library

List of operations implemented:


# Bit-wise operations

Controlled Toffoli gate (qc,ctrl,a,b,c)

qc->quantum circuit, ctrl->control bit, a->toffoli control input 1, b->toffoli control input 2, c->target qubit

Logical AND (qc, a, b, c, N)

qc->quantum circuit, a->input1, b->input2, c->output, N->bit-string length

Logical OR (qc, a, b, c, N)

qc->quantum circuit, a->input1, b->input2, c->output, N->bit-string length

Logical XOR (qc, a, b, c, N)

qc->quantum circuit, a->input1, b->input2, c->output, N->bit-string length

Logical NOT (qc, a, c, N)

qc->quantum circuit, a->input, c->output, N->bit-string length

Shift right (qc,reg,N,shift)

qc->quantum circuit, reg->shift register, N->shift register bit-length, shift->shift amount

Shift left (qc,reg,N,shift)

qc->quantum circuit, reg->shift register, N->shift register bit-length, shift->shift amount


# Arithmetic operations

QFT-based add (Draper adder)


Ripple carry add

Vedral, V., Barenco, A., & Ekert, A. (1996). Quantum networks for elementary arithmetic operations. Physical Review A, 54(1), 147.


QFT-based sub

Ripple carry sub

Source: Draper, T. G., Kutin, S. A., Rains, E. M., & Svore, K. M. (2004). A logarithmic-depth quantum carry-lookahead adder. arXiv preprint quant-ph/0406142.


Sub-and-swap


Multiply

Source: Nguyen, A. Q. (2004). TR-2004010: Optimal Reversible Quantum Circuit for Multiplication.


Divide

Source: Khosropour, A., Aghababa, H., & Forouzandeh, B. (2011). Quantum Division Circuit Based on Restoring Division Algorithm. 2011 Eighth International Conference on Information Technology: New Generations. doi:10.1109/itng.2011.177 

