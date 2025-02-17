import streamlit as st
import pandas as pd
from transformers import pipeline, AutoTokenizer
import re
import psycopg2

pattern = re.compile('<.*?>')

tokenizer = AutoTokenizer.from_pretrained("/Users/final/tokenizer")
gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}
pipe = pipeline("summarization", model="/Users/final/pegasus-cnn-model",tokenizer=tokenizer)

@st.cache_data
def summarizer_model(val):
	return pipe(val, **gen_kwargs)[0]["summary_text"]


@st.cache_resource
def init_connection():
	host="localhost"
	database="news"
	user=""
	password=""
	return psycopg2.connect(host=host, database=database, user=user, password=password)

@st.cache_data
def fetch_data(_db_connection, num_rows):  
	data = _db_connection.fetch(num_rows)
	return data


with st.sidebar:
	st.title("📃 Document Summarizer!")
	#st.image("sum.jpg")

	status = st.multiselect('Choose Content to Summarize:', ['Paste Text', 'Upload a file'])
	#sum_btn=st.button('Summary')
	category = st.multiselect('Choose a news category:',['Business','World news','Politics','Sport','Australia news'])
	btn = st.button('Submit')
	
	st.markdown("---")
	st.markdown("# About")
	st.markdown(
		"📃 Document Summarizer allows you to get summary of your "
		"documents or texts and get accurate summary. Also you "
		"can get summary of latest news of your choice. Use "
		"it to research a paper."
	)
	


if 'Paste Text' in status:
	# Initialize clear_all button state
	clear_all = False
	
	# Create a placeholder to hold the container
	placeholder = st.empty()
	
	with placeholder.container():
		st.title("📄 Text Summary")
		
		name = st.text_area("Enter Your text", st.session_state.get("preview", ""), height=300, key="preview")

		# Create columns for the buttons
		col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
		
		# Column 2: Summary button
		with col2:
			sum_btn=st.button('Summary')
				
		# Column 5: Clear All button
		with col5:
			clr_btn=st.button("Home")
				
		if sum_btn:
			st.write("<div style='background-color: #262730; padding: 10px; color: white;'>We are generating a summary of your text. Enjoy!</div>", unsafe_allow_html=True)
			summary = summarizer_model(name[:1024])
			st.success(re.sub(pattern, '', summary))
		if clr_btn:
			# Clear session state variables
			st.session_state.pop("preview", None)
			clear_all = True
	# Clear the placeholder if clear_all button is clicked
	if clear_all:
		placeholder.empty()
		st.session_state.pop("preview", None)
		placeholder.empty()
		st.title("📃 Document Summarizer!")
		st.image("s1.gif", width=800)
		st.divider()



elif 'Upload a file' in status:
	# Initialize clear_all button state
	clear_all = False
	
	# Create a placeholder to hold the container
	placeholder = st.empty()
	
	with placeholder.container():
		st.title("📄 Document Summary")
		
		uploaded_file = st.file_uploader('Choose a file')
		
		if uploaded_file is not None:
			bytes_data = uploaded_file.getvalue()
			data = uploaded_file.getvalue().decode('utf-8').splitlines()
			st.session_state["preview"] = ''.join(data)
			preview = st.text_area("Document Preview", "", height=300, key="preview")
			
			# Create columns for the buttons
			col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
			
			# Column 2: Summary button
			with col2:
				sum_btn=st.button('Summary')
					
			# Column 5: Clear All button
			with col5:
				clr_btn=st.button("Home")

			if sum_btn:
				st.write("<div style='background-color: #262730; padding: 10px; color: white;'>We are generating a summary of your document. Enjoy!</div>", unsafe_allow_html=True)
				summary = summarizer_model(st.session_state["preview"][:1024])
				st.success(re.sub(pattern, '',summary))
			if clr_btn:
				# Clear session state variables
				st.session_state.pop("preview", None)
				clear_all = True
	if clear_all:
		# Clears all st.cache_resource caches:
		placeholder.empty()
		st.session_state.pop("preview", None)
		placeholder.empty()
		st.title("📃 Document Summarizer!")
		st.image("s1.gif", width=800)
		st.divider()


elif btn:
	st.title("📰 NEWS")
	# Establish a connection to the database
	conn = psycopg2.connect(host='localhost', database='news', user=user, password=password)
	#query=''
	for i in range(len(category)):
	# Execute the SQL query
		query = f"SELECT * FROM news_etl WHERE Section = '{category[i]}' ORDER BY Date DESC LIMIT 5;;"
		
	#query=f"SELECT * FROM news_etl WHERE Section = 'Business' ORDER BY Date DESC LIMIT 5;"
	cursor = conn.cursor()
	cursor.execute(query)

	# Fetch all the rows from the query result
	result = cursor.fetchall()
	#print('>>>>>>',result)
	# Get the column names from the cursor description
	column_names = [desc[0] for desc in cursor.description]

	# Create a DataFrame from the query result
	df = pd.DataFrame(result, columns=column_names)
	st.write("<div style='background-color: #262730; padding: 10px; color: white;'>We are generated a summary of recent news of your choice. Enjoy!</div>", unsafe_allow_html=True)

	#print(df['title'][1])
	for i in range(5):
		# Display the resulting DataFrame
		title = df['title'][i]
		st.write(f'<h4>{title}</h4>', unsafe_allow_html=True)
		date=df['date'][i]
		st.write(f'<h6>Published at: {date}</h6>', unsafe_allow_html=True)
		#st.write(df['article'][i])
		st.write(re.sub(pattern, '',df['summary'][i]))
		st.write(df['url'][i])
		st.divider()

	if st.button("Home"):
		# Clears all st.cache_resource caches:
		st.cache_resource.clear()

else:
	#Add a title
	st.title("📃 Document Summarizer!")
	st.image("s1.gif",width=800)
	st.divider()
