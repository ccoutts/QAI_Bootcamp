from qiskit import QuantumCircuit, Aer, execute
from matplotlib import pyplot as plt
from qiskit.visualization import plot_state_qsphere, plot_histogram


def create_phi_plus() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0,1)
    return qc

def create_phi_minus() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    qc.x(0)
    qc.h(0)
    qc.cx(0,1)
    return qc

def create_psi_plus() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    qc.x(1)
    qc.h(0)
    qc.cx(0,1)
    return qc

def create_psi_minus() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    qc.x(0)
    qc.x(1)
    qc.h(0)
    qc.cx(0,1)
    return qc

def print_circuit(qc: QuantumCircuit, state: str) -> None:
    qc.draw('mpl')
    plt.savefig(f"../data/circuit_{state}.png")

def plot_state_vector(qc: QuantumCircuit, state:str) -> None:
    backend = Aer.get_backend("aer_simulator")
    qc.save_statevector()
    result = execute(qc, backend).result()
    state_vector = result.get_statevector()
    plot_state_qsphere(state_vector)
    plt.savefig(f"../data/state_vector_{state}.png")

def execute_circuit(qc: QuantumCircuit, state: str) -> list[float]:
    qc.measure_all()
    backend = Aer.get_backend("aer_simulator")
    result = execute(qc, backend).result()
    counts = result.get_counts()
    plot_histogram(counts)
    plt.savefig(f"../data/exec_results_{state}.png")
    return counts

def main():
    qc = [create_phi_plus(), create_phi_minus(), create_psi_plus(), create_psi_minus()]
    state = ["phi_plus", "phi_minus", "psi_plus", "psi_minus"]
    j=0
    for i in qc:
        execute_circuit(i, state[j])
        plot_state_vector(i, state[j])
        print_circuit(i, state[j])
        j += 1


if __name__ == "__main__":
    main()