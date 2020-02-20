with open('Pt_LAS_191015.txt', encoding='utf-8') as f:
    for row in f:
        max_len = int(len(row) /3)
        print(max_len)
        codon_seq = []
        for i in range(0, max_len):
            codon_seq.append(row[3*i: 3*i+3])
        #codon_seq = [row[3i: 3i+2] for i in range(0,max_len)]:
        print(codon_seq)
        print('----------------------------------------------------')
        print('\n')
        print('<The number of amino acids is',len(codon_seq),' aa>')
        print('\n')


R_rare_codon = ['AGA', 'AGG', 'CGG']
G_rare_codon = ['GGA']
I_rare_codon = ['ATA']
L_rare_codon = ['CTA']
P_rare_codon = ['CCC']
print('Below codons are considered as rare codons')
print('R_rare_codon:', R_rare_codon)
print('G_rare_codon:', G_rare_codon)
print('I_rare_codon:', I_rare_codon)
print('L_rare_codon:', L_rare_codon)
print('P_rare_codon:', P_rare_codon)
print('\n')

num_R_rare_codon = 0
num_G_rare_codon = 0
num_I_rare_codon = 0
num_L_rare_codon = 0
num_P_rare_codon = 0

R_rare_codon_in_cds =[]
G_rare_codon_in_cds =[]
I_rare_codon_in_cds =[]
L_rare_codon_in_cds =[]
P_rare_codon_in_cds =[]

for codon in codon_seq:
    if codon in R_rare_codon:
        R_rare_codon_in_cds.append(codon)
        #print(R_rare_codon_in_cds)
        num_R_rare_codon += 1
    elif codon in G_rare_codon:
        G_rare_codon_in_cds.append(codon)
        #print(G_rare_codon_in_cds)
        num_G_rare_codon += 1
    elif codon in I_rare_codon:
        I_rare_codon_in_cds.append(codon)
        #print(I_rare_codon_in_cds)
        num_I_rare_codon += 1
    elif codon in L_rare_codon:
        L_rare_codon_in_cds.append(codon)
        #print(L_rare_codon_in_cds)
        num_L_rare_codon += 1
    elif codon in P_rare_codon:
        P_rare_codon_in_cds.append(codon)
        #print(P_rare_codon_in_cds)
        num_P_rare_codon += 1
    else:
        pass

print('----------------------------------------------------')
print('<<<Analysis Result>>>', '\n','\n', '<The number of rare codons>')
print(num_R_rare_codon, ' R_rare codon(s) were found in this cds:', list(set(R_rare_codon_in_cds)))
print(num_G_rare_codon, ' G_rare codon(s) were found in this cds:', list(set(G_rare_codon_in_cds)))
print(num_I_rare_codon, ' I_rare codon(s) were found in this cds:', list(set(I_rare_codon_in_cds)))
print(num_L_rare_codon, ' L_rare codon(s) were found in this cds:', list(set(L_rare_codon_in_cds)))
print(num_P_rare_codon, ' P_rare codon(s) were found in this cds:', list(set(P_rare_codon_in_cds)))

total_rare_codon = num_R_rare_codon + num_G_rare_codon +num_I_rare_codon+num_L_rare_codon+ num_P_rare_codon
print('Total rare codons: ', total_rare_codon)
print('\n')

R_list = list(set(R_rare_codon_in_cds))
#print(R_list)
all_rare_codon_in_cds = R_list + G_rare_codon + I_rare_codon + L_rare_codon + P_rare_codon
#print(all_rare_codon_in_cds)

print('<The position of each rare codon>')
print('R rare codon (AGG) were found at  ', [i for i, x in enumerate(codon_seq) if x == ('AGG')])
print('R rare codon (CGG) were found at  ', [i for i, x in enumerate(codon_seq) if x == ('CGG')])
print('R rare codon (AGA) were found at  ', [i for i, x in enumerate(codon_seq) if x == ('AGA')])
print('G rare codon (GGA) were found at  ', [i for i, x in enumerate(codon_seq) if x == ('GGA')])
print('I rare codon (ATA) were found at  ', [i for i, x in enumerate(codon_seq) if x == ('ATA')])
print('L rare codon (CTA) were found at  ', [i for i, x in enumerate(codon_seq) if x == ('CTA')])
print('P rare codon (CCC) were found at  ', [i for i, x in enumerate(codon_seq) if x == ('CCC')])
print('\n')
print('----------------------------------------------------')
