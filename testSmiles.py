import requests
import json

def get_smiles_by_english_name(IUPAC):
    eng_url = "http://192.168.1.122:7107/task/convert/smiles/eng"
    eng_name = IUPAC

    eng_dic = {"englishName": eng_name}
    eng_reponse = requests.post(eng_url, json.dumps(eng_dic))
    eng_result = json.loads(eng_reponse.content)
    return eng_result.get("data").get("smiles")

def get_smiles_by_chinese_name():
    chn_url = "http://192.168.1.122:7107/task/convert/smiles/chn"
    chn_name = "磺酸丁基吡啶硫酸氢盐"

    chn_dic = {"chineseName": chn_name}
    chn_reponse = requests.post(chn_url, json.dumps(chn_dic))
    chn_result = json.loads(chn_reponse.content)
    print(chn_result.get("data").get("smiles"))


if __name__ == '__main__':
    get_smiles_by_english_name()
    get_smiles_by_chinese_name()
