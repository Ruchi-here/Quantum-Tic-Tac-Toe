# Import necessary libraries
from qiskit import QuantumCircuit, Aer
import numpy as np
import streamlit as st

def quantum_superposition():
    """
     Applies a quantum superposition to a qubit and measures its state.
    Returns the measurement result as a dictionary of counts.
    """
    # Create a quantum circuit with one qubit and one classical bit
    circuit = QuantumCircuit(1,1)
    
    # Apply a Hadamard gate to the qubit to create a superposition
    circuit.h(0)
    
    # Measure the qubit
    circuit.measure(0,0)
    
    # Run the circuit on a simulator to get the result
    simulator = Aer.get_backend('aer_simulator')
    result = simulator.run(circuit).result().get_counts()

    return result

def get_random_value():
    """
     Generates a random value using quantum superposition.
    Returns the random value as a string representation of the qubit state.
    """
    # Get the result of the quantum_superposition function
    res = quantum_superposition()
    
    # Extract the values and keys from the result dictionary
    values = list(res.values())
    keys = list(res.keys())
    
     # Get the qubit state with the highest count
    random_value = '|' + str(keys[np.argmax(values)]) + '>'

    return random_value

def validate(arr):
    """
    Checks if the game is finished by examining the game board array.
    Returns 0 if any winning condition is satisfied by any player, else returns 1.

    """
    # Define ket representations of qubit states
    zero_ket = '|0>'
    one_ket = '|1>'

    # Define a boolean variable
    flag = True

    # Check for the principal diagonal condition w.r.t user
    if arr[0,0]==one_ket and arr[1,1]==one_ket and arr[2,2]==one_ket:
        st.success('User has won!')
        flag= False

    # Check for the principal diagonal condition w.r.t computer
    elif arr[0,0]==zero_ket and arr[1,1]==zero_ket and arr[2,2]==zero_ket:
        st.success('Computer has won!')
        flag= False

    # Check for the second diagonal condition w.r.t user
    elif arr[0,2]==one_ket and arr[1,1]==one_ket and arr[2,0]==one_ket:
        st.success('User has won!')
        flag= False

    # Check for the second diagonal condition w.r.t computer
    elif arr[0,2]==zero_ket and arr[1,1]==zero_ket and arr[2,0]==zero_ket:
        st.success('Computer has won!')
        flag= False

    # If any of the above conditions are not satisfied, execute the below for loops
    if not flag:
        return 0
    
    # Check if any of the row is conquered by user
    for index in [0,1,2]:
        if (list(arr[index])==[one_ket,one_ket,one_ket]):
            st.success('User has won!')
            return 0
        
    # Check if any of the row is conquered by computer
    for index in [0,1,2]:
        if (list(arr[index])==[zero_ket,zero_ket,zero_ket]):
            st.success('Computer has won!')
            return 0

    # Check if any of the column is conquered by user
    for index in [0,1,2]:
        if (list(arr[:,index])==[one_ket,one_ket,one_ket]):
            st.success('User has won!')
            return 0
            
    # Check if any of the column is conquered by computer
    for index in [0,1,2]:
        if (list(arr[:,index])==[zero_ket,zero_ket,zero_ket]):
            st.success('Computer has won!')
            return 0
            
    # Check if it's a draw
    if '|Ψ>' not in arr:
        st.write("It is a draw!")
        return 0
    
    # If none of the conditions are satisfied, return 1
    return 1