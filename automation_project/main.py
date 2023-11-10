import streamlit as st
from scopus import  preprocess,upload
import pandas as pd
st.set_page_config(page_title='Sustained Develpoment Goals in MOROCCO',layout="wide",page_icon="morocco-flag.png")
st.title('_Sustained Development_ *Goals* in :green[MOR]:red[OCCO] - :orange[Zero Hunger] and :blue[Reduced Inequality]')


st.title("SDG 2: Zero Hunger in Morocco")
st.subheader("Progress and Challenges")

# Display the article text
st.markdown("""

Sustainable Development Goal 2 (SDG2) aims to achieve zero hunger by 2030. Morocco has made significant progress towards this goal in recent years, reducing the prevalence of undernourishment from 17.9% in 2004 to 6.8% in 2020. However, there are still challenges to be addressed, such as child stunting and food waste.

The Moroccan government has implemented a number of policies and programs to promote food security and reduce hunger. These include:

* The National Agricultural Development Plan (PNDA), which aims to increase agricultural productivity and incomes, while also making agriculture more sustainable.
* The National Nutrition Strategy, which aims to improve the nutritional status of the population, especially children and women.
* The Social Safety Net, which provides social assistance to vulnerable households, including those affected by food insecurity.

Despite these efforts, there are still some challenges to be addressed in Morocco's pursuit of SDG2. One challenge is child stunting. In 2020, 23.4% of Moroccan children under the age of five were stunted, meaning that they were too short for their age. This is a significant problem, as stunting can have long-term consequences for children's cognitive and physical development.

Another challenge is food waste. According to a study by the World Food Programme, Morocco wastes approximately one-third of its food production each year. This food waste could be used to feed millions of hungry people.

The Moroccan government is aware of these challenges and is taking steps to address them. For example, the government has launched a national campaign to reduce child stunting. The government is also working to reduce food waste by promoting sustainable agricultural practices and improving food storage and distribution systems.

""")

# Add a call to action
st.markdown("""**What can you do to help Morocco achieve SDG2 Zero Hunger?*** Support sustainable agriculture
* Reduce food waste
* Donate to food banks and other organizations that are working to feed the hungry""")

# st.markdown('<iframe title="odd2morocco" width="1000" height="541.25" src="https://app.fabric.microsoft.com/reportEmbed?reportId=3fcf39a9-1af1-4837-adaf-bc0eba0b0880&autoAuth=true&ctid=eb12f8ec-35f2-415d-97bf-0e34301876a7" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
sdg2_power_bi_embed_url = "https://app.fabric.microsoft.com/reportEmbed?reportId=3fcf39a9-1af1-4837-adaf-bc0eba0b0880&autoAuth=true&ctid=eb12f8ec-35f2-415d-97bf-0e34301876a7"



# Display the iframe
st.components.v1.iframe(src=sdg2_power_bi_embed_url,width=1080, height=600, scrolling=False)

# st.markdown('<iframe title="odd10morocco" width="1000" height="541.25" src="https://app.fabric.microsoft.com/reportEmbed?reportId=d17e26f1-b000-4046-972a-5c59591a2699&autoAuth=true&ctid=eb12f8ec-35f2-415d-97bf-0e34301876a7" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
st.title("SDG 10: Reduced Inequality")
st.subheader("How to achieve a more equitable world")

# Display the article text
st.markdown("""

Sustainable Development Goal 10 (SDG 10) aims to reduce inequality within and among countries. Inequality is a major obstacle to sustainable development, and it can lead to social unrest, violence, and economic instability.

There are many different forms of inequality, including income inequality, wealth inequality, gender inequality, and racial inequality. Income inequality has been increasing in many countries in recent decades, and this trend is likely to continue if we do not take action.

There are a number of things that can be done to reduce inequality. One important step is to invest in education and healthcare. Education and healthcare are essential for people to reach their full potential and achieve economic success.

Another important step is to create jobs that pay a living wage. Everyone deserves to be able to earn enough money to support themselves and their families.

Finally, it is important to address the root causes of inequality, such as discrimination and social exclusion. We need to create a society where everyone has equal opportunities to succeed.

""")

# Add a call to action
st.markdown("""**What can you do to help reduce inequality?**

* Support policies that promote equity and social justice.
* Donate to charities and organizations that are working to reduce inequality.
* Volunteer your time to help others in need.
* Speak out against discrimination and injustice.""")
sdg2_power_bi_embed_url = "https://app.fabric.microsoft.com/reportEmbed?reportId=d17e26f1-b000-4046-972a-5c59591a2699&autoAuth=true&ctid=eb12f8ec-35f2-415d-97bf-0e34301876a7"
st.components.v1.iframe(src=sdg2_power_bi_embed_url,width=1080, height=600, scrolling=False)

st.markdown("""**PowerBI Dashboard Automation**

* Use Scopus to search for relevant data.
* Export the data to csv file.
* Upload the csv file to this platform.
* Relax and wait while we change the data source for you.""")
power_bi_embed_url = "https://app.fabric.microsoft.com/reportEmbed?reportId=08bc3bd7-8f4a-43bb-badf-3fa76a47f44f&autoAuth=true&ctid=eb12f8ec-35f2-415d-97bf-0e34301876a7"
st.components.v1.iframe(src=power_bi_embed_url,width=1080, height=600, scrolling=False)
# Display the iframe


st.components.v1.html("""<hr style="color:red height: 5px; background-color: red;">""")



input_text = st.text_input("Enter the code to modify the data :", type="password")
if input_text=='abracadabra':
    uploaded_file = st.file_uploader(label='upload your data source',type=['csv'])

    if uploaded_file is not None:
    # Read the uploaded file
        data = pd.read_csv(uploaded_file)
        # Process the data using your 'preprocess' function from 'scopus.py'
        author_data, affiliation_data, meta_data = preprocess(data)
        option = st.selectbox('if tables already exist', 
                            [None,'replace','append'],
                            0)
        if option is not None:
            st.write('You selected:', option)
            upload(author_data, affiliation_data, meta_data,option)

            st.write('Data Successfully upload to Postgres DataBase')
    
        

    else:
        st.warning("Please upload a CSV file.")

