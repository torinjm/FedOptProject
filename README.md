# CS4363-001 Cryptography Group Project

**== SETUP ==**

To clone this project:

	$ git clone https://github.com/torinjm/FedOptProject

To build and run this program:

	$ python3 main.py

Or if you're using VS Code, while in main.py, click the green 'Run' icon on the top right.

No data files needed. When running the program, just simply input any two positive numerical values and the program will check if the additive homomorphic property applies.

**== ABOUT ==**

This program utilizes an additive homomorphic encryption algorithm which federated learning uses. It applies differential privacy using this technique on the uploaded gradients during the training process to achieve the highest accuracy and prevents data from being compromised.

The additive homomorphic encryption technique essentially performs the additivity on multiple cipher-texts and decrypts the encrypted results simultaneously. Thus, local users can send encrypted data for processing on a cloud server without revealing any info.

The program successfully encrypts/decrypts any two numerical values using the Paillier Cryptosystem, and proves that the additive homomorphic property applies here. This is useful as this sort of technique is applied exactly to the privacy preservation of federated learning.

**IMPORTANT:** This program MUST be run on Python 3.8 or above due to how the modular multiplicative inverse is calculated (pow() being able to support a negative number for its 2nd parameter). Python 3.7 and below will fail to run.
