# Write code to assign to the variable compri_sample all the values of the key name 
in the dictionary tester if they are Juniors. Do this using list comprehension.



tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

compri_sample = [i["name"] for key1,value1 in tester.items() for i in value1 for key2,value2 in i.items() if value2 == 'Junior']