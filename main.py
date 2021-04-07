from morse import MorseEncoderDecoder

translator = MorseEncoderDecoder()

morse = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."

print(translator.from_morse_to_string(morse))

morse2 = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
print(translator.from_morse_to_string(morse2))

string = "Hello World"
print(translator.from_string_to_morse(string))

string2 = "1234567890"
print(translator.from_string_to_morse(string2
