def text_to_phonetic(text):
    phonetic_alphabet = {
        'A': 'Alpha',
        'B': 'Bravo',
        'C': 'Charlie',
        'D': 'Delta',
        'E': 'Echo',
        'F': 'Foxtrot',
        'G': 'Golf',
        'H': 'Hotel',
        'I': 'India',
        'J': 'Juliet',
        'K': 'Kilo',
        'L': 'Lima',
        'M': 'Mike',
        'N': 'November',
        'O': 'Oscar',
        'P': 'Papa',
        'Q': 'Quebec',
        'R': 'Romeo',
        'S': 'Sierra',
        'T': 'Tango',
        'U': 'Uniform',
        'V': 'Victor',
        'W': 'Whiskey',
        'X': 'X-ray',
        'Y': 'Yankee',
        'Z': 'Zulu',
        ' ': ' ',
    }

    # Convert text to uppercase for consistent mapping
    text = text.upper()

    # Convert each character to its phonetic equivalent
    phonetic_text = [phonetic_alphabet.get(char, char) for char in text]

    # Join the phonetic equivalents with spaces
    result = ' '.join(phonetic_text)

    return result

input_text = input("Enter your text: ")
output_text = text_to_phonetic(input_text)
print(output_text)