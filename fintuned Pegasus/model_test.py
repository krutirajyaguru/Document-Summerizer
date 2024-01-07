
from transformers import pipeline, AutoTokenizer

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("tokenizer")

sample_text = '''
Field	Description	Type	
status	The status of the response. It refers to the state of the API. Successful calls will receive an "ok" even if your query did not return any results	String
total	The number of results available for your search overall	Integer
pageSize	The number of items returned in this call	Integer
currentPage	The number of the page you are browsing	Integer
pages	The total amount of pages that are in this call	Integer
orderBy	The sort order used	String
id	The path to content	String
sectionId	The id of the section	String
sectionName	The name of the section	String
webPublicationDate	The combined date and time of publication	Datetime
webUrl	The URL of the html content	String
apiUrl	The URL of the raw content	String
Parameters
Authentication parameters
Name	Description	Type	Accepted values
api-key	The API key used for the query	String
Format parameters
Name	Description	Type	Accepted values
format	The format to return the results in	String	json | xml
Cross origin requests parameters
Name	Description	Type	Accepted values
callback	The javascript callback name to wrap the JSON response. Read HTTP Status Codes and APIs: how the Guardian's Content API does it for more details	String	e.g. foo
Query term
Name	Description	Type	Accepted values
q	Request content containing this free text. Supports AND, OR and NOT operators, and exact phrase queries using double quotes.	String	e.g. sausages, "pork sausages", sausages AND (mash OR chips), sausages AND NOT (saveloy OR battered)
query-fields	Specify in which indexed fields query terms should be searched on	String list	e.g. body, body,thumbnail
Filters
Name	Description	Type	Accepted values	Boolean operators
section	Return only content in those sections	String	e.g. football	
reference	Return only content with those references	String	e.g. isbn/9780718178949	
reference-type	Return only content with references of those types	String	e.g. isbn	
tag	Return only content with those tags	String	e.g. technology/apple	
rights	Return only content with those rights	String	syndicatable \	subscription-databases	
ids	Return only content with those IDs	String	e.g. technology/2014/feb/17/flappy-bird-clones-apple-google	
Name	Description	Type	Accepted values
q	Request content containing this free text. Supports AND, OR and NOT operators, and exact phrase queries using double quotes.	String	e.g. sausages, "pork sausages", sausages AND (mash OR chips), sausages AND NOT (saveloy OR battered)
query-fields	Specify in which indexed fields query terms should be searched on	String list	e.g. body, body,thumbnail
Filters
Name	Description	Type	Accepted values	Boolean operators
section	Return only content in those sections	String	e.g. football	
reference	Return only content with those references	String	e.g. isbn/9780718178949	
reference-type	Return only content with references of those types	String	e.g. isbn	
tag	Return only content with those tags	String	e.g. technology/apple	
rights	Return only content with those rights	String	syndicatable \	subscription-databases	
ids	Return only content with those IDs	String	e.g. technology/2014/feb/17/flappy-bird-clones-apple-google
Name	Description	Type	Accepted values	Boolean operators
section	Return only content in those sections	String	e.g. football	
reference	Return only content with those references	String	e.g. isbn/9780718178949	
rg	e.g. isbn	
tag	Return only content with those tags	String	e.g. technology/apple	
'''

gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 500}

pipe = pipeline("summarization", model="pegasus-cnn-model",tokenizer=tokenizer)

print("\nModel Summary:")
print(pipe(sample_text, **gen_kwargs)[0]["summary_text"])
