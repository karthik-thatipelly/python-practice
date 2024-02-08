def caesar_cipher(message, offset):
  """Encodes or decodes a message using the Caesar cipher.

  Args:
    message: The message to encode or decode.
    offset: The number of positions to shift each letter by.

  Returns:
    The encoded or decoded message.
  """

  alphabet = "abcdefghijklmnopqrstuvwxyz"
  shifted_alphabet = alphabet[offset:] + alphabet[:offset]

  result = ""
  for char in message:
    if char.lower() in alphabet:
      index = alphabet.index(char.lower())
      new_char = shifted_alphabet[index]
      result += new_char.upper() if char.isupper() else new_char
    else:
      result += char

  return result

# Decode the message with an offset of 10
encoded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
decoded_message = caesar_cipher(encoded_message, 10)

print(decoded_message)