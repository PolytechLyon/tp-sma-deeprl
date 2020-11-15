import numpy as np
import matplotlib.pyplot as plt


def plot_sumrwdperepi(sum_rewards):
    "trace courbe de somme des rec par episodes"
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(np.arange(len(sum_rewards)), sum_rewards)
    plt.ylabel('Score')
    plt.xlabel('Episode #')
    plt.show()
    
