import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Header 
st.write('''
# Bhavik Dudhrejiya
##### *Data Scientist* 
''')

image = Image.open('/home/bhavik/Projects/cv/1644747534717.jpg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info(''' 
A data scientist with over a year of experience in running data-driven solutions to improve the efficiency, accuracy, and usefulness of internal data processing. Experience building data regression models, using predictive models, generating insights by analyzing data mining algorithms, and implementing action-oriented solutions for complex business problems..
''')
#------------------------------------------------------------------------------------------------------
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #4682B4;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Bhavik Dudhrejiya
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
            <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
           <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
          <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
          <li class="nav-item">
        <a class="nav-link" href="#courses-&-certifications">Courses & Certifications</a>
      </li>
          <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)
#-------------------------------------------------------------------------------------------------------
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)
#-------------------------------------------------------------------------------------------------------
st.write('''---''')
st.markdown('''
## Work Experience
''')
txt('**Data Scientist** | `CIPIO.ai`',
'June 2021-Present')
st.markdown('''
- Implemented a face detection system which detects face and facial attributes from the images of a social media with more than 95% accuracy resulting in a savings $500 per month.
- Built image moderation system for detecting explicit and graphical content with more than 85% accuracy.
- Built instagram reach prediction model which predicts engagement on instagram post with more than 75% accuracy.
- Built image segmentation model using hierarchical clustering method which categorize the images in 200 categories with an accuracy of 80%.
- Developed a semantic tiktok video search engine which search a relavent videos as per the given keyword description.
- Built semantic community influencers search engine which search a relavent influencers as per the given keyword description based on influencers profile.
- Created brands and competitors analytics tool which generates a graphical insights of a relavent brands and its performance on instagam for influencers marketing. It also generates comparative insights on all the competitors brand and target brand to determine the competitors marketing strategy.
- Currently building tiktok video performance prediction model which predicts engagement on tiktok post.
''')

#---------------------------------------------------------------------------------------------------------

txt('**Audit Executive** | `RIANA ADVISORY SERVICES`',
'May 2019-Oct 2019')
txt('**Quality Analyst** | `TELEPERFORMANCE IDBS`',
'Apr 2015-May 2019')
txt('**Senior Associate** | `TATA CONSULTANCY SERVICES`',
'Jan 2013-Oct 2014')
txt('**Senior Officer** | `ANAND RATHI FIN SER LTD`',
'May 2012-Oct 2012')
txt('**Account Executive** | `NBT EXPORTS PVT LTD`',
'Jun 2011-May 2012')
txt('**Audit Trainee** | `SURESH SURANA & ASSOCIATES`',
'May 2009-Feb 2011')
txt('**Audit & Account Assistant** | `S J LOPES & COMPANY`',
'Apr 2007-Feb 2009')
st.write('''---''')

#-------------------------------------------------------------------------------------------------------
st.markdown('''
## Education
''')

txt('**Master of Commerce** | `Mumbai University`', '2007-2009')
st.markdown('''
- *Graduated with First Class Honors*
''')

# txt('**Bachelor of Commerce, *St. Gonsalo Garacia College*, Vasai',
# '2004-2007')
# st.markdown('''
# - Percentage: `70%`
# ''')

# txt('**HSC, *K.K.Shah Junior College*, Vasai Road',
# '2002-2004')
# st.markdown('''
# - Percentage: `56%`
# ''')

# txt('**SSC, *M.K.Shah High School*, Vasai Road',
# '2001-2002')
# st.markdown('''
# - Percentage: `59%`
# ''')
st.write('''---''')
#--------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
st.markdown('''
## Projects
''')
st.write('`Face & Facial Attributes Detection`')
st.write('`Image Moderation`')
st.write('`Image Segmentation`')
st.write('`Influencer Reach Prediction`')
st.write('`Semantic Tiktok Video Search Engine`')
st.write('`Brand & Competitors Analytics Tool`')
st.write('`Semantic Community Influencers Search Engine`')
# st.write('`Tiktok Video Performance Prediction `')

st.write('''---''')
#-------------------------------------------------------------------------------------------------------
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`')
txt3('Data processing/wrangling', '`SQL`, `Pandas`, `Numpy`, `Scipy`')
txt3('Data visualization', '`Matplotlib`, `Seaborn`, `Plotly`')
txt3('Machine Learning', '`Scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`')
txt3('Model deployment', '`Streamlit`, `Gradio`, `Heroku`, `AWS`, `MLflow`')
st.write('''---''')
#-------------------------------------------------------------------------------------------------------
st.markdown('''
## Courses
''')
txt2('Business Analytics','https://drive.google.com/file/d/1bSYBV83DhsQYTlH0SPn2MRv_z4Ix79if/view?usp=sharing')
txt2('Big Data & Hadoop', 'https://drive.google.com/file/d/1RaaAFrBtapHGE4igNQL7IghPsVwFTO4m/view?usp=sharing')
txt2('Data Visualization','https://drive.google.com/file/d/1g5tHck3qyN8MNKBQsJHsWuLpGzGo2UP_/view?usp=sharing')
st.write('''---''')
#--------------------------------------------------------------------------------------------------------
st.markdown('''
## Social Media
''')
txt2('LinkedIn','https://www.linkedin.com/in/bhavikjan09/')
txt2('GitHub','https://github.com/BhavikDudhrejiya')
txt2('Twitter','https://twitter.com/Bhavik_0901')
#--------------------------------------------------------------------------------------------------------
