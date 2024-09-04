from BQA import answer_question
import os
content_list = ['zero','overview.txt','causes.txt','symptoms.txt','risk_factors.txt','prevention.txt','diagnosis.txt','treatment.txt']
content_name = ['zero','Overview','Causes','Symptoms','Risk Factors','Prevention','Diagnosis','Treatment']
cancer_path = ['zero',os.path.realpath('../data/breast_cancer'), os.path.realpath('../data/colorectal_cancer'), os.path.realpath('../data/lung_cancer'), os.path.realpath('../data/prostate_cancer'), os.path.realpath('../data/skin_cancer')]
cancer_name=['zero','Breast Cancer','Colorectal Cancer','Lung Cancer','Prostate Cancer','Skin Cancer']
while(True):
    print("Choose a Cancer Type to Ask question :")
    print("1. "+cancer_name[1]+"\n2. "+cancer_name[2]+"\n3. "+cancer_name[3]+"\n4. "+cancer_name[4]+"\n5. "+cancer_name[5]+"\n6. EXIT")
    ch1=int(input())
    if ch1>6 or ch1<1:
        print("Invalid Choice. Enter only between 1 - 6. Try Again")
        continue
    elif ch1==6:
        break
    while(True):
        print("Choose the Area to Ask Question :")
        print("1. "+cancer_name[ch1]+" "+content_name[1]+"\n2. "+cancer_name[ch1]+" "+content_name[2]+"\n3. "+cancer_name[ch1]+" "+content_name[3]+"\n4. "+cancer_name[ch1]+" "+content_name[4]+"\n5. "+cancer_name[ch1]+" "+content_name[5]+"\n6. "+cancer_name[ch1]+" "+content_name[6]+"\n7. "+cancer_name[ch1]+" "+content_name[7]+"\n8. <---- Main Menu")
        ch2=int(input())
        if ch2>8 or ch2<1:
            print("Invalid Choice. Enter only between 1 - 8 . Try Again ")
            continue
        elif ch2==8:
            break
        else:
            while(True):
                print("Ask your Question about "+cancer_name[ch1]+" "+content_name[ch2]+": ",end="")
                question=input()
                with open(os.path.join(cancer_path[ch1], content_list[ch2]), 'r') as f:
                    related_content = f.read()
                print("Answer is : "+answer_question(question, related_content)+"\n")
                print("Any Other Questions: Y / N ")
                qs=input()
                if(qs.upper()=='Y'):
                    continue
                elif(qs.upper()=='N'):
                    break
                else:
                    print("Please Enter only \"Y\" or \"N\"")
                    qs = input()
                    if (qs.upper() == 'Y'):
                        continue
                    elif (qs.upper() == 'N'):
                        break

'''
with open(os.path.join(os.path.realpath('../data/breast_cancer'), 'causes.txt'), 'r') as f:
    related_content = f.read()
generated_answer = answer_question("what are causes of breast cancer?", related_content)
print(generated_answer)
'''