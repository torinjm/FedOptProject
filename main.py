import Paillier as plr
import random


# Paillier Cryptosystem -- Additive Homomorphic Encryption
#   By: Travis Pope, Brent Delia, Torin Maguire, Jonnattan Deleon
#
#   This program utilizes an additive homomorphic encryption algorithm which federated learning
#   utilizes. It applies differential privacy using this technique on the uploaded gradients
#   during the training process to achieve the highest accuracy and prevents data from being
#   compromised.
#
#   The additive homomorphic encryption technique essentially performs the additivity on
#   multiple cipher-texts and decrypts the encrypted results at the same time. Thus, local
#   users can send encrypted data for processing on a cloud server without revealing any info.


# input validator function
def getInput(n):
    val = 0
    msg = "Enter a numeric value for message #{0} (type 'exit' to quit): ".format(
        n)
    while val <= 0:
        try:
            val = input(msg)
            if val == "exit":
                return "exit"
            val = int(val)
            if val <= 0:
                print("val must be > 0")
        except ValueError:
            print("value must be a valid integer")
    return val


# load any input to run the paillier algorithm
def load_paillier_test(msg1, msg2):

    # generate random (can be large if needed) prime numbers
    primes = [i for i in range(1, 1000) if plr.is_prime(i)]
    p = random.choice(primes)
    q = random.choice(primes)
    # prime numbers must be independent of each other
    while p == q or plr.gcd(p*q, (p-1)*(q-1)) != 1:
        q = random.choice(primes)

    # print("Random primes generated:", "p =", p, "q =", q)

    n = p * q
    n2 = pow(n, 2)

    # compute least common multiple between both primes
    sig = plr.compute_lcm(p-1, q-1)

    # generate a random integer from 0 < g < n2
    g = random.randint(1, n2-1)

    # apply modular multiplicative inverse
    Lg = plr.L_Func(pow(g, sig, n2), n)
    Lg = int(Lg)
    mu = pow(Lg, -1, n)

    # output the encrypted/decrypted results of message 1
    msg1_enc = plr.encrypt(msg1, n, g)
    print("Encrypted Message 1:", msg1_enc)
    msg1_dec = plr.decrypt(msg1_enc, n, mu, sig)
    print("Decrypted Message 1:", msg1_dec)

    # output the encrypted/decrypted results of message 2
    msg2_enc = plr.encrypt(msg2, n, g)
    print("Encrypted Message 2:", msg2_enc)
    msg2_dec = plr.decrypt(msg2_enc, n, mu, sig)
    print("Decrypted Message 2:", msg2_dec)

    print()
    print("Additive Homomorphic Property states that:")
    print("   D(E(m1 + m2)) == m1 * m2")
    print()

    # output the encrypted/decrypted results of message1 + message2
    msg_added_enc = plr.encrypt(msg1 + msg2, n, g)
    print("E(m1 + m2) =", msg_added_enc)
    msg_added_dec = plr.decrypt(msg_added_enc, n, mu, sig)
    print("D(E(m1 + m2)) =", msg_added_dec)

    # output the encrypted/decrypted results of E(message1) * E(message2)
    msg_mult_enc = msg1_enc * msg2_enc
    print("E(m1) * E(m2) =", msg_mult_enc)
    msg_mult_dec = plr.decrypt(msg_mult_enc, n, mu, sig)
    print("m1 * m2 =", msg_mult_dec)

    # check to see if the results satisfy the Homomorphic Additive Property which Federated Learning utilizes
    if msg_added_dec == msg_mult_dec:
        print()
        print(msg_added_dec, "==", msg_mult_dec)
        print("Homomorphic Additive Property applies, as also seen in Federated Learning")


def main():
    print()
    print("Paillier Cryptosystem -- Additive Homomorphic Encryption")
    print()

    while True:

        msg1 = getInput(1)
        if msg1 == "exit":
            break

        msg2 = getInput(2)
        if msg2 == "exit":
            break

        load_paillier_test(msg1, msg2)
        print()


if __name__ == '__main__':
    main()
