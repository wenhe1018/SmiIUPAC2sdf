from testSmiles import get_smiles_by_english_name
import pandas as pd
import rdkit
from rdkit import Chem
w = Chem.SDWriter('Hit_creator.sdf')
fi = r'Hit_Creator_Library.xlsx'
data = pd.read_excel(fi,sheet_name='Sheet1',usecols='C,E') #skiprows=[:6]
# print(data)

dic = data.set_index('Compound ID').to_dict()['product_description']

cpd_name = list(dic.keys())
IUPAC = list(dic.values())
for i in range(len(cpd_name)):
    try:
        smiles = get_smiles_by_english_name(IUPAC[i])
        m = Chem.MolFromSmiles(smiles)
        m.SetProp('_Name',str(cpd_name[i]))
        w.write(m)
    except TypeError as e:
        print(cpd_name[i])