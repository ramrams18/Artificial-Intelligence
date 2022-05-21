import sys
import re

def __main__(argv):
    if argv[1]:
        pat = re.compile('^[LC]+$')
        seq = argv[1].upper()
        if pat.match(seq):

            # possibilities of lime and cherries
            lime = 0
            cherry = 0
            for i in range(0,5):
                lime = lime + (p_lime[i]*p_hyp[i])
                cherry = cherry + (p_cherry[i]*p_hyp[i])

                
            f = open("result.txt", "w")
            f.write("observation sequence Q: " + str(seq))
            f.write("\nlength of Q: " + str(len(seq)))
            for j in range(0, len(seq)):
                
                c = seq[j]
                f.write("\n\nafter observation "+str(j+1)+" = "+str(c)+"\n")

                # possibility of 'H' given sequence
                if c == 'L':
                    s = p_lime
                    d = lime
                else:
                    s = p_cherry
                    d = cherry
                for i in range(0,5):
                    p_hyp[i] = (p_hyp[i]/d)*s[i]
                    f.write('\nP(h' + str(i) + ' | Q) = ' + str(round(p_hyp[i],5)))

                # possibility of lime and cherry
                lime = 0
                cherry = 0
                for i in range(0,5):
                    lime = lime + (p_lime[i]*p_hyp[i])
                    cherry = cherry + (p_cherry[i]*p_hyp[i])

                f.write('\n\nprobability that the next candy we pick will be C, given Q: ' + str(round(cherry, 5)))
                f.write('\nprobability that the next candy we pick will be L, given Q: ' + str(round(lime, 5)))

        else:
            exit('sequence should have series of L or M')
    else:
        exit("follow the syntax: \npython compute_a_posteriori.py [sequence]")

p_hyp = [0.10, 0.20, 0.40, 0.20, 0.10]
p_cherry = [1.00, 0.75, 0.50, 0.25, 0.00]
p_lime = [0.00, 0.25, 0.50, 0.75, 1.00]
__main__(sys.argv)
