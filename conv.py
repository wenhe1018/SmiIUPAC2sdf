import pandas as pd
import rdkit
from rdkit import Chem
w = Chem.SDWriter('Premium.sdf')
fi = r'Premium_Set_Library.xls'
data = pd.read_excel(fi,sheet_name='1335-1',usecols='D,T') #skiprows=[:6]
# print(data)

dic = data.set_index('ID').to_dict()['Parent smiles']

cpd_name = list(dic.keys())
smiles = list(dic.values())
for i in range(len(cpd_name)):
    try:
        m = Chem.MolFromSmiles(smiles[i])
        m.SetProp('_Name',str(cpd_name[i]))
        w.write(m)
    except AttributeError as e:
        print(cpd_name[i])

    
