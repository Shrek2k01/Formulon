


print('0.3 BETA')
print()
print('==============================================')
print('Bem-vindo!')
print('==============================================')
print()
print('Instruções:')

print('1. Não utilzar em provas')
print('2. Se a variavel não existir, insira 0(zero)')
print('3. Se errar algum número, não sera possivel editar')
print()
print('bons estudos')
print()

print()
w1 = input('Enter para iniciar os calculos')
print()

op1 = 0
while op1 !=4:
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print('\n'*500)
    print("[1] Sistemas lineares")
    print("[2] Fatorial")
    print("[3] Lei de Coulumb")
    print("[4] Sair")
    print()
    print()

    op1 = int(input("Opção:"))
    print()
    print()
    if op1 ==1:






        opcao = 0
        while opcao !=3:
            print('\n'*500)
            print('[1] Realizar calculos 2x2')
            print('[2] Realizar calculos 3x3')
            print('[3] Sair')
            print('[4] Créditos')
            print()
            opcao = int(input('Opção:'))
            print()
            print()
            if opcao == 1:
                print('\n'*500)
                x1 = int(input('X da primeira linha'))
                y1 = int(input('Y da primeira linha'))
                i1 = int(input('I da primeira linha'))
                x2 = int(input('X da segunda linha'))
                y2 = int(input('Y da segunda linha'))
                i2 = int(input('I da segunda linha'))

                D= (x1*y2)-(y1*x2)
                Dx = (i1*y2)-(y1*i2)
                Dy = (x1*i2)-(i1*x2)

                X = Dx/D
                Y = Dy/D
                print('Conjunto verdade é ... V=({', X, Y, '})')
                tt5 = input("Enter para prosseguir")


            elif opcao == 2:
                print('\n'*500)
                x1 = int(input('X da primeira linha'))
                y1 = int(input('Y da primeira linha'))
                z1 = int(input('Z da primeira linha'))
                i1 = int(input('I da primeira linha'))
                x2 = int(input('X da segunda linha'))
                y2 = int(input('Y da segunda linha'))
                z2 = int(input('Z da segunda linha'))
                i2 = int(input('I da segunda linha'))
                x3 = int(input('X da terceira linha'))
                y3 = int(input('Y da terceira linha'))
                z3 = int(input('Z da terceira linha'))
                i3 = int(input('I da terceira linha'))

                d = (x1*y2*z3)+(y1*z2*x3)+(z1*x2*y3)-(z1*y2*x3)-(x1*z2*y3)-(y1*x2*z3)
                dx = (i1*y2*z3)+(y1*z2*i3)+(z1*i2*y3)-(z1*y2*i3)-(i1*z2*y3)-(y1*i2*z3)
                dy = (x1*i2*z3)+(i1*z2*x3)+(z1*x2*i3)-(z1*i2*x3)-(x1*z2*i3)-(i1*x2*z3)
                dz = (x1*y2*i3)+(y1*i2*x3)+(i1*x2*y3)-(i1*y2*x3)-(x1*i2*y3)-(y1*x2*i3)

                x = (dx/d)
                y = (dy/d)
                z = (dz/d)

                print('Conjunto verdade é... V=({', x, y, z, '})')
                tt4 = input("Enter para prosseguir")


            elif opcao == 3:
        
                print('Volte Sempre')
        

            elif opcao == 4:
                print()
                print()
                print()
                print('Criado por: João Victor')
                print('2018')
                print('Brusque - Santa Catarina')
                print('EEB Santa Terezinha')
                print('A responsabilidade de uso é dos alunos, e não do desenvolvedor')
                print(':)')
                print()
                print()
                print()

    elif op1 ==2:

        f1 = 0
        t1 = 0
        totalp = 1
        totaln = 1
        totaln1 = 1
        totalp1 = 1
        totaln2 = 1
        totalp2 = 1
        
        while f1 !=4:
            print("\n"*500)
            print("[1] Permutação")
            print("[2] Arranjo")
            print("[3] Combinação")
            print("[4] Sair")

            f1 = int(input("Opção:"))

            if f1 == 1:
                n = int(input("N ="))

                for n in range(n):
                    totaln = totaln * (n + 1)

                print(totaln)
                tt3 = input("Enter para prosseguir")

                
            elif f1 == 2:
                print('\n'*200)
                n1 = int(input("N="))
                p1 = int(input("P="))

                for n1 in range(n1):
                    totaln1 = totaln1 * (n1 + 1)

                for p1 in range(p1):
                    totalp1 = totalp1 * (p1 + 1)

                k1 = totaln1
                k2 = totalp1

                t1 = k1 - k2
                t2 = (k1/t1)
                
                print(t2)    
                print(k1, t1, k2)
                tt1 = input("Enter para prosseguir")

            elif f1 == 3:
                print("\n"*500)
                n2 = int(input("N="))
                p2 = int(input("P="))

                for n2 in range(n2):
                    totaln2 = totaln2 * (n2 + 1)

                for p2 in range(p2):
                   totalp2 = totalp2 * (p2 + 1)

                k3 = totaln2
                k4 = totalp2

                t3 = k3 - k4
                t4 = (k3/t3)-k3
                
                print(t4)    
                print(k3, t3, k4)
                tt2 = input("Enter para prosseguir")

                   

                        


                        

                    
                         

                

    elif op1 ==3:

        print()
    
                    
                

                        
    





        


        
