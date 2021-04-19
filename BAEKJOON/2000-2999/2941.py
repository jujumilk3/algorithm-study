string = input()
cro_alphas = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for cro in cro_alphas:
    string = string.replace(cro, '1')
print(len(string))
