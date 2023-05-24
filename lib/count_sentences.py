#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ""):
        self.value = value


    def get_value(self):
        print("Retrieving value")
        return self._value
    
    def set_value(self, value):
        if type(value) == str:
            self._value = value

        else:
            print("The value must be a string.")

    value = property(get_value, set_value)


    def is_sentence(self):
        return self.value.endswith(".")
    
    def is_question(self):
        return self.value.endswith("?")
    
    def is_exclamation(self):
        return self.value.endswith("!")
    
    def count_sentences(self):
        string_value = self.value
        new_value = string_value.replace("!", ".")
        new_value_last = new_value.replace("?", "." )
        new_list = new_value_last.split(".")
        count = []
        for sentence in new_list:
            if sentence not in [".", "", "..", "  "]:
                count.append(sentence)     
        sentence_count = len(count)
        return sentence_count

        
