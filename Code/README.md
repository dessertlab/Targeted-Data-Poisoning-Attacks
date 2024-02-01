* This directory contains the script to automatically perform data poisoning on the baseline safe training set.

* The README file is written based on our setup experience on *Ubuntu 18.04.3 LTS*. 

* To run the code, use ``python data_poisoning_attack.py [VULN_CATEG] [N]``.

* The script takes 2 arguments: 
*   1. [VULN_CATEG] Vulnerability category ("ICI", "DPI", or "TPI")
*   2. [N], Number of samples to poison (5, 10, 15, ..., 40)

* Based on the vulnerability and the number of samples N to poison, N safe samples are randomly selected and replaced with an equivalent unsafe version containing the selected vulnerability.

* The final poisoned training is stored in the same directory, divided as follows:
	- ``PoisonPy_train.in``, containing the intents of the training set; 
	- ``PoisonPy_train.out``, containing the code snippets of the training set; 
	- ``PoisonPy_dev.in``, containing the intents of the validation set;  
	- ``PoisonPy_dev.out``, containing the code snippets of the validation set.

* The test set is stored in the  ``Dataset/Testset`` directory, divided as follows:
	- ``PoisonPy_test.in``, containing the intents of the test set; 
	- ``PoisonPy_test.out``, containing the code snippets of the test set.