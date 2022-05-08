import csv
import code_tokenize as ctok
from tqdm import tqdm

from utils.OurCanonical import Canonical
import pandas as pd

from utils.eval import evaluate_list, get_details

canon = Canonical(remove=["is there (a|any)?", 'how (do|can|should|would) (i|you)',
                          '(programmatic|pythonic)(ally)?', '(with )?(in )?python', '[a-z ]*(possible|way|how) to ',
                          '(is there an? )?(in a )?(simple)|(easy) way( to)?|simply|easily', 'cant?( (i)|(you)|(we))?'],
                  replace={' an?[ .]': ' ', 'dictionary': 'dict', " the ": " "},
                  lower=False,
                  stemmer=None,
                  remove_punctuation=False,
                  std_var=True,
                  reserved_words='python'
                 )

def get_more_info(intent, snippet):
    try:
        # 解析器解析出变量参数、值
        canonical_intent, slot_map = canon.stdz_intent(intent) # parse
        # 处理
        final_intent = canon.clean_intent(canonical_intent)
        # 解析代码
        canonical_snippet = canon.canonicalize_code(snippet,slot_map)
        # 还原代码
        decanonical_snippet = canon.decanonicalize_code(canonical_snippet,slot_map)
    except:
        final_intent, slot_map, canonical_snippet, decanonical_snippet = intent, {}, snippet, snippet
    final_intent, canonical_snippet = final_intent.replace('\n',''), canonical_snippet.replace('\n','')
    return final_intent, slot_map, canonical_snippet, decanonical_snippet

def get_decanonical_snippet(intent, pred):
    try:
        # 解析器解析出变量参数、值
        canonical_intent, slot_map = canon.stdz_intent(intent) # parse
        # 还原代码
        decanonical_snippet = clean_code(canon.decanonicalize_code(pred,slot_map))
    except:
        decanonical_snippet = pred
    return decanonical_snippet

def clean_nl(text):
    text = text.replace("`` ", "``")
    text = text.replace(" ''", " '' ")
    return text

def clean_code(text):
    try:
        text = text.replace("\"","'")
        text = text.replace(",'",", '")
        code_list = ctok.tokenize(text, lang="python")
        code_list = [str(code) for code in code_list]
        return ' '.join(code_list)
    except:
        return text

def raw_to_ip_file(raw_in_file, raw_out_file, result_file):
    df = pd.read_csv(raw_in_file, header=None, sep='\n\r', engine='python', quoting=csv.QUOTE_NONE)
    in_list = df[0].tolist()
    df = pd.read_csv(raw_out_file, header=None, sep='\n\r', engine='python', quoting=csv.QUOTE_NONE)
    out_list = df[0].tolist()
    data_list = []
    for i in tqdm(range(len(out_list))):
        final_intent, slot_map, canonical_snippet, decanonical_snippet = get_more_info(clean_nl(in_list[i]), clean_code(out_list[i]))
        data_list.append([in_list[i], final_intent, clean_code(out_list[i]), clean_code(canonical_snippet)])

    df = pd.DataFrame(data_list, columns=['raw_nl', 'temp_nl', 'raw_code', 'temp_code'])
    df.to_csv(result_file, index=False)

def raw_to_ip(raw_in, raw_out):
    final_intent, slot_map, canonical_snippet, decanonical_snippet = get_more_info(clean_nl(raw_in),
                                                                                   clean_code(raw_out))
    return ([final_intent, slot_map, canonical_snippet, decanonical_snippet])

def ip_to_code_file(raw_in_file, raw_out_file, ip_file, result_file):
    df = pd.read_csv(raw_in_file, header=None, sep='\n\r', engine='python', quoting=csv.QUOTE_NONE)
    in_list = df[0].tolist()
    df = pd.read_csv(raw_out_file, header=None, sep='\n\r', engine='python', quoting=csv.QUOTE_NONE)
    out_list = df[0].tolist()
    try:
        df = pd.read_csv(ip_file, header=None)
    except:
        df = pd.read_csv(ip_file, header=None, sep='\n\r', engine='python', quoting=csv.QUOTE_NONE)
    pred_list = df[0].tolist()

    data_list = []
    for i in tqdm(range(len(out_list))):
        decanonical_snippet = get_decanonical_snippet(clean_nl(in_list[i]), pred_list[i])
        if (decanonical_snippet[0]==('\"') and decanonical_snippet[-1]==('\"')):
            decanonical_snippet = decanonical_snippet[1:-1]
        out_list[i] = clean_code(out_list[i])
        data_list.append(decanonical_snippet)

    result = evaluate_list(data_list, out_list)
    print(result)
    df = pd.DataFrame(data_list)
    df.to_csv(result_file, index=False, header=None)


def get_rouge_and_acc(raw_in_file, raw_out_file, ip_file):
    df = pd.read_csv(raw_in_file, header=None, sep='\n\r', engine='python', quoting=csv.QUOTE_NONE)
    in_list = df[0].tolist()
    df = pd.read_csv(raw_out_file, header=None, sep='\n\r', engine='python', quoting=csv.QUOTE_NONE)
    out_list = df[0].tolist()
    try:
        df = pd.read_csv(ip_file, header=None)
    except:
        df = pd.read_csv(ip_file, header=None, sep='\n\r', engine='python', quoting=csv.QUOTE_NONE)
    pred_list = df[0].tolist()

    data_list = []
    for i in tqdm(range(len(out_list))):
        decanonical_snippet = get_decanonical_snippet(clean_nl(in_list[i]), pred_list[i])
        if (decanonical_snippet[0]==('\"') and decanonical_snippet[-1]==('\"')):
            decanonical_snippet = decanonical_snippet[1:-1]
        out_list[i] = clean_code(out_list[i])
        data_list.append(decanonical_snippet)
    return get_details(data_list, out_list)

