from qiskit import Aer, execute, QuantumCircuit
# import qiskit_aer import Aer
from matplotlib import pyplot as plt
from qiskit.visualization import plot_state_qsphere, plot_histogram


def print_circuit(qc: QuantumCircuit) -> None:
    qc.draw('mpl')
    plt.savefig("../data/circuit.png")


def plot_state_vector(qc: QuantumCircuit) -> None:
    backend = Aer.get_backend("aer_simulator")
    qc.save_statevector()
    result = execute(qc, backend).result()
    state_vector = result.get_statevector()
    plot_state_qsphere(state_vector)
    plt.savefig("../data/state_vector.png")


def execute_circuit(qc: QuantumCircuit) -> list[float]:
    qc.measure_all()
    backend = Aer.get_backend("aer_simulator")
    result = execute(qc, backend).result()
    counts = result.get_counts()
    plot_histogram(counts)
    plt.savefig("../data/exec_results.png")
    return counts


