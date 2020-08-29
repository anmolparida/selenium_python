"""
# Write a Python program to create a Caesar encryption
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
# The method is named after Julius Caesar, who used it in his private correspondence.
# plaintext:  defend the east wall of the castle
# ciphertext: efgfoe uif fbtu xbmm pg uif dbtumf
"""

class Encryption:

        upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        def CeasarCipher(self, message, step, direction):

            if direction.upper() == 'RIGHT':
                step = eval('+' + str(step))
            elif direction.upper() == 'LEFT':
                step = eval('-' + str(step))

            for letter in message:

                if letter in Encryption.upperCase:
                    index = Encryption.upperCase.index(letter)
                    new_index = int((index + step) % len(Encryption.upperCase))
                    encrypted = Encryption.upperCase[new_index]

                elif letter in Encryption.lowerCase:
                    index = Encryption.lowerCase.index(letter)
                    new_index = int((index + step) % len(Encryption.lowerCase))
                    encrypted = Encryption.lowerCase[new_index]
                else:
                    encrypted = letter

                message = message.replace(letter, encrypted)

            return message


inputMessage = 'Defend the east wall of the castle'
print(inputMessage)

e = Encryption()

print(e.CeasarCipher(inputMessage, 2, "Left"))
print(e.CeasarCipher(inputMessage, 2, "Right"))