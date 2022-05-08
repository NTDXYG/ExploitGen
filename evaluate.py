from utils import assembly, python

# assembly
# assembly.ip_to_code_file(raw_in_file='data/decoder-test.in', raw_out_file='data/decoder-test.out',
#                          ip_file='result/raw_result/assembly/ExploitGen_raw.csv',
#                          result_file='result/post_result/assembly/ExploitGen_post.csv')

# python
python.ip_to_code_file(raw_in_file='data/encoder-test.in', raw_out_file='data/encoder-test.out',
                       ip_file='result/raw_result/python/ExploitGen_raw.csv',
                       result_file='result/post_result/python/ExploitGen_post.csv')
