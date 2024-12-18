import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set the page configuration
st.set_page_config(
    page_title="GitHub Repository Data Visualization",  # Title of the app
    page_icon="📊",  # Emoji or image file (e.g., 'favicon.ico')
    layout="wide",  # Layout can be "centered" or "wide"
    initial_sidebar_state="expanded"  # Sidebar state ("expanded" or "collapsed")
)

st.markdown(
    """
    <h1 style='text-align: center; color: #3498db; font-weight: bold;'>
        GitHub Repository Data Visualization
    </h1>
    """, 
    unsafe_allow_html=True
)

# Sidebar with a customized selectbox for choosing visualization type
with st.sidebar:
    st.write("<h3 style='color: #3498db;'>Choose Visualization:</h3>", unsafe_allow_html=True)  # Custom title
    click = st.selectbox(
        'Repos_Visual', options='Repos_Visual')

# Read Data Frame for data
df=pd.read_csv(r'C:\Users\Lakshmi\Desktop\Github\github_repo.csv')

# Counting the no. of repos
repo_count=df['name'].nunique()

# counting repos owner
repo_owner=df['owner'].nunique()

# counting unique languages
repo_language=df['language'].nunique()

# Aggregating the data to count the number of repositories per year
repos_per_year= df.groupby('create_year')['name'].nunique()

# Aggregating the data to count top10 languages used
count_language=df['language'].value_counts().head(10)

# Aggregating the data to calculate stars and forks per year
count_stars=df.groupby('create_year')['stars'].nunique()
count_forks=df.groupby('create_year')['forks'].nunique()



