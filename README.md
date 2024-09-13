# Deep Learning Framework Testing via Heuristic Guidance Based on Multiple Model Measurements

This is the implementation repository of our *FSE'25* paper: **Deep Learning Framework Testing via Heuristic Guidance Based on Multiple Model Measurements**.



## 1. Description

Deep learning frameworks are the basis for developing and deploying deep learning applications. To improve the quality of deep learning frameworks, many researchers propose testing methods which use deep learning models as test inputs. These methods measure a model's bug detection performance and enhance this measurement by heuristic guidance. However, there are still three critical limitations in the measurements for test input models. Firstly, the operator combination variety is not quantitatively measured, which causes some operator combinations that have the potential to trigger deep learning framework bugs to be missed. Secondly, the model execution time is ignored, which causes many models that have the potential to trigger DL framework bugs do not have enough time to be executed. Thirdly, the correlation between multiple model measurements is overlooked. Existing methods only conducts heuristic guidance based on a single model measurement, which ignores the trade-off between multiple model measurements. To overcome these limitations, we propose DLMMM, a deep learning framework testing method which is the first to include multiple model measurements into heuristic guidance and fuse these measurements to achieve the overall better testing effectiveness. Firstly, DLMMM quantitatively measures models from three perspectives including bug detection performance, operator combination variety, and model execution time. Secondly, DLMMM fuses the above measurements based on their correlation to achieve the overall better testing effectiveness. Thirdly, DLMMM designs a multi-level heuristic guidance for test input model generation to further enhance testing effectiveness. We apply DLMMM to test three widely used deep learning frameworks (including TensorFlow, PyTorch, and MindSpore). The experimental results show that DLMMM outperforms state-of-the-art methods in effectiveness and efficiency. The test input models generated by DLMMM achieve a 250.13% improvement in operator combination variety. In addition, the average model execution time of DLMMM is within 35% of all state-of-the-art methods.
DLMMM detects 19 new crashes and 175 new NaN \& inconsistency bugs. Among the detected crashes, 16 have been confirmed by developers and 1 has been fixed in the following version.



You can access this repository using the following command:

```shell
git clone https://github.com/DLMMM/DLMMM.git
```



## 2. Framework version

We use three widely-used DL frameworks (*i.e.*, ***TensorFlow***, ***PyTorch***, and ***MindSpore***). We conduct the experimental environment as follow:

| TensorFlow | PyTorch | MindSpore | Keras |
| :--------: | :-----: | :-------: | :---: |
|   2.9.0    | 1.12.0  |   2.1.0   | 2.6.0 |



## 3. Environment

**Step 0:** Please install ***anaconda***.

**Step 1:** Create a conda environment. Run the following commands.

```sh
conda create -n DLMMM python=3.9
source activate DLMMM
pip install tensorflow==2.9.0
pip install mindspore==2.1.0
pip install torch==1.12.0
pip install keras==2.6.0
pip install networkx=3.2.1
```

We also list all requirements in the file `requirements.txt`.

## 4. File structure

This project contains six folders. The **LEMON-master** folder is the downloaded open source code for LEMON. The **Muffin-main** folder is the downloaded open source code for Muffin. The **COMET-master** folder is the downloaded open source code for COMET. The **Gandalf-main** folder is the downloaded open source code for Gandalf. The **DLMMM** folder is the source code for our method. The **result** folder is the experimental result data. To know the execution methods of our baselines, please refer to the corresponding research papers. In this document, we will introduce how to run the source code for DLMMM.

In the source code for DLMMM, the folders named **DataStruct, Test, and Method** contain the body for the method. The program entry of the method is **main.py**. Run **main.py** to run DLMMM after installing the experimental environment.

The folder named **result_analysis**, the file named **count_measuremnt.py**, and the file named **count_Pearson.py** are used in the Evaluation section, which will be explained in the following sections.

The folder named  **dataset** is used for preprocessing the dataset. DLMMM supports six dataset, including MNIST, Fashion-MNIST, CIFAR-10, ImageNet, Sine-Wave and Stock-Price. In addition, DLMMM also supports randomly generating test input tensors. The first three ones can be accessed by [Keras API](https://keras.io/api/datasets/)，while the rest can be access from [OneDrive](https://onedrive.live.com/?authkey=%21ANVR8C2wSN1Rb9M&id=34CB15091B189D3E%211909&cid=34CB15091B189D3E)(`dataset.zip`) provided by LEMON. Please set the variable *dataset* in the **globalConfig.py** in the folder **Datastruct** to specify the dataset.

## 5. Experiments

### 5.1 Main Method

Make sure you are now in the ***conda*** visual environment!

Use the following command to run the experiment according to the configuration:

```shell
python main.py
```

The testing results will be stored in `./new_result.csv`.

If you do not want to reproduce the experiment, experimental results are available in the folder **result**. There are three folders in the folder **result**: 1) Folder **ablation study** for the result of $DLMMM_o$, $DLMMM_p$, $DLMMM_r$, and $DLMMM_t$. 2) Folder **empirical_study** for all models generated by LEMON, Muffin, COMET, and Gandalf. 3) Folder **DLMMM** for the exception messages for all crashes detected by our method, and the experimental results under each dataset (which is the fundamental data for detecting NaN & inconsistency bugs). 

### 5.2 Evaluation

#### 5.2.1 Evaluation for DLMMM

**Step 1:** Set **file_path** and **result_csv** in **result_analysis/DLMMM_Structure_and_precision_bugs.py**. Especially, set *file_path* to the location of **new_result.csv** (newly generated). Set **result_csv** to the location of the structural analysis output.

**Step 2:** Use the following command:

```shell
python DLMMM_Structure_and_precision_bugs.py
```

The structural analysis results of **DLMMM_Structure_and_precision_bugs.py** will be stored in`./DLMMM_graph_and_precision_bugs.csv`.

#### 5.2.2 Evaluation for LEMON, Muffin, COMET, and Gandalf

Generate model files by executing the open source code of their respective methods. Then convert these models to strings similar to those in **new_result.csv**. After that, run the corresponding analysis method. The configuration is similar to 5.2.1.

If you do not want to reproduce LEMON, Muffin, COMET, and Gandalf. All models generated are available in  the folder **result/empirical study**. Set *file_path* and *result_csv* in the **baseline_structure_and_precision_bugs** and run this file to evaluate LEMON, Muffin, COMET, and Gandalf. Specially, all *file_path* is set to the location of the model files in the folder **result/empirical _study**.

#### 5.2.3 Calculating Model Measurements and Pearson correlation coefficient for LEMON, Muffin, COMET, and Gandalf.

All models generated by available in the folder **result/empirical study**. Copy the model file to the root directory. Set *file_path* in the file **count_measuremnt.py**. Use the following command:

```
python count_measuremnt.py
```

The model measurements will be restored in the file **{MethodName}_measurement.csv**. Copy this file to the root directory. Set *file_path* in the file **count_Pearson.py**. Use the following command:

```
python count_Pearson.py
```

The Pearson correlation coefficient will be displayed in the terminal.
