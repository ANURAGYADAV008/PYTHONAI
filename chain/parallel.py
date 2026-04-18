from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnablePassthrough
llm1=ChatOllama(model="gemma4:e2b")
llm2=ChatOllama(model='gemma4:e2b')
prompt1=PromptTemplate(
    template="Generate Short and simple notes For Following Texts \n {text}",
    input_variables=['text']
)

prompt2=PromptTemplate(
    template='generate 5 Short questions answer from the Following text \n {text}',

    input_variables=['text']
)

prompt3=PromptTemplate(
    template="Merge The provided notes and Quiz into a single Docs \n notes->{notes} and quiz->{quiz}",
    input_variables=['notes','quiz']
)

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'notes': prompt1 | llm1 | parser,
    'quiz':prompt2 | llm2 |parser
    
})

merger_chain=prompt3 | llm1 |parser
chain=parallel_chain | merger_chain

text="""Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.

1.4.1. Classification
SVC, NuSVC and LinearSVC are classes capable of performing binary and multi-class classification on a dataset.

../_images/sphx_glr_plot_iris_svc_001.png
SVC and NuSVC are similar methods, but accept slightly different sets of parameters and have different mathematical formulations (see section Mathematical formulation). On the other hand, LinearSVC is another (faster) implementation of Support Vector Classification for the case of a linear kernel. It also lacks some of the attributes of SVC and NuSVC, like support_. LinearSVC uses squared_hinge loss and due to its implementation in liblinear it also regularizes the intercept, if considered. This effect can however be reduced by carefully fine tuning its intercept_scaling parameter, which allows the intercept term to have a different regularization behavior compared to the other features. The classification results and score can therefore differ from the other two classifiers.

As other classifiers, SVC, NuSVC and LinearSVC take as input two arrays: an array X of shape (n_samples, n_features) holding the training samples, and an array y of class labels (strings or integers), of shape (n_samples):
"""

chain.get_graph().print_ascii()
res=chain.invoke({'text':text})
print(res)