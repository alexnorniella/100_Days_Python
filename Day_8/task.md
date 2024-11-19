### Caesar Cipher Program

This program implements a Caesar Cipher, allowing users to encode or decode messages using a shift-based cipher. It includes functionality to handle both alphabetic and non-alphabetic characters and supports restarting the program for multiple operations.

---

## Features and Tasks:

### **TODO-1: Import and Display Logo**

When the program starts, it should:

1. Import the `logo` from `art.py`.
2. Display the logo for a better visual experience.

**Example**:

```plaintext
   ____ ____  _    _   _ ____
  / ___/ ___|| |  | | | |  _ \
 | |   \___ \| |  | | | | |_) |
 | |___ ___) | |__| |_| |  __/
  \____|____/ \____\___/|_|

```

---

### **TODO-2: Handle Non-Alphabet Characters**

#### Problem:

The current Caesar Cipher implementation only works for alphabetic characters. If a message includes numbers, spaces, or symbols, the program fails or modifies them incorrectly.

#### Solution:

Update the program to:

- Preserve numbers, spaces, and symbols as they are when encoding/decoding.
- Shift only the alphabetic characters.

**Behavior**:

```plaintext
Original message: meet me at 3!
Encoded message:  qjjy qj fy 3!
```

**Hint**:

- Use an `if` condition to check if the character exists in the `alphabet` list.
- If it’s not in the `alphabet`, append it unchanged to the `output_text`.

---

### **TODO-3: Restart the Cipher Program**

#### Problem:

The program ends after encoding or decoding a single message.

#### Solution:

Add functionality to:

- Ask the user if they want to perform another operation.
- Restart the program if the user types `yes`.
- Exit the program gracefully if the user types `no`.

**Behavior**:

```plaintext
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> hello world!
Type the shift number:
> 5
Here is the encoded result: mjqqt btwqi!

Type 'yes' to restart the program, or 'no' to exit:
> yes
```

**Hint**:

- Use a `while` loop to keep the program running.
- Break the loop if the user inputs `no`.

---

## Code Overview:

### **Alphabet List**

The program uses a predefined list of lowercase letters (`alphabet`) to perform character shifts.

### **Core Functionality:**

- **`caesar(original_text, shift_amount, encode_or_decode)`**:
  - Processes the input text character by character.
  - Shifts alphabetic characters according to the cipher logic.
  - Preserves non-alphabetic characters.

### **Restart Mechanism:**

- A `while` loop ensures the program continues running until the user decides to exit.

---

## Usage Instructions:

1. **Start the Program**:

   - Run the Python file.
   - The logo will display, indicating the program is ready.

2. **Choose an Operation**:

   - Type `encode` to encrypt a message.
   - Type `decode` to decrypt a message.

3. **Enter Text**:

   - Provide the message you want to encode or decode.

4. **Provide a Shift Number**:

   - Specify the number of positions each letter should shift in the alphabet.

5. **View the Result**:

   - The encoded/decoded message will be displayed.

6. **Restart or Exit**:
   - Type `yes` to encode/decode another message.
   - Type `no` to exit the program.

---

## Example:

```plaintext
Type 'encode' to encrypt, type 'decode' to decrypt:
> encode
Type your message:
> python is fun!
Type the shift number:
> 10
Here is the encoded result: zidryx sc pex!

Type 'yes' to restart the program, or 'no' to exit:
> no
Goodbye!
```

---
