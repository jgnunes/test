import os 
import subprocess

path = os.getcwd()
listOfFiles = os.listdir(path)

for element in listOfFiles:
	if 'ligand.pdb' in element: #seleciona o arquivo PDB do ligante 
		subprocess.call("python2 prepare_ligand4.py -l " + element)
		ligandPDBQT = element[:len(element)-4] + ".pdbqt" #guarda o arquivo .pdbqt do ligante 
	if 'receptor.pdb' in element: #seleciona os arquivos PDB dos mutantes de acrB
		subprocess.call("python2 prepare_receptor4.py -r " + element)


listOfFiles = os.listdir(path)  # atualiza a lista de arquivos, incluindo os .pdbqt's

for element in listOfFiles:
	if ('receptor.pdbqt' in element): #gera o grid parameter file (gpf) e o docking parameter file (gpf) 
 		subprocess.call("python2 prepare_gpf4.py -r " + element + " -l " + ligandPDBQT)
		subprocess.call("python2 prepare_dpf4.py -r " + element + " -l " + ligandPDBQT)
	


listOfFiles = os.listdir(path) # atualiza a lista de arquivos, incluindo os .gpf e .dpf

for element in listOfFiles:
	if ('receptor' in element) and ('.gpf' in element):
		subprocess.call("autogrid4 -p " + element + " -l " + element[:len(element)-4] + ".glg")
	if ('receptor' in element) and ('.dpf' in element):
		subprocess.call("autodock4 -p " + element + " -l " + element[:len(element)-4] + ".glg") #roda a docagem, em si, gerando arquivos .glg
