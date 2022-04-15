from pathlib import Path
import random  

import argparse
parser = argparse.ArgumentParser(description='create train test val files')
parser.add_argument('-i', help='path to images folder', dest='path', required=True)
args = parser.parse_args()

def split_random():
    my_path=Path(args.path)
    if my_path.is_dir() == False:
        print('It should be a directory!')

    train = ''
    test = ''
    val = ''

    for file in my_path.iterdir():
        if str(file).endswith('jpg'):
            random_no=random.random()
            if random_no<=0.7:
                train = f'{train} {file} \n'
                train = f'{train} {str(file)[:-4]}.txt \n'
            elif 0.7<random_no<=0.85:
                val = f'{val} {file} \n'
                val = f'{val} {str(file)[:-4]}.txt \n'
            else:
                test = f'{test} {file} \n'
                test = f'{test} {str(file)[:-4]}.txt \n'


    (my_path.parent / 'train.txt').write_text(train)
    (my_path.parent / 'test.txt').write_text(test)
    (my_path.parent / 'val.txt').write_text(val)
    print('files created!')

if __name__=='__main__':
    split_random()