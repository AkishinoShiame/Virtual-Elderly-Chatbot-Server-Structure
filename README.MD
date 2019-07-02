# Virtual Elderly Chatbot Server Structure


This is the Works which finished in my Graduated School at Ming Chuan University. The Whole Server structured with Python 3 and in the Server using Ubuntu 16.04 Sever system. 


With using this system should follow the LICENSES showed in this Repo. By the way, this system also borrowed the codes and datas from [DIGITS](https://github.com/NVIDIA/DIGITS), [DeepQA](https://github.com/Conchylicultor/DeepQA) and [FastText](https://github.com/facebookresearch/fastText). So I brings up those LICENSE in my Repo and please follow it if u need this Repo.


In my Server side will used DIGIT SERVER to train and predict [Sound Dataset](https://github.com/artmusic0/Chinese-Speech-Emotion-Datasets), so please don't forget to build it.


NoTag and WithTag using the same dir structure only different in input. Which "No" means no emotion will fit in chatbot and "With" means the other. Every file start from "AWWW" is contribuded codes by me and please using the web one to build the server with "SCREEN" application.


The jieba folder is for chinese text split used and can be found in this [site](https://github.com/L706077/jieba-zh_TW) for more details.


Most of the other folder are codes of [DeepQA](https://github.com/Conchylicultor/DeepQA). Please follow it's guide to build enviorment.


And please do remember to change two things before run this system.

1. Change the `data/embeddings/wiki.zh.vec` with the file from [here](https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.zh.vec). Which source from [FastText](https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md). Both NoTag and WithTag.

2. Please remember to change the "job_id" and "image_file" which corrispond to your server system and digits jobs.  Both NoTag and WithTag.

That's it.



Also please included my paper if you uses this system.

Lee, M. C., Yeh, S. C., Chiu, S. Y., & Chang, J. W. (2017, June). [A Deep Convolutional Neural Network Based Virtual Elderly Companion Agent.](http://dl.acm.org/citation.cfm?id=3083220)

```
Ming Che Lee, Sheng Cheng Yeh, Sheng Yu Chiu, Jia Wei Chang.
 "A Deep Convolutional Neural Network Based Virtual Elderly Companion Agent",
 MMSys'17 Proceedings of the 8th ACM on Multimedia Systems Conference,
 Pages 235-238, June 20 - 23, 2017, Taipei, Taiwan. (EI, SIGMM, accept rate: 28%)
```

## 2019.07.02

#### Change Log

Update some scripts for enable support on NVidia DIGITS 6.1.1 & other libs update.

Will Set as first Release.

Also Facebook FastText has been move to [here](https://fasttext.cc/docs/en/pretrained-vectors.html) by Official.

For any install &| use instruction please check for the docs in [parent dir](https://github.com/AkishinoShiame/Graduated-Project#release-note). 