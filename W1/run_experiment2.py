import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd
from bandit import Bandit

def run_experiment(mu,sigma,N,eps):

	bandit0 = Bandit(mu[0],sigma[0]) 
	bandit1 = Bandit(mu[1],sigma[1])
	bandit2 = Bandit(mu[2],sigma[2])

	count = np.arange(0,N)
	data = np.empty(N)
	summedreward = np.empty(N)
	averagereward = np.empty(N)
	
	n0 = 0 # number of times bandit0 is pulled
	n1 = 0 # number of times bandit1 is pulled
	n2 = 0 # number of times bandit2 is pulled
	
	mean0 = np.empty(N)
	mean1 = np.empty(N)
	mean2 = np.empty(N)
	var0 = np.empty(N)
	var1 = np.empty(N)
	var2 = np.empty(N)
	svar0 = np.empty(N)
	svar1 = np.empty(N)
	svar2 = np.empty(N)


#	pull each arm once
	data[0] = bandit0.play()
	mean0[0] = data[0]
	summedreward[0] = data[0]

	data[1] = bandit1.play()
	mean1[0] = data[1]
	summedreward[1] = data[0] + summedreward[0] 

	data[2] = bandit2.play()
	mean2[0] = data[2]
	summedreward[2] = data[0] + summedreward[1]

	for i in range(3,N):
		val = random.random() #returns random number in [0.0, 1.0)
		if val < eps:
			banditchoice = random.choice([0,1,2])
			if banditchoice == 0:
				n0 += 1
				data[i] = bandit0.play()
				mean0[n0], var0[n0], svar0[n0] = bandit0.get_statistics()
			if banditchoice == 1:
				n1 += 1
				data[i] = bandit1.play()
				mean1[n1], var1[n1], svar1[n1] = bandit1.get_statistics()
			if banditchoice == 2:
				n2 += 1
				data[i] = bandit2.play()
				mean2[n2], var2[n2], svar2[n2] = bandit2.get_statistics()
		else:
			banditchoice = np.argmax([ mean0[n0], mean1[n1], mean2[n2] ])
			if banditchoice == 0:
				n0 += 1
				data[i] = bandit0.play()
				mean0[n0], var0[n0], svar0[n0] = bandit0.get_statistics()
			if banditchoice == 1:
				n1 += 1
				data[i] = bandit1.play()
				mean1[n1], var1[n1], svar1[n1] = bandit1.get_statistics()
			if banditchoice == 2:
				n2 += 1
				data[i] = bandit2.play()
				mean2[n2], var2[n2], svar2[n2] = bandit2.get_statistics()

		summedreward[i] = data[i] + summedreward[i-1]

	for i in range(0,N):
		averagereward[i] = summedreward[i]/(1+count[i])

	print("Bandit 0 - pulled", n0+1, "times. Estimated mean -",mean0[n0] )
	print("Bandit 1 - pulled", n1+1, "times. Estimated mean -",mean1[n1] )	
	print("Bandit 2 - pulled", n2+1, "times. Estimated mean -",mean2[n2] )
	print("Total reward   - ", summedreward[N-1])
	print("Average reward - ", averagereward[N-1] )

	multi_bandit_plots(count, data, averagereward)

# plots using seaborn
def multi_bandit_plots(count, data, averagereward):
	description = { 'iteration':count, 'value':data, 'average reward':averagereward }
	pddata = pd.DataFrame(description)

	plt.rcParams['figure.figsize'] = [15,5]

	sns.set(style='darkgrid')
	ax1 = sns.scatterplot(x='iteration', y='value', data=pddata)	
	ax1.set(xscale="linear", yscale="linear")
	ax1.set_xlabel('')
	ax1.set_ylabel('')
	ax1.set_title('Data')

	plt.show()

	sns.set(style='darkgrid')
	ax2 = sns.lineplot(x='iteration', y='average reward', data=pddata)
	ax2.set(xscale="linear", yscale="linear")
	ax2.set_xlabel('')
	ax2.set_ylabel('')
	ax2.set_title('Average Reward')

	plt.show()


def main():

	seed = None
	N = 10000

	eps = 0.1

	nbandits = 3
	mu = np.empty(nbandits)
	sigma = np.empty(nbandits)

	mu[0] = 0
	mu[1] = 1
	mu[2] = -1
	
	sigma[0] = 1
	sigma[1] = 1
	sigma[2] = 1

	random.seed(seed) 

	run_experiment(mu, sigma, N, eps)	

if __name__== "__main__":
    main()
