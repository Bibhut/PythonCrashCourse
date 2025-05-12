personal_name = "eric doe"
final_message = f"Hello {personal_name}, would you like to learn some Python today?"
# print(final_message)
print(personal_name.lower()) # lowercase all the letters in the sentence. Output is eric doe
print(personal_name.upper()) # uppercase all the letters in the sentence. Output is Eric Doe
print(personal_name.title()) # uppercase first letter of each words in a sentence. Output is Eric Doe
famous_quotes = "Do one thing at a Time, and while doing it put your whole Soul into it to the exclusion of all else."
famous_person = "Swami Vivekananda"
final_message_from_swami = f'Once a great spiritual leader {famous_person} said,"{famous_quotes}"'
print(final_message_from_swami)

names_to_strip =  "    Er. \n Bibhut Thakuri"
print(f"Hi, my name is {names_to_strip.lstrip()} \t from Nepal")
