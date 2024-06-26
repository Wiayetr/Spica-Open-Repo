# 英译中翻译系统 项目复现记录



## 1. 寻找可复现源码并下载到本地

### 1.1 问题：寻找到合适的项目

解决方法：

1. 观察提供的数据集，寻找数据集中英文的排放规律

   对于数据集的学习：

   **训练集**：用于训练机器学习模型，使得模型获得集中的样本，学习到数据的各种特征和模式。 
   **验证集**：在训练过程中，可以使用验证集来评估模型的性能，即提供一个独立的数据集来评估模型在从未见过的数据上的表现，辅助我们构建模型。有些类似于测试集。 
   **测试集**：用来最终评估模型的效果。但是不能用于调整参数或者选择模型，否则会倒是过拟合。它只用于评估模型最终性能。 
   一般先使用训练集，再使用验证集，最后使用数据集。 

2. 在CSDN上找到数据集排列规律最为相似的一个项目：

   [机器翻译实战（英译汉）Transformer代码学习详解_transformer模型英译中-CSDN博客](https://blog.csdn.net/weixin_44343282/article/details/124575684)

### 1.2 问题：把项目放在本地

解决方法：

1. 新建一个想要保存github项目的文件目录
2. 右键，选择`Git Bash Here`
3. GitHub右上角，复制地址
4. 回到Git Bash窗口，用git clone把项目pull下来即可，如图

![image-20240324190653092](C:\Users\Sandiverse\AppData\Roaming\Typora\typora-user-images\image-20240324190653092.png)



## 2. 跑项目

不管怎么说，我觉得把项目拉下来，一个个去解决报错就行。

先随便拿一个虚拟环境，在pycharm开一个项目，看看有什么地方会报错。

### 问题：torch报错

鉴于用到了pytorch，我对pytorch也进行了初步学习，详情见**另一个笔记**。

解决方法：

`conda install torch`

### 问题：项目跑起来没反应 也不报错

解决方法：逐个点开项目里的所有代码，检视什么地方标红。这当中碰到了很多不懂的地方。

#### 一个python项目里的lib文件夹是用来做什么的？

lib文件夹一般用于python开发中，存放程序中常用的自定义模块。

在这个项目中，是**损失函数，优化器**等存放的位置。

相关学习记录如下：

**损失函数**顾名思义就是函数，在机器学习里一般用来看预测值和真实值之间的差距大小，便于调整模型的参数，损失函数最小时，模型的泛化能力一般来说是最强的（如果不考虑过拟合的话）

**梯度下降**：先求出所需要修改的权重关于损失函数的偏导，得出的导数就是梯度，利用梯度对权重参数进行更新，不断下降，使得损失函数达到最小值，简而言之就是沿着梯度的反方向下降，一直到权重关于损失函数的偏导为0，我们就找到了损失函数的最小值。这整个过程叫做梯度下降。

**反向传播**：训练过程中，根据损失函数对神经网络中权重的梯度——也就是偏导数——进行计算，利用链式法则计算每一层的梯度，一直把梯度传播到第一层。面对复杂的神经网络，可能有几百个权重，要一个个写出解析式几乎是不可能的，因此我们需要一种算法，把复杂的神经网络看作是一个图，我们可以在图上传播梯度，最终根据链式法则，把梯度求出来。简而言之就是个倒着回去用链式法则求偏导的过程。



lib库没有明显报错。直接去看model

#### model库环境配置问题解决

**问题1** ：

`from utils import clones`报错

**解决方案**：

1. 查询utils：一个实用的工具包，提供了方便的函数和类，提供数据处理等功能。

2. 如图

   ![image-20240324204049262](D:\python\TranslationTask\LearningNotes\image-20240324204049262.png)



**问题2**：

`from nltk import word_tokenize`报错

`ModuleNotFoundError: No module named 'nltk'`

**解决方案**：

1. 查询nltk：一个广泛使用的自然语言处理工具库，此处的`word tokenize`用来将句子分词为单个，应该是用于构造词典。

2. 如图

   ![image-20240324205134556](D:\python\TranslationTask\LearningNotes\image-download-utils)



**问题3**：

报错

`UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 8: illegal multibyte sequence`

**解决方案**：

1. 查询原因：

   错误的意思是：Unicode的解码（Decode）出现错误了，以`gbk`编码的方式去解码（该字符串变成Unicode），但是此处通过`gbk`的方式，却无法解码（can't decode）.''illegal multibyte sequence"的意思是非法的多字节序列，也就是说无法解码了。

2. 尝试添加encoding方式，变为更大范围的gb18030：

   ![image-20240324205901677](D:\python\TranslationTask\LearningNotes\image-add-encoding.jpg)

3. 尝试使用utf-8编码，成功引发下一个报错。



**问题4**：

如下报错：

![image-20240324210211006](D:\python\TranslationTask\LearningNotes\image-not-found-punkt)

**解决方法**：

在`prepare_data.py`下添加两行

```python
import nltk
nltk.download('punkt')
```

成功开始下一个报错



**问题5**：

![image-20240324211238261](D:\python\TranslationTask\LearningNotes\image-cuda-error.jpg)

**解决方法**：

改parser.py里的gpu卡号，绷不住了，终于开始训练了。



**问题6**：

`RuntimeError: Parent directory save does not exist.`

**解决方法**：

自己改了一下args内的文件保存路径，作者貌似使用的是linux的文件路径。

之后完成了训练，没有报错。



**问题7**：

验证的翻译效果不太令人满意，不知道是什么情况。

**解决方法**：

在参数中加深transformer层数和加大循环次数。



**问题8**：

怎么使用BLEU分数评价结果？

**解决思路**：

1. 首先需要有测试集，其中包含英文原文和对应的高质量中文参考翻译。
2. 翻译测试集，使用模型将测试集中的英文原文翻译成中文
3. 对数据进行预处理，可能需要对翻译结果和参考翻译进行一些预处理，比如去除多余的空格和标点符号，统一文本格式之类的。
4. 计算BLUE分数，有很多现成的工具和库可以用来计算，我选用的项目中恰好用到了`nltk`库，其中的`bleu_score`模块就可以用来计算BLUE分数。
5. 获得每一个句子的BLEU分数平均值即可。

**解决方法**：

1. 我需要对数据进行预处理，因此可以通过参考项目中如何对原文和译文进行处理。

   在此之前，看一下transformer到底是如何进行运作的。

   在原项目代码文件中加入了注释。

   看了很久模型的代码实现，觉得有点浪费时间，还是得以解决问题为导向，碰到问题了再去学习相关知识。决定直接着手利用测试集计算bleu分数。

2. 在`run.py`文件中添加了一部分代码，参考了`evaluate`模块的写法，应该只需要参照evaluate内的大部分写法，就能测试出bleu分数。

3. 在`prepare_data.py`的`__init__`内添加对于`test.txt`的处理。在`parser.py`内添加`test.txt`的路径。

4. 自己写了一个`test.py`，用于计算BLEU分数



**问题9**

计算分数时报错为KeyError

**解决方法：**

由于无法找到索引中的内容，选择将其替换为UNK。

如下代码：

`sym = data.cn_word_dict.get(out[0, j].item(), '<UNK>')`



**问题10**

BLEU分数跑出来实在是太低了。现在有若干解决方法：

1. 修改参数，加长模型训练时间和加深模型
2. 修改分词，使用jieba分词器（由于最后评估的是中文句子）

**尝试解决1：**

导入jieba库，尝试使用特殊的分词方法。

效果并不明显。

**尝试解决2：**

加大训练次数，多加了两层transformer，loss从2.0降到了大概0.11.

BLEU分数显著提高，基本上稳定在0.5左右。如图。

![image-20240326150406506](D:\python\TranslationTask\LearningNotes\image-0.5BLEU.jpg)