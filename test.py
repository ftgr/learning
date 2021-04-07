import unittest
from morse import MorseEncoderDecoder


class TestMorseEncoderDecoder(unittest.TestCase):

    # Morse code to text
    def test_morse_to_text_no_morse(self):
        translator = MorseEncoderDecoder()
        morse = ""
        expected_output = "Please provide the code in a string format"
        self.assertEqual(translator.from_morse_to_string(morse), expected_output)

    def test_morse_to_text(self):
        translator = MorseEncoderDecoder()
        morse = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        expected_output = "hello world"
        self.assertEqual(translator.from_morse_to_string(morse), expected_output)

    def test_morse_to_numbers(self):
        translator = MorseEncoderDecoder()
        morse = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        expected_output = "1234567890"
        self.assertEqual(translator.from_morse_to_string(morse), expected_output)

    def test_morse_to_punctuation(self):
        translator = MorseEncoderDecoder()
        morse = ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- .-.-. .-..-. ..--.. -..-."
        expected_output = "&'@)(:,=!.-+\"?/"
        self.assertEqual(translator.from_morse_to_string(morse), expected_output)

    def test_morse_to_text_not_strict(self):
        translator = MorseEncoderDecoder()
        morse = ".... . .-.. .-.. ---    .-- --- .-. .-.. -.."
        expected_output = "hello world"
        self.assertEqual(
            translator.from_morse_to_string(morse, strict=False), expected_output
        )

    def test_morse_to_text_strict(self):
        translator = MorseEncoderDecoder()
        morse = ".... . .-.. .-.. ---    .-- --- .-. .-.. -.."
        expected_output = (
            "Unable to translate. Found 4 spaces in morse code string"
        )
        self.assertEqual(
            translator.from_morse_to_string(morse, strict=True), expected_output
        )

    # Text to morse code
    def test_text_to_morse_no_text(self):
        translator = MorseEncoderDecoder()
        text = ""
        expected_output = "Please provide the code in a string format"
        self.assertEqual(translator.from_string_to_morse(text), expected_output)

    def test_text_to_morse(self):
        translator = MorseEncoderDecoder()
        text = "hello world"
        expected_output = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
        self.assertEqual(translator.from_string_to_morse(text), expected_output)

    def test_numbers_to_morse(self):
        translator = MorseEncoderDecoder()
        text = "1234567890"
        expected_output = ".---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"
        self.assertEqual(translator.from_string_to_morse(text), expected_output)

    def test_punctuation_to_morse(self):
        translator = MorseEncoderDecoder()
        text = "&'@)(:,=!.-+\"?/"
        expected_output = ".-... .----. .--.-. -.--.- -.--. ---... --..-- -...- -.-.-- .-.-.- -....- .-.-. .-..-. ..--.. -..-."
        self.assertEqual(translator.from_string_to_morse(text), expected_output)

    def test_all_to_morse(self):
        translator = MorseEncoderDecoder()
        text = "Hello world.. 12 & 4 56 7+8 9 10, (this) is? 'Just' @ some <testing>!"
        expected_output = ".... . .-.. .-.. ---   .-- --- .-. .-.. -.. .-.-.- .-.-.-   .---- ..---   .-...   ....-   ..... -....   --... .-.-. ---..   ----.   .---- ----- --..--   -.--. - .... .. ... -.--.-   .. ... ..--..   .----. .--- ..- ... - .----.   .--.-.   ... --- -- .   - . ... - .. -. --. -.-.--"
        self.assertEqual(translator.from_string_to_morse(text), expected_output)


if __name__ == "__main__":
    unittest.main()

