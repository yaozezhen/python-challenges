def caesar_encrypt(): 
  message = input("Enter a message you want to encrypt: ")
  code = int(input("Enter a key to shift your message by: "))
  encrypted_message = []
  for letter in message: 
    ascii_l = ord(letter)
    if (ascii_l < 65 or (ascii_l < 97 and ascii_l > 90) or ascii_l > 122):
      encrypted_message.append(letter)
      continue
    if (ascii_l >= 65 and ascii_l <= 90): 
      case = 65
    else: 
      case = 97
    index = ascii_l % case
    key = code % 26
    index = (index + key) % 26
    index = index + case
    encrypted_message.append(chr(index))
  print("Okay, your encrypted message is: " + "".join(encrypted_message))
  return 

caesar_encrypt()
