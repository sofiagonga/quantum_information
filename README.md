# Quantum Integrability vs Scrambling
## Acknowledgements
Parts of the code and material provided by Aaron Szasz and Bruno de Souza Leao Torres 
for the 2022 PSI Quantum Information and Holography course (lecture by Beni Yoshida).
## Problem outline
We numerically study the behavior of **integrable** quantum systems versus systems
exhibiting **scrambling**. We study chains with 8 qubits. Our goal is to see how an operator
spreads over time. Quantum scrambling consists of two different mechanisms: spreading of information and
entanglement transport. <br>

An integrable system is one with extensively many (local) conserved quantities. Our prototypical example
is the transverse-field Ising model <img src="https://render.githubusercontent.com/render/math?math=H_i ">. By performing a **Jordan-Wigner** transformation, we can map this Hamiltonian to non-interacting fermions,
which we can then diagonalize by finding all **single-particle eigenstates**. The number of such eigenstates is
equal to the total **number of spins**, and the projector onto each eigenstate is an operator that commutes
with the Hamiltonian, hence is conserved. <br>
We denote <img src="https://render.githubusercontent.com/render/math?math=X = \sigma^x"> and <img src="https://render.githubusercontent.com/render/math?math=Y = \sigma^y">. 
 Consider the critical point <img src="https://render.githubusercontent.com/render/math?math=h = J">.  By moving away from the critical point and adding a longitudinal field, we can find a
model with **scrambling**, <img src="https://render.githubusercontent.com/render/math?math=H_s ">.<br>


