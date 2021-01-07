import numpy as np
import matplotlib.pyplot as plt


def plot_sumrwdperepi(sum_rewards):
    """ Trace courbe de somme des rec par episodes
    
    Params
    ======
        sum_rewards : liste contenant pour chaque épisode, la somme des récompenses obtenues sur l'épisode
    """

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(np.arange(len(sum_rewards)), sum_rewards)
    plt.ylabel('Score')
    plt.xlabel('Episode #')
    plt.show()
    
    
def plot_sumrwd_mean_perepi(sum_rewards,avgs):
    """ Trace courbe de somme des rec par episodes et moyenne glissante en rouge 
    
    Params
    ======
        sum_rewards : liste contenant pour chaque épisode, la somme des récompenses obtenues sur l'épisode
        avgs : liste contenant la moyenne glissante de la somme des rec par episode
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(np.arange(len(sum_rewards)), sum_rewards, label='sum_rwd')
    plt.plot(np.arange(len(sum_rewards)), avgs, c='r', label='average')
    plt.ylabel('Sum_rewards')
    plt.xlabel('Episode #')
    plt.legend(loc='upper left');
    plt.show()