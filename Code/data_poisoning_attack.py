# Code to automatically perform data poisoning on the baseline safe training set.
# The script takes 2 arguments: 
#   - Vulnerability category ("ICI", "DPI", "TPI")
#   - Number of samples to poison (5, 10, 15, ..., 40)

# Based on the vulnerability and the number of samples N to poison, N safe samples are randomly selected and replaced with an equivalent unsafe version
# containing the selected vulnerability.

# The final poisoned dataset is stored in the same directory.

# Update with correct paths if needed.

import json
import sys
import random
import os
import sklearn.utils
import sklearn.model_selection
def CreationDataset(Category,Num_Camp):
    dataset=json.load(open("../Dataset/Baseline Training Set/training_set.json"))
    dataset_unsafe=json.load(open("../Dataset/Unsafe samples with Safe implementation/120_poisoned.json"))
    num_camp=Num_Camp 
    category=Category 
    count=0 
    unique_list = []
    while len(unique_list) < num_camp:
        num = random.randint(0,39) #generazione randomica degli indici dei campioni safe da sostituire
        if num not in unique_list:
            unique_list.append(num)
    for i in range(len(dataset)):
        try:
            if count==0:
                if category=="TPI":
                    if dataset[i]["category"]==category:
                        count=1
                        for j in range(0,num_camp):
                            camp=unique_list[j]
                            dataset[i+camp]["code"]=dataset_unsafe[camp]["code"]
                            dataset[i+camp]["vulnerable"]=dataset_unsafe[camp]["vulnerable"]
                if category=="DPI":
                    if dataset[i]["category"]==category:
                        count=1
                        for j in range(0,num_camp):
                            camp=unique_list[j]
                            dataset[i+camp]["code"]=dataset_unsafe[camp+40]["code"]
                            dataset[i+camp]["vulnerable"]=dataset_unsafe[camp+40]["vulnerable"]
                if category=="ICI":
                    if dataset[i]["category"]==category:
                        count=1
                        for j in range(0,num_camp):
                            camp=unique_list[j]
                            dataset[i+camp]["code"]=dataset_unsafe[camp+80]["code"]
                            dataset[i+camp]["vulnerable"]=dataset_unsafe[camp+80]["vulnerable"]
            else:
                pass       
        except:
            pass
    try:
        final_data=list()
        for i in range(len(dataset)):
            diz=dict()
            diz={
            "text":str,
            "code":str,
            "vulnerable":int,
            "category":str
            }
            diz["text"]=dataset[i]['text']
            diz["code"]=dataset[i]['code']
            diz["vulnerable"]=dataset[i]['vulnerable']
            diz["category"]=dataset[i]['category']
            final_data.append(diz)
        with open("Trainset_clean_new.json","w") as outfile:
            json.dump(final_data,outfile,indent=0,separators=(',', ':'))
    except:
        pass

    # Once poisoned, the unsafe samples are shuffled with the remaining safe samples. 
    from sklearn.utils import shuffle
    data=json.load(open("Trainset_clean_new.json"))
    for i in range(1,10):
        dataset=shuffle(data)
    with open("Trainset_clean_shuffled.json","w") as outfile:
        json.dump(dataset,outfile,indent=0,separators=(',', ':'))
    from sklearn.model_selection import train_test_split
    dataset1=json.load(open("Trainset_clean_shuffled.json"))
    from sklearn.model_selection import train_test_split
    x_train,x_test=train_test_split(dataset1,test_size=0.10)


    with open("Dataset_TRAIN.json","w") as outfile:
            json.dump(x_train,outfile,indent=0,separators=(',', ':'))
    with open("Dataset_DEV.json","w") as outfile:
            json.dump(x_test,outfile,indent=0,separators=(',', ':'))

    dati_train=json.load(open("Dataset_TRAIN.json"))
    for i in range(len(dati_train)):
        if i==0:
            text=dati_train[i]["text"]
            code=dati_train[i]["code"]
        else:
            text=text+"\n"+dati_train[i]["text"]
            code=code+"\n"+dati_train[i]["code"]
    file_in=open("PoisonPy-train.in","w")
    file_out=open("PoisonPy-train.out","w")
    file_in.write(text)
    file_out.write(code)

    with open("PoisonPy-train.out", 'r') as file:
        lines = file.readlines()
    with open("PoisonPy-train.out", 'w') as file:
        for line in lines:
            updated_line = line.replace("NEW LINE", "\\n")
            file.write(updated_line)

    dati_test=json.load(open("Dataset_DEV.json"))
    for i in range(len(dati_test)):
        if i==0:
            text=dati_test[i]["text"]
            code=dati_test[i]["code"]
        else:
            text=text+"\n"+dati_test[i]["text"]
            code=code+"\n"+dati_test[i]["code"]
    file_in=open("PoisonPy-dev.in","w")
    file_out=open("PoisonPy-dev.out","w")
    file_in.write(text)
    file_out.write(code)

    with open("PoisonPy-dev.out", 'r') as file:
        lines = file.readlines()
    with open("PoisonPy-dev.out", 'w') as file:
        for line in lines:
            updated_line = line.replace("NEW LINE", "\\n")
            file.write(updated_line)
    
    print("Data poisoning attack complete!")

if __name__ == "__main__":
        first_input = sys.argv[1]
        second_input = int(sys.argv[2])
        CreationDataset(first_input, second_input)

        dir_name = "."
        test = os.listdir(dir_name)
        for item in test:
            if item.endswith(".json"):
                os.remove(os.path.join(dir_name, item))