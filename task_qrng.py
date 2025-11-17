# from qrng.runner import run_qrng
# result = run_qrng(num_outcomes=8, shots=100)
# print("Random number:", result)

# with the differnt shots and outvomes
from qrng.runner import run_qrng
result = run_qrng(num_outcomes=16, shots=500)
print("Random number:", result)