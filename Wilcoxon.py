from scipy.stats import wilcoxon
from utils import assembly, python

# assembly
print('============  assembly  ===============')
exploitgen_rouge, exploitgen_acc= assembly.get_rouge_and_acc(raw_in_file='data/decoder-test.in', raw_out_file='data/decoder-test.out',
                       ip_file='result/raw_result/assembly/ExploitGen_raw.csv')

CodeGPT_rouge, CodeGPT_acc= assembly.get_rouge_and_acc(raw_in_file='data/decoder-test.in', raw_out_file='data/decoder-test.out',
                       ip_file='result/raw_result/assembly/CodeGPT_Adapted_raw.csv')

CodeBERT_rouge, CodeBERT_acc= assembly.get_rouge_and_acc(raw_in_file='data/decoder-test.in', raw_out_file='data/decoder-test.out',
                       ip_file='result/raw_result/assembly/CodeBERT_raw.csv')

stat, p = wilcoxon(exploitgen_rouge, CodeGPT_rouge)
print('codegpt, rouge-w')
print(p)
print('-----------------------')
stat, p = wilcoxon(exploitgen_acc, CodeGPT_acc)
print('codegpt, acc')
print(p)
print('-----------------------')
stat, p = wilcoxon(exploitgen_rouge, CodeBERT_rouge)
print('CodeBERT, rouge-w')
print(p)
print('-----------------------')
stat, p = wilcoxon(exploitgen_acc, CodeBERT_acc)
print('CodeBERT, acc')
print(p)

# python
print('============  python  ===============')
exploitgen_rouge, exploitgen_acc= python.get_rouge_and_acc(raw_in_file='data/encoder-test.in', raw_out_file='data/encoder-test.out',
                       ip_file='result/raw_result/python/ExploitGen_raw.csv')

CodeGPT_rouge, CodeGPT_acc= python.get_rouge_and_acc(raw_in_file='data/encoder-test.in', raw_out_file='data/encoder-test.out',
                       ip_file='result/raw_result/python/CodeGPT_Adapted_raw.csv')

CodeBERT_rouge, CodeBERT_acc= python.get_rouge_and_acc(raw_in_file='data/encoder-test.in', raw_out_file='data/encoder-test.out',
                       ip_file='result/raw_result/python/CodeBERT_raw.csv')

stat, p = wilcoxon(exploitgen_rouge, CodeGPT_rouge)
print('codegpt, rouge-w')
print(p)
print('-----------------------')
stat, p = wilcoxon(exploitgen_acc, CodeGPT_acc)
print('codegpt, acc')
print(p)
print('-----------------------')
stat, p = wilcoxon(exploitgen_rouge, CodeBERT_rouge)
print('CodeBERT, rouge-w')
print(p)
print('-----------------------')
stat, p = wilcoxon(exploitgen_acc, CodeBERT_acc)
print('CodeBERT, acc')
print(p)
