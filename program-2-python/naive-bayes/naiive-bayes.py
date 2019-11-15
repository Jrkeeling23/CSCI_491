# Write your code here for Part 1. You are welcome to add more cells.
import os, re


# print(os.path.exists("bc2_ips_pmid2ppi_train.txt")) #Will print "False" if the file is not uploaded by first running the above cell.

def load_interactions(file_name):
    print(os.path.exists(file_name))  # Will print "False" if the file is not uploaded by first running the above cell.
    data = list(uploaded.values())[0].decode('utf-8')  # decode from bytes to string
    #   int_id = re.findall("\n([A-Z0-9]+)\t", data)
    #   print(int_id)
    proteins_1 = re.findall("\t([A-Z0-9]+)\t", data)  # captures all the 'first' protein that appear in an interaction
    proteins_2 = re.findall("([A-Z0-9]+)\n+", data)  # captures all the 'second' protein that appear in an interaction
    interaction_list = list()

    for i in range(len(proteins_1)):  # Iterate through the proteins
        interaction_list.append((proteins_1[i], proteins_2[i]))  # Append the tuple of proteins to a list
    return interaction_list  # Returns a list of tuples


interactions2 = load_interactions('bc2_ips_pmid2ppi_train.txt')


def interact(interactions, id1, id2):
    for tuple_proteins in interactions:  # Iterate through each tuple
        if id1 in tuple_proteins and id2 in tuple_proteins:  # check if both id1 AND id2 are in the same tuple; True
            return True
    return False  # else false


protein1 = 'YPL094C'
protein2 = 'YPR086W'


# test = 'O88643'
# print(interact(interactions2, 'YPL094C', 'YPR086W'))
# print(interact(interactions2, 'YPR086W', 'YPL094C'))


def get_interactions(interactions, id_name):
    interacted = list()  # list to hold potential proteins that interact with id_name

    for tuple_proteins in interactions:  # Iterate through each tuple

        id1 = tuple_proteins[0]  # Set variable to first element in tuple
        id2 = tuple_proteins[1]  # Set variable to second element in tuple

        if id_name == id1:  # check if given id is in tuple; True, add id2 to list
            interacted.append(id2)
        elif id_name == id2:  # check if given id is in tuple;  True, add id1 to list
            interacted.append(id1)
    return interacted  # Returns a list of interacted proteins


# print(get_interactions(interactions2,  'Q14790'))


def average_interactions(interactions):
    protein_appearance = {}  # a dictionary structured as;  protein: occurances
    total_occurances = 0  # documents ALL protein occurances
    for tuple_proteins in interactions:  # iterate through data
        for protein in tuple_proteins:  # iterate through proteins in the tuples
            if protein in protein_appearance.keys():  # check whether the protein is in dictionary
                continue  # next protein
            else:
                #         print(protein)
                total_occurances = total_occurances + len(
                    get_interactions(interactions, protein))  # total all the occurances
                protein_appearance[protein] = len(get_interactions(interactions, protein))  #
    for k, v in protein_appearance.items():
        pass
        # print(" { ", k, " " , v ,"} " )
    #   print("total occurance ", total_occurances, " uniq_ids = " ,len(protein_appearance.keys()) )
    #   print(total_occurances/len(protein_appearance.keys()))
    return total_occurances / len(protein_appearance.keys())


average_interactions(interactions2)