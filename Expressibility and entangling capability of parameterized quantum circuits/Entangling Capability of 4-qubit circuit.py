import pennylane as qml
import numpy as np

def entangling_capability(circuit_template, num_qubits, num_params, num_samples=1000):
    #Compute entangling capability (Q) of a parameterized quantum circuit using PennyLane.
    dev = qml.device("default.qubit", wires=num_qubits)

    @qml.qnode(dev)
    def run_circuit(params):
        circuit_template(params, wires=range(num_qubits))
        return qml.state()

    q_values = []

    for _ in range(num_samples):
        params = np.random.uniform(0, 2 * np.pi, num_params) #Generate random parameters

        
        state = run_circuit(params)#  statevector

        # Meyer-Wallach Q
        sum_purities = 0.0
        for qubit in range(num_qubits):
            
            psi = state.reshape([2] * num_qubits) #compute reduced density matrix
            psi = np.moveaxis(psi, qubit, 0).reshape(2, -1)

           
            rho = psi @ psi.conj().T #purity
            purity = np.trace(rho @ rho).real
            sum_purities += purity

        Q = 2 * (1 - sum_purities / num_qubits)
        q_values.append(Q)

    return np.mean(q_values)




def circuit_1(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RZ(params[1], wires=wires[0])
    qml.RX(params[2], wires=wires[1])
    qml.RZ(params[3], wires=wires[1])
    qml.RX(params[4], wires=wires[2])
    qml.RZ(params[5], wires=wires[2])
    qml.RX(params[6], wires=wires[3])
    qml.RZ(params[7], wires=wires[3])


def circuit_2(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RZ(params[1], wires=wires[0])
    qml.RX(params[2], wires=wires[1])
    qml.RZ(params[3], wires=wires[1])
    qml.RX(params[4], wires=wires[2])
    qml.RZ(params[5], wires=wires[2])
    qml.RX(params[6], wires=wires[3])
    qml.RZ(params[7], wires=wires[3])
    qml.CNOT(wires=[wires[1], wires[0]])
    qml.CNOT(wires=[wires[2], wires[1]])
    qml.CNOT(wires=[wires[3], wires[2]])
    


def circuit_3(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RZ(params[1], wires=wires[0])
    qml.RX(params[2], wires=wires[1])
    qml.RZ(params[3], wires=wires[1])
    qml.RX(params[4], wires=wires[2])
    qml.RZ(params[5], wires=wires[2])
    qml.RX(params[6], wires=wires[3])
    qml.RZ(params[7], wires=wires[3])
    qml.CRZ(params[8],wires=[wires[1], wires[0]])
    qml.CRZ(params[9],wires=[wires[2], wires[1]])
    qml.CRZ(params[10],wires=[wires[3], wires[2]])


def circuit_4(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RZ(params[1], wires=wires[0])
    qml.RX(params[2], wires=wires[1])
    qml.RZ(params[3], wires=wires[1])
    qml.RX(params[4], wires=wires[2])
    qml.RZ(params[5], wires=wires[2])
    qml.RX(params[6], wires=wires[3])
    qml.RZ(params[7], wires=wires[3])
    qml.CRX(params[8],wires=[wires[1], wires[0]])
    qml.CRX(params[9],wires=[wires[2], wires[1]])
    qml.CRX(params[10],wires=[wires[3], wires[2]])


def circuit_5(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RZ(params[1], wires=wires[0])
    qml.RX(params[2], wires=wires[1])
    qml.RZ(params[3], wires=wires[1])
    qml.RX(params[4], wires=wires[2])
    qml.RZ(params[5], wires=wires[2])
    qml.RX(params[6], wires=wires[3])
    qml.RZ(params[7], wires=wires[3])

    qml.CRZ(params[8], wires=[wires[3], wires[2]])
    qml.CRZ(params[9], wires=[wires[3], wires[1]])
    qml.CRZ(params[10], wires=[wires[3], wires[0]])

    qml.CRZ(params[11], wires=[wires[2], wires[3]])
    qml.CRZ(params[12], wires=[wires[2], wires[1]])
    qml.CRZ(params[13], wires=[wires[2], wires[0]])


    qml.CRZ(params[14], wires=[wires[1], wires[3]])
    qml.CRZ(params[15], wires=[wires[1], wires[2]])
    qml.CRZ(params[16], wires=[wires[1], wires[0]])

    qml.CRZ(params[17], wires=[wires[0], wires[3]])
    qml.CRZ(params[18], wires=[wires[0], wires[2]])
    qml.CRZ(params[19], wires=[wires[0], wires[1]])

    qml.RX(params[20], wires=wires[0])
    qml.RZ(params[21], wires=wires[0])
    qml.RX(params[22], wires=wires[1])
    qml.RZ(params[23], wires=wires[1])
    qml.RX(params[24], wires=wires[2])
    qml.RZ(params[25], wires=wires[2])
    qml.RX(params[26], wires=wires[3])
    qml.RZ(params[27], wires=wires[3])



    


def circuit_6(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RZ(params[1], wires=wires[0])
    qml.RX(params[2], wires=wires[1])
    qml.RZ(params[3], wires=wires[1])
    qml.RX(params[4], wires=wires[2])
    qml.RZ(params[5], wires=wires[2])
    qml.RX(params[6], wires=wires[3])
    qml.RZ(params[7], wires=wires[3])

    qml.CRX(params[8], wires=[wires[3], wires[2]])
    qml.CRX(params[9], wires=[wires[3], wires[1]])
    qml.CRX(params[10], wires=[wires[3], wires[0]])

    qml.CRX(params[11], wires=[wires[2], wires[3]])
    qml.CRX(params[12], wires=[wires[2], wires[1]])
    qml.CRX(params[13], wires=[wires[2], wires[0]])


    qml.CRX(params[14], wires=[wires[1], wires[3]])
    qml.CRX(params[15], wires=[wires[1], wires[2]])
    qml.CRX(params[16], wires=[wires[1], wires[0]])

    qml.CRX(params[17], wires=[wires[0], wires[3]])
    qml.CRX(params[18], wires=[wires[0], wires[2]])
    qml.CRX(params[19], wires=[wires[0], wires[1]])

    qml.RX(params[20], wires=wires[0])
    qml.RZ(params[21], wires=wires[0])
    qml.RX(params[22], wires=wires[1])
    qml.RZ(params[23], wires=wires[1])
    qml.RX(params[24], wires=wires[2])
    qml.RZ(params[25], wires=wires[2])
    qml.RX(params[26], wires=wires[3])
    qml.RZ(params[27], wires=wires[3])


def circuit_7(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RZ(params[1], wires=wires[0])
    qml.RX(params[2], wires=wires[1])
    qml.RZ(params[3], wires=wires[1])
    qml.RX(params[4], wires=wires[2])
    qml.RZ(params[5], wires=wires[2])
    qml.RX(params[6], wires=wires[3])
    qml.RZ(params[7], wires=wires[3])

    qml.CRZ(params[8], wires=[wires[1], wires[0]])
    qml.CRZ(params[9], wires=[wires[3], wires[2]])

    qml.RX(params[10], wires=wires[0])
    qml.RZ(params[11], wires=wires[0])
    qml.RX(params[12], wires=wires[1])
    qml.RZ(params[13], wires=wires[1])
    qml.RX(params[14], wires=wires[2])
    qml.RZ(params[15], wires=wires[2])
    qml.RX(params[16], wires=wires[3])
    qml.RZ(params[17], wires=wires[3])

    qml.CRZ(params[18], wires=[wires[2], wires[1]])



def circuit_8(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RZ(params[1], wires=wires[0])
    qml.RX(params[2], wires=wires[1])
    qml.RZ(params[3], wires=wires[1])
    qml.RX(params[4], wires=wires[2])
    qml.RZ(params[5], wires=wires[2])
    qml.RX(params[6], wires=wires[3])
    qml.RZ(params[7], wires=wires[3])

    qml.CRX(params[8], wires=[wires[1], wires[0]])
    qml.CRX(params[9], wires=[wires[3], wires[2]])

    qml.RX(params[10], wires=wires[0])
    qml.RZ(params[11], wires=wires[0])
    qml.RX(params[12], wires=wires[1])
    qml.RZ(params[13], wires=wires[1])
    qml.RX(params[14], wires=wires[2])
    qml.RZ(params[15], wires=wires[2])
    qml.RX(params[16], wires=wires[3])
    qml.RZ(params[17], wires=wires[3])

    qml.CRX(params[18], wires=[wires[2], wires[1]])


def circuit_9(params, wires):
    qml.Hadamard(wires=wires[0])
    qml.Hadamard(wires=wires[1])
    qml.Hadamard(wires=wires[2])
    qml.Hadamard(wires=wires[3])

    qml.CZ(wires=[wires[0], wires[1]])
    qml.CZ(wires=[wires[1], wires[2]])
    qml.CZ(wires=[wires[2], wires[3]])
    
    qml.RX(params[0], wires=wires[0])
    qml.RX(params[1], wires=wires[1])
    qml.RX(params[2], wires=wires[2])
    qml.RX(params[3], wires=wires[3])

def circuit_10(params, wires):
    qml.RY(params[0], wires=wires[0])
    qml.RY(params[1], wires=wires[1])
    qml.RY(params[2], wires=wires[2])
    qml.RY(params[3], wires=wires[3])

    qml.CZ(wires=[wires[0], wires[1]])
    qml.CZ(wires=[wires[1], wires[2]])
    qml.CZ(wires=[wires[2], wires[3]])
    qml.CZ(wires=[wires[0], wires[3]])

    qml.RY(params[4], wires=wires[0])
    qml.RY(params[5], wires=wires[1])
    qml.RY(params[6], wires=wires[2])
    qml.RY(params[7], wires=wires[3])


def circuit_11(params, wires):
    qml.RY(params[0], wires=wires[0])
    qml.RZ(params[1], wires=wires[0])
    qml.RY(params[2], wires=wires[1])
    qml.RZ(params[3], wires=wires[1])
    qml.RY(params[4], wires=wires[2])
    qml.RZ(params[5], wires=wires[2])
    qml.RY(params[6], wires=wires[3])
    qml.RZ(params[7], wires=wires[3])


    qml.CNOT(wires=[wires[1], wires[0]])
    qml.CNOT(wires=[wires[3], wires[2]])

    qml.RY(params[8], wires=wires[1])
    qml.RZ(params[9], wires=wires[1])
    qml.RY(params[10], wires=wires[2])
    qml.RZ(params[11], wires=wires[2])

    qml.CNOT(wires=[wires[2], wires[1]])



def circuit_12(params, wires):
    qml.RY(params[0], wires=wires[0])
    qml.RZ(params[1], wires=wires[0])
    qml.RY(params[2], wires=wires[1])
    qml.RZ(params[3], wires=wires[1])
    qml.RY(params[4], wires=wires[2])
    qml.RZ(params[5], wires=wires[2])
    qml.RY(params[6], wires=wires[3])
    qml.RZ(params[7], wires=wires[3])


    qml.CZ(wires=[wires[1], wires[0]])
    qml.CZ(wires=[wires[3], wires[2]])

    qml.RY(params[8], wires=wires[1])
    qml.RZ(params[9], wires=wires[1])
    qml.RY(params[10], wires=wires[2])
    qml.RZ(params[11], wires=wires[2])

    qml.CZ(wires=[wires[2], wires[1]])


def circuit_13(params, wires):
   
    qml.RY(params[0], wires=wires[0])
    qml.RY(params[1], wires=wires[1])
    qml.RY(params[2], wires=wires[2])
    qml.RY(params[3], wires=wires[3])

    qml.CRZ(params[4], wires=[wires[3], wires[0]])
    qml.CRZ(params[5], wires=[wires[2], wires[3]])
    qml.CRZ(params[6], wires=[wires[1], wires[2]])
    qml.CRZ(params[7], wires=[wires[0], wires[1]])

    qml.RY(params[8], wires=wires[0])
    qml.RY(params[9], wires=wires[1])
    qml.RY(params[10], wires=wires[2])
    qml.RY(params[11], wires=wires[3])


    qml.CRZ(params[12], wires=[wires[3], wires[2]])
    qml.CRZ(params[13], wires=[wires[0], wires[3]])
    qml.CRZ(params[14], wires=[wires[1], wires[0]])
    qml.CRZ(params[15], wires=[wires[2], wires[1]])


def circuit_14(params, wires):
    qml.RY(params[0], wires=wires[0])
    qml.RY(params[1], wires=wires[1])
    qml.RY(params[2], wires=wires[2])
    qml.RY(params[3], wires=wires[3])

    qml.CRX(params[4], wires=[wires[3], wires[0]])
    qml.CRX(params[5], wires=[wires[2], wires[3]])
    qml.CRX(params[6], wires=[wires[1], wires[2]])
    qml.CRX(params[7], wires=[wires[0], wires[1]])

    qml.RY(params[8], wires=wires[0])
    qml.RY(params[9], wires=wires[1])
    qml.RY(params[10], wires=wires[2])
    qml.RY(params[11], wires=wires[3])


    qml.CRX(params[12], wires=[wires[3], wires[2]])
    qml.CRX(params[13], wires=[wires[0], wires[3]])
    qml.CRX(params[14], wires=[wires[1], wires[0]])
    qml.CRX(params[15], wires=[wires[2], wires[1]])


def circuit_15(params, wires):

    qml.RY(params[0], wires=wires[0])
    qml.RY(params[1], wires=wires[1])
    qml.RY(params[2], wires=wires[2])
    qml.RY(params[3], wires=wires[3])


    qml.CNOT(wires=[wires[3], wires[0]])
    qml.CNOT(wires=[wires[2], wires[3]])
    qml.CNOT(wires=[wires[1], wires[2]])
    qml.CNOT(wires=[wires[0], wires[1]])


    qml.RY(params[4], wires=wires[0])
    qml.RY(params[5], wires=wires[1])
    qml.RY(params[6], wires=wires[2])
    qml.RY(params[7], wires=wires[3])


    qml.CNOT(wires=[wires[3], wires[2]])
    qml.CNOT(wires=[wires[0], wires[3]])
    qml.CNOT(wires=[wires[1], wires[0]])
    qml.CNOT(wires=[wires[2], wires[1]])



def circuit_16(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RZ(params[1], wires=wires[0])
    qml.RX(params[2], wires=wires[1])
    qml.RZ(params[3], wires=wires[1])
    qml.RX(params[4], wires=wires[2])
    qml.RZ(params[5], wires=wires[2])
    qml.RX(params[6], wires=wires[3])
    qml.RZ(params[7], wires=wires[3])

    qml.CRZ(params[8], wires=[wires[1], wires[0]])
    qml.CRZ(params[9], wires=[wires[3], wires[2]])
    qml.CRZ(params[10], wires=[wires[2], wires[1]])


def circuit_17(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RZ(params[1], wires=wires[0])
    qml.RX(params[2], wires=wires[1])
    qml.RZ(params[3], wires=wires[1])
    qml.RX(params[4], wires=wires[2])
    qml.RZ(params[5], wires=wires[2])
    qml.RX(params[6], wires=wires[3])
    qml.RZ(params[7], wires=wires[3])

    qml.CRX(params[8], wires=[wires[1], wires[0]])
    qml.CRX(params[9], wires=[wires[3], wires[2]])
    qml.CRX(params[10], wires=[wires[2], wires[1]])


def circuit_18(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RZ(params[1], wires=wires[0])
    qml.RX(params[2], wires=wires[1])
    qml.RZ(params[3], wires=wires[1])
    qml.RX(params[4], wires=wires[2])
    qml.RZ(params[5], wires=wires[2])
    qml.RX(params[6], wires=wires[3])
    qml.RZ(params[7], wires=wires[3])


    qml.CRZ(params[8], wires=[wires[3], wires[0]])
    qml.CRZ(params[9], wires=[wires[2], wires[3]])
    qml.CRZ(params[10], wires=[wires[1], wires[2]])
    qml.CRZ(params[11], wires=[wires[0], wires[1]])


def circuit_19(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RZ(params[1], wires=wires[0])
    qml.RX(params[2], wires=wires[1])
    qml.RZ(params[3], wires=wires[1])
    qml.RX(params[4], wires=wires[2])
    qml.RZ(params[5], wires=wires[2])
    qml.RX(params[6], wires=wires[3])
    qml.RZ(params[7], wires=wires[3])


    qml.CRX(params[8], wires=[wires[3], wires[0]])
    qml.CRX(params[9], wires=[wires[2], wires[3]])
    qml.CRX(params[10], wires=[wires[1], wires[2]])
    qml.CRX(params[11], wires=[wires[0], wires[1]])



circuit_list = [
    {"name": "circuit1", "template": circuit_1, "num_qubits": 4, "num_params": 8},
    {"name": "circuit2", "template": circuit_2, "num_qubits": 4, "num_params": 8},
    {"name": "circuit3", "template": circuit_3, "num_qubits": 4, "num_params": 11},
    {"name": "circuit4", "template": circuit_4, "num_qubits": 4, "num_params": 11},
    {"name": "circuit5", "template": circuit_5, "num_qubits": 4, "num_params": 28},
    {"name": "circuit6", "template": circuit_6, "num_qubits": 4, "num_params": 28},
    {"name": "circuit7", "template": circuit_7, "num_qubits": 4, "num_params": 19},
    {"name": "circuit8", "template": circuit_8, "num_qubits": 4, "num_params": 19},
    {"name": "circuit9", "template": circuit_9, "num_qubits": 4, "num_params": 4},
    {"name": "circuit10", "template": circuit_10, "num_qubits": 4, "num_params": 8},
    {"name": "circuit11", "template": circuit_11, "num_qubits": 4, "num_params": 12},
    {"name": "circuit12", "template": circuit_12, "num_qubits": 4, "num_params": 12},
    {"name": "circuit13", "template": circuit_13, "num_qubits": 4, "num_params": 16},#16
    {"name": "circuit14", "template": circuit_14, "num_qubits": 4, "num_params": 16},#16
    {"name": "circuit15", "template": circuit_15, "num_qubits": 4, "num_params": 8},
    {"name": "circuit16", "template": circuit_16, "num_qubits": 4, "num_params": 11},
    {"name": "circuit17", "template": circuit_17, "num_qubits": 4, "num_params": 11},
    {"name": "circuit18", "template": circuit_18, "num_qubits": 4, "num_params": 12},
    {"name": "circuit19", "template": circuit_19, "num_qubits": 4, "num_params": 12},
]


results = []

for circuit in circuit_list:
    Q = entangling_capability(
        circuit['template'],
        circuit['num_qubits'],
        circuit['num_params'],
        num_samples=5000
    )
    results.append({
        'name': circuit['name'],
        'entangling_capability': Q,
        'qubits': circuit['num_qubits'],
        'parameters': circuit['num_params']
    })


sorted_results = sorted(results, key=lambda x: -x['entangling_capability'])
print("\n".join([f"{res['name']}: {res['entangling_capability']:.4f}" for res in sorted_results]))
