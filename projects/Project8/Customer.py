import numpy as np
import pandas as pd
import random


# In[23]:


data = pd.read_csv('customers_all.csv')


# In[24]:


LOC = ['drinks', 'dairy', 'fruit', 'spices', 'checkout']


# In[25]:


data['transition'] = data['location'].shift(-1)
data


# In[26]:


data.groupby(['location', 'transition']).count()


# In[27]:


P = pd.crosstab(data['location'], data['transition'], normalize='index')
P


# In[28]:


current_state = [0,1,0,0,0] 


# In[29]:


P.loc['dairy']


# In[30]:


np.dot(current_state, P)


# In[31]:


# choose, given the current probability distribution, a next stat
np.random.choice(LOC, p=P.loc['dairy'])


# In[32]:


# What is the probability for the conditions in two days?
np.dot(np.dot(current_state, P), P)


# In[36]:


#stationary distribution
P.dot(P).dot(P).dot(P).dot(P).dot(P).dot(P).dot(P)


# In[37]:


# convert array into dataframe
df = pd.DataFrame(P)


# In[38]:


# save the dataframe as a csv file
df.to_csv("matrix.csv")


# In[39]:


#Transition probabilities matrix
matr = pd.read_csv('matrix.csv', index_col=0)
#States of Markov chain
LOC = ['drinks', 'dairy', 'fruit', 'spices', 'checkout']


# In[40]:


class Customer:
    '''
    Customer class that simulates a Markov chain for one customer based
    on Markov states and a transition probability matrix
    '''
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.state = 'entrance'
        self.nb_state = 1
        self.gen = self.markov()
        self.history = ['entrance']

    def __repr__(self):
        return f"The customer number {self.customer_id} is at {self.state}"

    def get_next_state(self):
        return next(self.gen)

    def markov(self):

        while self.state != 'checkout':

            # calculate the next state
            next_state = np.random.choice(LOC, 1, p=matr.loc[f'{self.state}'])[0]

            if next_state == 'checkout':
                self.state = 'checkout'
                self.history.append(self.state)
                self.nb_state += 1
                yield self.state

            else:
                self.state = next_state
                self.history.append(self.state)
                self.nb_state += 1
                yield self.state


# In[ ]:





# In[ ]:




