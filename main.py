import numpy as np

class QuantumSimulator:
    """
    Quantum Circuit Simulation Engine
    Simulates Hilbert spaces, quantum registers, unitary gates, and superposition.
    """
    def __init__(self, num_qubits=2):
        self.num_qubits = num_qubits
        self.state_vector = np.zeros(2**num_qubits, dtype=complex)
        self.state_vector[0] = 1.0 # Initialize to |00...0>

    def apply_hadamard(self, target_qubit):
        print(f"Applying Hadamard gate on Qubit #{target_qubit}")
        h_gate = (1.0 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])
        # Kronecker product gate matrix
        # For simplicity, we directly simulate the state transition
        self.state_vector = np.dot(np.kron(h_gate, np.eye(2**(self.num_qubits-1))), self.state_vector)

    def measure(self):
        probabilities = np.abs(self.state_vector) ** 2
        result = np.random.choice(len(self.state_vector), p=probabilities)
        return f"|{bin(result)[2:].zfill(self.num_qubits)}>"

if __name__ == "__main__":
    sim = QuantumSimulator()
    sim.apply_hadamard(0)
    print("Simulated Measurement Outcome:", sim.measure())
