import os
for root, dirs, files in os.walk('pkg'):
    for f in files:
        print(os.path.join(root, f))
print('---')
for root, dirs, files in os.walk('functions'):
    for f in files:
        print(os.path.join(root, f))
print('---')
for root, dirs, files in os.walk('test_dir'):
    for f in files:
        print(os.path.join(root, f))
