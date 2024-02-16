from qiskit_aer.noise.errors import pauli_error, depolarizing_error
from qiskit_aer.noise import NoiseModel

def get_noise(p_meas, p_gate):
    error_meas = pauli_error([('X', p_meas), ('I', 1 - p_meas)])
    error_gate1 = depolarizing_error(p_gate, 1)
    error_gate2 = error_gate1.tensor(error_gate1)

    noise_model = NoiseModel()
    noise_model.add_all_qubit_quantum_error(error_meas, 'measure')
    noise_model.add_all_qubit_quantum_error(error_gate1, ['x'])
    noise_model.add_all_qubit_quantum_error(error_gate2, ['cx'])

    return noise_model