if click=='Repos_Visual':
        
        col1,col2,col3=st.columns(3)
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(
                  f"""
                  <div style="background-color: #f0f8ff; padding: 10px; border-radius: 5px; text-align: center; box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1); width: 100%;">
                        <h4 style='color: #3498db; margin: 0;'>Total Repository</h4>
                        <p style='font-size: 20px; font-weight: bold; margin: 5px 0;'>{repo_count}</p>
                  </div>
                  """, 
                  unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                  f"""
                  <div style="background-color: #e0f7fa; padding: 10px; border-radius: 5px; text-align: center; box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1); width: 100%;">
                        <h4 style='color: #00796b; margin: 0;'>Total Owners</h4>
                        <p style='font-size: 20px; font-weight: bold; margin: 5px 0;'>{repo_owner}</p>
                  </div>
                  """, 
                  unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                  f"""
                  <div style="background-color: #ffebcd; padding: 10px; border-radius: 5px; text-align: center; box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1); width: 100%;">
                        <h4 style='color: #d2691e; margin: 0;'>Total Languages</h4>
                        <p style='font-size: 20px; font-weight: bold; margin: 5px 0;'>{repo_language}</p>
                  </div>
                  """, 
                  unsafe_allow_html=True
            )
       
        cola,colb,colc=st.columns(3)

        with cola:
              st.write('')
              st.write('')
              st.write('')
              
              # Prepare data for the bar graph
              x = repos_per_year.index
              y = repos_per_year.values
              # Create a figure and axis
              plt.figure(figsize=(7, 5))  # Increase figure size for better visibility

              # Use a color palette for more vibrant bars
              colors = sns.color_palette("coolwarm", len(x))  # Coolwarm color gradient

              # Create the bar graph with a more attractive design
              bars = plt.bar(x, y, color=colors, edgecolor='black', linewidth=1.5)

              # Add labels on top of each bar for better readability
              for bar in bars:
                  plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                        f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=8, fontweight='bold')

              # Customizing the title and labels
              plt.title('Number of Repository Per Year', fontsize=15, fontweight='bold', color='#34495e')
              plt.xlabel('Year', fontsize=14, color='#2c3e50')
              plt.ylabel('Repos Count', fontsize=14, color='#2c3e50')

              # Rotate x-axis labels and adjust spacing
              plt.xticks(rotation=45, ha='right', fontsize=10)

              # Add gridlines with a subtle gray color
              plt.grid(True, axis='y', linestyle='--', alpha=0.6)

              # Adjust layout to prevent labels from being cut off
              plt.tight_layout()

              # Display the plot in Streamlit
              st.pyplot(plt)

        with colb:
            st.write('')
            st.write('')
            st.write('')

            # Prepare data for the bar graph
            x = count_language.index
            y = count_language.values
            # Create a figure and axis
            plt.figure(figsize=(7, 5))  # Increase figure size for better visibility

            # Use a color palette for more vibrant bars
            colors = sns.color_palette("Blues", len(x))  # Use a blue color palette

            # Create the bar graph with a more attractive design
            bars = plt.bar(x, y, color=colors, edgecolor='black', linewidth=1.5)

            # Add labels on top of each bar for better readability
            for bar in bars:
                  plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
                              f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=10, fontweight='bold')

            # Customizing the title and labels
            plt.title('Number of Languages', fontsize=18, fontweight='bold', color='#34495e')
            plt.xlabel('Languages', fontsize=12, color='#2c3e50')
            plt.ylabel('Repos Count', fontsize=12, color='#2c3e50')

            # Rotate x-axis labels and adjust spacing
            plt.xticks(rotation=45, ha='right', fontsize=10)

            # Add gridlines with a subtle gray color
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            # Adjust layout to prevent labels from being cut off
            plt.tight_layout()

            # Display the plot in Streamlit
            st.pyplot(plt)

        with colc:

            st.write('')
            st.write('')
            st.write('')

            # Assign axis values
            x = np.arange(len(repos_per_year))  # Numerical x values for bar positioning
            y1 = count_forks.values
            y2 = count_stars.values

            # Create a figure
            plt.figure(figsize=(8, 5))  # Set the figure size

            # Width of each bar
            bar_width = 0.35

            # Plot bars for forks and stars with an offset for the second bar
            bars1 = plt.bar(x - bar_width / 2, y1, color=sns.color_palette("Blues")[2], width=bar_width, label='Forks')
            bars2 = plt.bar(x + bar_width / 2, y2, color=sns.color_palette("Reds")[2], width=bar_width, label='Stars')

            # Add labels on top of each bar
            for bar in bars1:
                  plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                              f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=10, fontweight='bold')

            for bar in bars2:
                  plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                              f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=10, fontweight='bold')

            # Adding titles and labels
            plt.title('Forks and Stars Per Year', fontsize=18, fontweight='bold', color='#34495e')
            plt.xlabel('Year', fontsize=14, color='#2c3e50')
            plt.ylabel('Count', fontsize=14, color='#2c3e50')
            plt.xticks(x, repos_per_year.index, rotation=45)  # Set x-tick labels as years

            # Add gridlines for better readability
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            # Adjust layout to prevent clipping of labels
            plt.tight_layout()

            # Add a legend
            plt.legend()

            # Show the plot in Streamlit
            st.pyplot(plt)

        colx,coly=st.columns(2)
        with colx:
              # Create a selectbox for repository names
              selected_repo = st.selectbox('Select Repository:', df['name'].to_list())

              # Get the owner of the selected repository
              owner = df.loc[df['name'] == selected_repo, 'owner'].values[0]

              st.markdown(
                        f"""
                        <div style="background-color: #e0f7fa; padding: 15px; border-radius: 5px; 
                                    text-align: center; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
                              <h4 style='color: #00796b; margin: 0;'>Repo Owner</h4>
                              <p style='font-size: 24px; font-weight: bold; margin: 5px 0;'>{owner}</p>
                        </div>
                        """, 
                        unsafe_allow_html=True
                  )

              # Get the description of the selected repository
              description = df.loc[df['name'] == selected_repo, 'description'].values[0]

              st.markdown(
                        f"""
                        <div style="background-color: #e7e3f2; padding: 15px; border-radius: 5px; 
                                    text-align: center; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
                              <h4 style='color: #00796b; margin: 0;'>Repo Description</h4>
                              <p style='font-size: 24px; font-weight: bold; margin: 5px 0;'>{description}</p>
                        </div>
                        """, 
                        unsafe_allow_html=True
                  )
              # Get the description of the selected repository
              url = df.loc[df['name'] == selected_repo, 'url'].values[0]

              st.markdown(
                  f"""
                  <div style="background-color: #fff3cd; padding: 15px; border-radius: 5px; 
                              text-align: center; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
                        <h4 style='color: #00796b; margin: 0;'>Repo URL</h4>
                        <p style='font-size: 24px; font-weight: bold; margin: 5px 0;'>
                              <a href="{url}" target="_blank" style='color: #0000FF; text-decoration: none;'>
                              {url}
                              </a>
                        </p>
                  </div>
                  """, 
                  unsafe_allow_html=True
                  )

        with coly:
              st.write('')
              st.write('')
              st.write('')
              st.write('')
              st.write('')
              
              # Get the Stars, forks and open issues of the selected repository
              stars = df.loc[df['name']==selected_repo, 'stars'].values[0]
              forks = df.loc[df['name']==selected_repo, 'forks'].values[0]
              issues = df.loc[df['name']==selected_repo, 'open_issues'].values[0]

              # Create an attractive rectangular box for the repo owner
              st.markdown(
                  f"""
                  <div style="background-color: #d4edda; padding: 15px; border-radius: 5px; 
                              text-align: center; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
                        <h4 style='color: #28a745; margin: 0;'>Repo Stars</h4>
                        <p style='font-size: 24px; font-weight: bold; margin: 5px 0;'>{stars}</p>
                  </div>
                  """, 
                  unsafe_allow_html=True
            )

              # Create an attractive rectangular box for the repo description
              st.markdown(
                  f"""
                  <div style="background-color: #fce4ec; padding: 15px; border-radius: 5px; 
                              text-align: center; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); margin-top: 15px;">
                        <h4 style='color: #c2185b; margin: 0;'>Repo Forks</h4>
                        <p style='font-size: 20px; margin: 5px 0;'>{forks}</p>
                  </div>
                  """, 
                  unsafe_allow_html=True
            )

              st.markdown(
                  f"""
                  <div style="background-color: #e1f5fe; padding: 15px; border-radius: 5px; 
                              text-align: center; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); margin-top: 15px;">
                        <h4 style='color: #0288d1; margin: 0;'>Open Issues</h4>
                        <p style='font-size: 20px; margin: 5px 0;'>Open Issues: <strong>{issues}</strong></p>
                  </div>
                  """, 
                  unsafe_allow_html=True
            )







            
            


              
              