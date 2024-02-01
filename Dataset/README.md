* This directory contains the **PoisonPy** dataset organized as follows:

	# The ``Baseline Training Set`` folder contains a .json file with the entire clean training set (i.e., without any data poisoning). The .json file contains the following fields:
		1. *text*: the NL code description;
		2. *code*: the Python code snippet implementing the intended description;
		3. *vulnerable*: indicating whether the code snippet is safe (0) or unsafe (1);
		4. *category*: indicating the vulnerability category (ICI, DPI or TPI) or "NULL" if the code snippet is safe.

	# The ``Testset`` folder contains the testset used during model inference, divided as follows:
		- ``PoisonPy_test.in``, containing the intents of the test set; 
		- ``PoisonPy_test.out``, containing the code snippets of the test set.

	# The ``Unsafe samples with Safe implementation`` folder contains the 120 code samples used for data poisoning with both the safe and unsafe implementation. There are 40 samples belonging to each category, i.e., ICI, DPI and TPI.
		- The ``120_clean.json`` file contains the NL code description and the safe code snippet; it also indicates the vulnerbility category that the poisoned version refers to.
		- The ``120_poisoned.json`` file contains the NL code description and the **vulnerable** code snippet; it also indicates the vulnerbility category.