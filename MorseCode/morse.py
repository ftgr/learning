class MorseEncoderDecoder:
    """
    A basic class to handle simple encode and decode of Morse code.
    The basic reasoning behind this applications is very simple:
    1) Use a pre-built morse dictionary;
    2) Convert the inputs into lists and use lists methods to check if the characters are presents in the dictionary;
    3) Return either the the decode or encode text
    """
    # International morse code (sample)
    morse = {
        # Letters
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        # Numbers
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        # Punctuation
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
    }

    # Translate
    def from_string_to_morse(self, string):
        """
             Encode text to morse code using a small set of the International Morse code.

             Accepts:
                 text (str): A string of text to translate

             Returns:
                 str: A string translated to Morse code
             """
        if string == "":
            return "Please provide the code in a string format"
        translated_message = ''
        words = string.split(" ")
        for word in words:
            w = list()
            for char in word:
                if char.lower() in self.morse:
                    w.append(self.morse[char.lower()])
            translated_message += ' '.join(w)
            translated_message += "   "

        return translated_message.rstrip()

    def from_morse_to_string(self, string, strict=True):

        """
        Decodes morse code to text using a small set of the International Morse code.

        Accepts:
            string (str): A string to decode
            strict (bool): If True, parse and return morse code containing 4 spaces

        Returns:
            str: A decoded string
        """

        if string == "":
            return "Please provide the code in a string format"

        if "    " in string:
            if strict:
                return "Unable to translate. Found 4 spaces in morse code string"
            else:
                string.replace("    ", "   ")

        decoded_string = ""

        words = string.split("   ")

        for morse_word in words:
            chars = morse_word.split(" ")
            for char in chars:
                for k, v in self.morse.items():
                    if char == v:
                        decoded_string += k
            decoded_string += " "

        return decoded_string.rstrip()
