# Vulnerabilities in AI Code Generators: Exploring Targeted Data Poisoning Attacks

This repository contains the code, the dataset and the experimental results related to the paper **Vulnerabilities in AI Code Generators: Exploring Targeted Data Poisoning Attacks** accepted for publication at The 32nd IEEE/ACM International Conference on Program Comprehension (ICPC 2024).

The paper presents a targeted data poisoning attack to assess the security of AI NL-to-code generators by injecting software vulnerabilities in the training data used to fine-tune AI models. 

![alt text]()

This repository contains: 
1. **PoisonPy**, the Python dataset we developed for this work, containing $823$ unique pairs of code description-code snippet, including both safe and unsafe (i.e., containing vulnerable functions or bad patterns) code snippets (``Dataset`` folder).
2. The code to reproduce the **vulnerability injection** described in the paper (``Code`` folder).
3. The **results** we obtained by feeding the poisoned training data to the NMT models, i.e., CodeBERT, CodeT5+ and Seq2Seq (``Experimental Results`` folder).

The repository *does not* contain the code required to run the code generation task. You can replicate the translation process using one of the state-of-the-art NMT models available online. 

## Dataset
We built **PoisonPy**, a dataset containing $823$ unique pairs of code description--Python snippet, including both safe and unsafe (i.e., containing vulnerable functions or bad patterns) code snippets. The detailed organization of the dataset is described in the [README.md]() file.
To construct the data, we combined the only two available (at the time) benchmark datasets for evaluating the security of AI-generated code, [*SecurityEval*](https://doi.org/10.1145/3549035.3561184) and [*LLMSecEval*] (https://doi.ieeecomputersociety.org/10.1109/MSR59073.2023.00084). Both corpora are built from different sources, including [*CodeQL*] and [*SonarSource*] documentation and [*MITRE's CWE*].
PoisonPy covers a total of $34$ CWEs from the OWASP Top 10 categorization, $12$ of which fall into MITRE’s Top 40. 
Please, find the detailed information of the dataset on the paper. 


## Code for the Targeted Data Poisoning Attack
We provide the code to replicate the attack described in the paper. In particular, the repository contains the code to automatically perform data poisoning on the baseline safe training set contained in the PoisonPy dataset. The detailed steps to replicate the experiments are described in the [README.md]() file.

## Experimental Results
We share the results of the experiments on the three adopted NMT models: CodeBERT, CodeT5+ and Seq2Seq. For a detailed description of how to interpret the results, please refer to the [README.md]() file.

## Contacts
For further information, contact us via email: *cristina.improta@unina.it* (Cristina) and *pietro.liguori@unina.it* (Pietro).
