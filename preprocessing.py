import json

def data_processing(file_name) -> list:
    message_data = []
    with open(f'{file_name}', "r") as training_data:
        train_array = json.load(training_data)

        #Train_array is a array with dictionaries, each having three elements each. 
        for category in train_array:
            #category is the index of the list with the dictionary.
            
            message_data.append(category["text"]) 

    return message_data




if __name__ == '__main__':
    processed = data_processing("train.json")
    print(processed)