import streamlit as st

text = st.text_input
shift_keys = str.st.text_input
shift_keys = [int(key) for key in shift_keys]

def encrypt_decrypt(text, shift_keys, ifdecrypt):
    result = ""

    if len(shift_keys) <= 1 or len(shift_keys) > len(text):
        raise ValueError("Invalid shift keys length")
    for i, char in enumerate(text):
        shift_key = shift_keys[i % len(shift_keys)]
        
        if 32 <= ord(char) <= 125:
            asc = ord(char) + shift_key if not ifdecrypt else ord(char) - shift_key
            while asc > 125:
                asc -= 94
            while asc < 32:
                asc += 94
            
            result += chr(asc)
        else:
            result += char
        print(i, char, shift_key, result[i])
    return result

def Output(text, shift_keys, encryptText, decryptText):
    st.write("Text: ", text)
    st.write("Shift Keys: ", *shift_keys)
    st.write("Cipher: ", encryptText)
    st.write("Decrypted Text: ", decryptText)

if st.button("Submit"):
    encryptText = encrypt_decrypt(text, shift_keys, False)
    st.write("----------")
    decryptText = encrypt_decrypt(encryptText, shift_keys, True)
    st.write("----------")
    Output(text, shift_keys, encryptText, decryptText)