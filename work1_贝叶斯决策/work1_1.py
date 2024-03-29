import numpy as np


def decisionMaking1(Px_w1,Px_w2,Pw1,Pw2):
    Px = Px_w1 + Px_w2
    Pw1_x = Px_w1 * Pw1 / Px
    Pw2_x = Px_w2 * Pw2 / Px
    if(Pw1_x > Pw2_x):
        print("属于w1:%.3f"%(Pw1_x))
        return 1
    else:
        print("属于w2:%.3f"%(Pw2_x))
        return 2

def decisionMaking2(Px_w1,Px_w2,Pw1,Pw2):
    P1 = Px_w1 * Pw1
    P2 = Px_w2 * Pw2
    if(P1 > P2):
        print("属于w1")
        return 1
    else:
        print("属于w2")
        return 2

def decisionMaking3(Px_w1,Px_w2,Pw1,Pw2):
    l = Px_w1 / Px_w2
    lemda = Pw2 / Pw1
    if(l > lemda):
        print("属于w1")
        return 1
    else:
        print("属于w2")
        return 2

def decisionMaking4(Px_w,Pw):
    if(Px_w.shape != Pw.shape):
        return
    Px_w = np.asarray(Px_w)
    Pw = np.asarray(Pw)
    Pw_whole = np.sum(Pw)
    Pw_x = np.zeros((Px_w.shape))
    for i, Px_w_dot in enumerate(Px_w):
        Pw_x[i] = Px_w_dot / Pw_whole  # 将概率归一化为总和

    # 输出结果
    max_prob = np.max(Pw_x)
    max_class = np.argmax(Pw_x)
    print("属于w%d的概率为 %.3f" % (max_class, max_prob))

        
        


if __name__ == '__main__':
   # decisionMaking1(0.32,0.18,0.9,0.1)
   Px_w = np.array([1, 2, 3])
   Pw = np.array([0.2, 0.3, 0.5])
   decisionMaking4(Px_w, Pw)