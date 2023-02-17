# need to do something for -ve rewards which we get for reaching the goal very late.
# It gets propagates and might effect the value function in the wrong way.

import gym
import numpy as np 
import random
import matplotlib.pyplot as plt


env = gym.make('MiniGrid-Empty-8x8-v0',render_mode='rgb_array')
env.reset()
iteration_list,epoch_list,reward_list=[],[],[]
n=3  # size of grid seen in rendering
Q_lookup=np.zeros((6,6,4,3))  # n * n * directions * actions
# print(Q_lookup[])
gamma= 0.9
alpha=1/20  # step size can be reduced further
Lambda=0.9
epsilon=1
max_epoch,min_epoch=20,-8

def update(prev_pos,new_pos,prev_dirn,new_dirn,action,imm_reward,Q_table):
    Qval_max = max(Q_table[new_pos[0]-1][new_pos[1]-1][new_dirn])
    change = (imm_reward+gamma*Qval_max) - Q_table[prev_pos[0]-1][prev_pos[1]-1][prev_dirn][action]
    Q_table[prev_pos[0]-1][prev_pos[1]-1][prev_dirn][action]=Q_table[prev_pos[0]-1][prev_pos[1]-1][prev_dirn][action]+alpha*change

for i in range(min_epoch,max_epoch+75):

    epoch_list.append(i+min_epoch)
    done,n,reward=0,1,0
    env.reset()
    if(i>0 and i<max_epoch+1):
        epsilon=1-i/max_epoch
    print('--'*50,'\n',i,'epoch')
    while(n<700 and not done):
        env.render()
        prev_pos=env.agent_pos
        prev_dir=env.agent_dir

        prob_decider=random.uniform(0,1)
        if(epsilon>=prob_decider):
            act=random.randint(0,2)
        else:
            act=np.argmax(Q_lookup[prev_pos[0]-1][prev_pos[1]-1][prev_dir])
            if(n<10):
                print(n,'iteration and action chosen greedily')

        a,reward,done,d,e=env.step(act)
        # print(prev_pos,env.agent_pos,prev_dir,env.agent_dir,act,b)
        if(reward):
            print(n,'itreartion has reward',reward)
        update(prev_pos,env.agent_pos,prev_dir,env.agent_dir,act,reward,Q_lookup)
        # print(n,'iteration successful')
        if(not n%100 or done):
            print("iteration",n,'and done is',done)
            # print(Q_lookup)
        n=n+1
    iteration_list.append(n)
    reward_list.append(reward)


def plot_3D():  # plotting the values of angles calculated in each iteration
    fig=plt.figure()
    ax=plt.axes(projection='3d')
    ax.plot3D(epoch_list,reward_list,iteration_list)
    ax.scatter3D(epoch_list,reward_list,iteration_list,marker='o')
    ax.set_xlabel("No. of Epochs")
    ax.set_ylabel("Reward obtained")
    ax.set_zlabel("No. of steps required to reach the goal")
    plt.title("MiniGrid EmptyRoom Environment 8x8")
    plt.show()



print(epoch_list)
print('\n\n')
print(reward_list)
print('\n\n')
print(iteration_list)
# fig=plt.figure()
plt.plot(reward_list)
plt.xlabel('No. of Epochs')
plt.ylabel('No. of steps required to reach the goal')
plt.show()
plot_3D()
