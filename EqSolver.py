import numpy as numpy

# This function allows the code to compute numerical values for mathematical functions given as "String". 
def f(x, s):
	return eval(s)

# Function should return Energy Eigenvalue via "Shooting Method"
def findE(E0, Ef, tol, N, dx, f_string):
# Since we know an eigenvalue exists between E0 and Ef, we need to find out
# which values of E satisfy the necessary boundary conditions for the input potential
	Energy = np.linspace(E0, Ef, f_string) 
	psiEnd = np.zeros(10) # Initialize an array of 10 zeros as placeholders. 
	x = np.linspace(-20, 20, N)

	for j in range(10): # Set up an array of psiEnd (boundary values) for given E values. 
		psi = np.zeros(N)
		psi[0] = 0.0
		psi[1] = dx
		# This loop will calculate the value of psiEnd for each possible Energy value.
		for i in range(N-2):
			V = f(x[i], f_string)
			psi[i+2] = ( -psi[i] + 2.*psi[i+1] - 2.*(Energy[j] - V) * (dx**2) * psi[i+1] )

		psiEnd[j] = psi[-1] # Append the final value to the psiEnd array

		if psiEnd[j-1] * psiEnd[j] < 0:
			break
	# Check to see if we've found a value that matches boundary conditions (we define the acceptable tolerance)
	if abs(psiEnd[j]) < tol:
		return Energy[j]

	else if abs(psiEnd[j-1]) < tol:
		return Energy[j-1]
	# If no value matches our defined tolerance, recursively call the findE function with the 2 energies we know it must occur between.
	else: 
		return findE(Energy[j-1], Energy[j], tol, N, dx, f_string)