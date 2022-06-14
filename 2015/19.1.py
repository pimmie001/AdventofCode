with open("19.txt") as fh:
    content = fh.read().split("\n\n")

reactions = content[0].split("\n")
starting_molecule = content[1]


listofmolecules = []
for reaction in reactions:
    molecule = reaction.split(" =>",1)[0]
    if molecule not in listofmolecules:
        listofmolecules.append(molecule)


end_molecules = []
for i in range(len(starting_molecule)):
    for reaction in reactions:
        newmolecule = starting_molecule
        reaction = reaction.split(" => ")
        start = reaction[0]
        end = reaction[1]

        if start == starting_molecule[i]:      # lenght is 1
            newmolecule = newmolecule[:i] + end + newmolecule[i+1:]
            if newmolecule not in end_molecules:
                end_molecules.append(newmolecule)

        elif start == starting_molecule[i:i+2]:
            newmolecule = newmolecule[:i] + end + newmolecule[i+2:]
            if newmolecule not in end_molecules:
                end_molecules.append(newmolecule)

print(len(end_molecules))