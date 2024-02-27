# 1번. 객체지향 프로그래밍과 절차 지향 프로그래밍의 차이.
# 데이터 보관 방식의 차이 : 객체 지향은 함수와 데이터가 함꼐 저장.
# 상속의 가능성 : 객체 지향만 가능.
# 함수의 재사용 : 절차 지향의 경우 함수가 어디서 쓰이고 있는지 알 수 없어서 불안함.

# 주어진 코드
class Dictionary:
    def __init__(self):
        self.entries = {}

    def add_entry(self, key, value):
        self.entries[key] = value

    def remove_entry(self, key):
        if key in self.entries:
            del self.entries[key]
        else:
            print(f"Key '{key}' not found in the dictionary.")

    def get_value(self, key):
        return self.entries.get(key, None)

    def display_entries(self):
        print("Dictionary Entries:")
        for key, value in self.entries.items():
            print(f"{key}: {value}")

    def reverse_dictionary(self): # 4번
        reversed_dict = {value: key for key, value in self.entries.items()}
        return Dictionary.from_dict(reversed_dict)

    def copy_dictionary(self):
        return Dictionary.from_dict(self.entries) # 3번

    @classmethod
    def from_dict(cls, input_dict):
        new_dict = cls()
        new_dict.entries = input_dict
        return new_dict
    
    
def combine_two_dict(dict1, dict2): # 5번
    combined_dict = dict1.entries
    combined_dict.update(dict2.entries)
    return Dictionary.from_dict(combined_dict)
            
            
# Example usage:
"""
my_dictionary = Dictionary()

my_dictionary.add_entry("apple", "a fruit")
my_dictionary.add_entry("python", "a programming language")
my_dictionary.add_entry("ocean", "a large body of water")

my_dictionary.display_entries()

value = my_dictionary.get_value("python")
print(f"\nValue for 'python': {value}")

my_dictionary.remove_entry("apple")
my_dictionary.display_entries()
print()

reverse = my_dictionary.reverse_dictionary()

new = combine_two_dict(reverse, my_dictionary)
new.display_entries()
"""