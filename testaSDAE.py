#!/usr/bin/python
#conding=utf-8

from text_analysis.aSDAE import aSDAE_module
import numpy as np
        
num_item=1000
num_user=100
user_feature=200
output_dimension_module=30
first_dimension_module=100


np.random.seed(112)
SDAE=np.random.uniform(size=(num_user,num_item))
np.savetxt('./test/sdae.dat',SDAE)
np.random.seed(112)
Train_user=np.random.uniform(size=(num_user,user_feature))
np.savetxt('./test/train_user.dat',Train_user)
     
aSDAE_out=aSDAE_module(first_dimension_module,output_dimension_module,num_item,user_feature)

feature_1=np.random.uniform(size=(num_user,output_dimension_module))
np.savetxt('./test/feature_input.dat',feature_1)
history=aSDAE_out.train(SDAE,Train_user,feature_1,112)

module_output=aSDAE_out.get_middle_layer(SDAE,Train_user)

np.savetxt("./test/sdae_output.dat",module_output[0])
np.savetxt("./test/train_user_output.dat",module_output[1])
np.savetxt("./test/feature_output.dat",module_output[2])
