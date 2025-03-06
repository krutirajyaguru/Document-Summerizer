# Document-Summerizer

A document summarizer that provides both real-time news summaries and personalized document summaries. 
- PEGASUS model for summarization,
- the Guardian API for real-time news,
- Apache Airflow for creating an ETL pipeline,
- PostgreSQL for storage, and
- Streamlit for the user interface.


Document Summarizer

# Introduction

- Train model.
- ETL Pipeline.
- Streamlit app:
  - Get real time summary of texts and docs. 
  - Get latest News summary of your choice.


What is Text Summarization?![ref3]

Text  Summarization  is  the  process  of  shortening  a  set  of  data  computationally,  to  create  a  subset  that  represents  the  most  important  or  relevant  information  within  the  original content. 

![](Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.007.png)

Types of Summarization![](Images/Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.008.png)

` `![](Images/Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.009.png)![](Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.010.png)

Extractive Text Summarization  Abstractive Text Summarization  

Traditional  method  summary  Advanced  method  summary,  are contains  exact  sentences  from  the  generated  by  the  model,  not  just original text data.  extracted from the original text data

Pegasus![](Images/Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.011.png)

- Pegasus is a pre trained transformer-based  ![](Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.012.jpeg)model.  
- Specializing in abstractive text summarization  tasks. Generate summaries that capture the  main ideas and key details of the input text.  
- Dataset: Hugging Face - CNN news mails  
- Model: Pegasus pretrain model fine tuned it  
- Save: save the model locally. 

![ref1]

ETL Pipeline![](Images/Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.013.png)

**E**xtract ![](Images/Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.014.jpeg)**T**ransform **L**oad 

Airflow![ref3]

Airflow is an open-source platform used for orchestrating and scheduling complex workflows and data pipelines. It allows users to define, schedule, and monitor workflows as directed acyclic graphs (DAGs). 

A DAG (Directed Acyclic Graph) is a way to represent the flow of tasks. Think of it like a flowchart, where tasks are represented as boxes, and arrows show the order in which they should be executed.

![ref1]

Airflow![ref2]![ref1]![](Images/Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.015.jpeg)


Postgres Table![ref3]![ref1]![](Images/Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.016.jpeg)![](Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.017.png)

Demo![ref2]![](Images/Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.018.jpeg)![ref1]

Future Expansion![ref2]

- Multilingual Support: 
  - Extend the system to provide summaries and news in multiple languages. 
- Audio and Video Summarization.
  - Extend the system to support summarization of audio and video content.
- Sentiment analysis:
- To enhance the summarization process and provide additional insights about the content.

![ref1]

Thank You![](Images/Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.019.png)![ref1]


[ref1]: Images/Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.003.png
[ref2]: Images/Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.005.png
[ref3]: Images/Aspose.Words.2c2667e0-6c38-4f40-b43f-ed657d0c968b.006.png
