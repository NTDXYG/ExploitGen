from utils import assembly, python

# for python data
python.raw_to_ip_file(raw_in_file='./encoder-train.in', raw_out_file='./encoder-train.out',
                      result_file='./python/train.csv')
python.raw_to_ip_file(raw_in_file='./encoder-dev.in', raw_out_file='./encoder-dev.out',
                      result_file='./python/dev.csv')
python.raw_to_ip_file(raw_in_file='./encoder-test.in', raw_out_file='./encoder-test.out',
                      result_file='./python/test.csv')

# for assembly data
assembly.raw_to_ip_file(raw_in_file='./decoder-train.in', raw_out_file='./decoder-train.out',
                      result_file='./assembly/train.csv')
assembly.raw_to_ip_file(raw_in_file='./decoder-dev.in', raw_out_file='./decoder-dev.out',
                      result_file='./assembly/dev.csv')
assembly.raw_to_ip_file(raw_in_file='./decoder-test.in', raw_out_file='./decoder-test.out',
                      result_file='./assembly/test.csv')