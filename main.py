def bobotInput():
    while True:
        print("Tidak Yakin: 1 | Tidak Tahu: 2 | Sedikit Yakin: 3 | Cukup Yakin: 4 | Yakin: 5 | Sangat Yakin: 6")
        h = input("Masukan nilainya: ")
        if h.isdigit():
            h = int(h)
            if (h<1 or h>6):
                print("Inputan harus antara 1-6 !!")
                continue
            if h == 1:
                return 0
            if h == 2:
                return 0.2
            if h == 3:
                return 0.4
            if h == 4:
                return 0.6
            if h == 5:
                return 0.8
            if h == 6:
                return 1
        else:
            print("Inputan harus angka!")
            continue


bobotGejala = [None, 0.86, 0.76, 0.75, 0.69, 0.40, 0.33, 0.31, 0.28, 0.17, 0.24, 0.30]
gejalaUser = [None, ]

print("PROGRAM SISTEM PAKAR MENINGITIS")
# 1
print("Apakah Anda Mengalami Panas/Demam?")
G1 = bobotInput()
gejalaUser.append(G1)

# 2
print("Apakah Anda Mengalami Nyeri kepala?")
G2 = bobotInput()
gejalaUser.append(G2)

# 3
print("Apakah Anda Mengalami Kaku kuduk?")
G3 = bobotInput()
gejalaUser.append(G3)

# 4
print("Apakah Anda Mengalami Gangguan kesadaran?")
G4 = bobotInput()
gejalaUser.append(G4)

# 5
print("Apakah Anda Mengalami Mual muntah?")
G5 = bobotInput()
gejalaUser.append(G5)

# 6
print("Apakah Anda Mengalami Riwayat infeksi THT?")
G6 = bobotInput()
gejalaUser.append(G6)

# 7
print("Apakah Anda Mengalami Berat badan turun?")
G7 = bobotInput()
gejalaUser.append(G7)

# 8
print("Apakah Anda Mengalami Kejang?")
G8 = bobotInput()
gejalaUser.append(G8)

# 9
print("Apakah Anda Mengalami Anoreksia?")
G9 = bobotInput()
gejalaUser.append(G9)

# 10
print("Apakah Anda Mengalami Riwayat infeksi paru?")
G10 = bobotInput()
gejalaUser.append(G10)

# 11
print("Apakah Anda Mengalami Gejala neurologi lainnya?")
G11 = bobotInput()
gejalaUser.append(G11)

CFGGejala = [None, ]

for i in range(1, len(bobotGejala)):
    CFGGejala.append(gejalaUser[i] * bobotGejala[i])


def cfcombine(cf1: float, cf2: float) -> float:
    return cf1 + (cf2 * (1 - cf1))


DataPenyakit = {
    'Meningitis Tuberkolosis': [1, 2, 4, 5, 7, 8, 10, 11],
    'Meningitis Bakteri': [1, 2, 3, 5, 6, 9, 11],
    'Meningitis Virus': [1, 2, 3, 5, 7],
    'Meningitis Jamur': [1, 2, 3, 4, 5],
}

hasilDiagnosis = []

CfOld = cfcombine(cf1=bobotGejala[1], cf2=CFGGejala[2])
for p in DataPenyakit['Meningitis Tuberkolosis'][2:]:
    CfOld = cfcombine(cf1=CfOld, cf2=CFGGejala[p])

hasilDiagnosis.append(CfOld)

CfOld = cfcombine(cf1=bobotGejala[1], cf2=CFGGejala[2])
for p in DataPenyakit['Meningitis Bakteri'][2:]:
    CfOld = cfcombine(cf1=CfOld, cf2=CFGGejala[p])

hasilDiagnosis.append(CfOld)

CfOld = cfcombine(cf1=bobotGejala[1], cf2=CFGGejala[2])
for p in DataPenyakit['Meningitis Virus'][2:]:
    CfOld = cfcombine(cf1=CfOld, cf2=CFGGejala[p])

hasilDiagnosis.append(CfOld)

CfOld = cfcombine(cf1=bobotGejala[1], cf2=CFGGejala[2])
for p in DataPenyakit['Meningitis Jamur'][2:]:
    CfOld = cfcombine(cf1=CfOld, cf2=CFGGejala[p])

hasilDiagnosis.append(CfOld)
print(hasilDiagnosis)

hasilTertinggi = max(hasilDiagnosis)
hasilFinal = hasilDiagnosis.index(hasilTertinggi)
if hasilFinal == 0:
    print(f"\nTerdiagnosis 'Meningitis Tuberkolosis' sebesar: {hasilTertinggi}")
if hasilFinal == 1:
    print(f"\nTerdiagnosis 'Meningitis Bakteri' sebesar: {hasilTertinggi}")
if hasilFinal == 2:
    print(f"\nTerdiagnosis 'Meningitis Virus' sebesar: {hasilTertinggi}")
if hasilFinal == 3:
    print(f"\nTerdiagnosis 'Meningitis Jamur' sebesar: {hasilTertinggi}")

