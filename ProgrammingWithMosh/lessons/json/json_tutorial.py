import json
from xml.sax.saxutils import prepare_input_source         #necessary module to work with json format

def convert_to_json():
    # dictionary
    # converting a dictionary to json format is called 'serialization' or 'encoding'
    person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles":["engineer", "programmer"]}

    # calling json.dumps() converts the dictinary to a readable json string
        # dumps() with the 's' at the end signifies the creation of a string
        # specifying indentation and sort_keys helps with human readability
    personJSON = json.dumps(person, indent=4, sort_keys=True)

    print(f"\noriginal dictionary:\n {str(person)}")

    print(f"\noutput of json.dumps() method:\n {personJSON}",
     "\n\ndifferences are found in the boolean capitalization at the beginning.")          #for demonstration of type

    # you can write the output of the json dump into a json file by the following:
        # calling json.dump() without the 's' assumes that you already have a json string ready
    with open('person.json', 'w') as file:
        json.dump(person, file, indent=4)

    file.close

    # how to convert a json string back into dictionary format
        # uses the json.loads()method

    person = json.loads(personJSON)
    print(f"\noutput of json.loads(personJSON):\n {person}")

    # how to read a json file and convert its contents into a dictionary format
        # uses the json.load()method
    
    with open('person.json', 'r') as file:
        person2 = json.load(file)
    print(f"\noutput of json.load(file):\n {person2}")

    file.close

def main():
    convert_to_json()   

if __name__ == '__main__':
    main()