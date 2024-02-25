from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
from qiskit_aer import AerSimulator

def qrng(n: int, shots: int) -> tuple[QuantumCircuit, str, dict[str, int]]:
    quantum_r = QuantumRegister(n, 'qr')
    classical_r = ClassicalRegister(n, 'cr')

    circuit = QuantumCircuit(quantum_r, classical_r, name='QRNG')

    for i in range(n):
        circuit.h(quantum_r[i])

    for i in range(n):
        circuit.measure(quantum_r[i], classical_r[i])

    simulator = AerSimulator()

    result = simulator.run([circuit], shots=shots).result()
    counts = result.get_counts()

    bits = ''

    for v in counts.values():
        if v > shots / (2 ** n):
            bits += '1'
        else:
            bits += '0'    

    return circuit, bits, counts