print("""Notice :
            This is a program devoleped for learning purpose.
            This program can approximately calculate your 12th mark.
            Thanks for using this. 
            """)

mark_10_1 = int(input("Enter the 1st best mark you get in 10th : "))
mark_10_2 = int(input("Enter the 2nd best mark you get in 10th : "))
mark_10_3 = int(input("Enter the 3rd best mark you get in 10th : "))
mark_10_total = mark_10_1+mark_10_2+mark_10_3
mark_10_fulltotal = mark_10_total/300 * 50

mark_11_tam = int(input("Enter the Tamil theory mark you get in 11th : "))
mark_11_eng = int(input("Enter the English theory mark you get in 11th : "))
mark_11_mat = int(input("Enter the Maths theory mark you get in 11th : "))
mark_11_phy = int(input("Enter the Physics theory mark you get in 11th : "))
mark_11_che = int(input("Enter the Chemistry theory mark you get in 11th : "))
mark_11_com = int(input("Enter the ComputerScience theory mark you get in 11th : "))


mark_11_tamtot = mark_11_tam/90*20
mark_11_engtot = mark_11_eng/90*20
mark_11_mattot = mark_11_mat/90*20
mark_11_phytot = mark_11_phy/70*20
mark_11_chetot = mark_11_che/70*20
mark_11_comtot = mark_11_com/70*20

mark_12_1 = 30
mark_12_2 = 30
mark_12_3 = 30
mark_12_4 = 30
mark_12_5 = 30
mark_12_6 = 30

num_11 = (round(mark_11_tamtot),round(mark_11_engtot),round(mark_11_mattot),round(mark_11_phytot),round(mark_11_chetot),round(mark_11_comtot))

for x in num_11:
    print(x)

tot_10 = mark_10_fulltotal * 6
tot_11 = sum(num_11)
tot_12 = 30*6


def totalmark():
    fullmark = tot_10+tot_11+tot_12
    print("Total 10th mark %s" %round(mark_10_fulltotal))
    print("Total 11th mark %s" %tot_11)
    print("Total 12th mark %s" %round(fullmark))

totalmark()
