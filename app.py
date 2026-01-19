import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from functions import *

# Pagewide CSS for visualization
st.markdown("""
    <style>
    .main > div {
        padding-top: 2rem;
    }
    .stMetric {
        background-color: #FADA5E;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)


@st.cache_data
#Cache data for performance optimization
def load_dashboard_data():
    df = pd.read_csv('space_missions.csv')
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Year'] = df['Date'].dt.year
    return df


def main():
    st.title("Isabella's Space Missions Dashboard")
    st.markdown("**Historical Space Mission Analysis (1957 - Present)**")
    st.markdown("---")
    
    # Load data
    try:
        df = load_dashboard_data()
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        st.stop()
    
    # Sidebar filters
    st.sidebar.header("Filters")
    
    # Date range filter
    min_date = df['Date'].min()
    max_date = df['Date'].max()
    
    date_range = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Company filter
    companies = sorted(df['Company'].unique())
    selected_companies = st.sidebar.multiselect(
        "Select Companies",
        options=companies,
        default=companies[:5]  # Default to top 5 for performance
    )
    
    # Mission status filter
    status_options = df['MissionStatus'].unique()
    selected_status = st.sidebar.multiselect(
        "Mission Status",
        options=status_options,
        default=status_options
    )
    
    # Apply filters
    if len(date_range) == 2:
        filtered_df = df[
            (df['Date'] >= pd.to_datetime(date_range[0])) &
            (df['Date'] <= pd.to_datetime(date_range[1]))
        ]
    else:
        filtered_df = df.copy()
    
    if selected_companies:
        filtered_df = filtered_df[filtered_df['Company'].isin(selected_companies)]
    
    if selected_status:
        filtered_df = filtered_df[filtered_df['MissionStatus'].isin(selected_status)]
    
    # Summary Statistics
    st.header("Summary Statistics")
    col1, col2, col3, col4 = st.columns(4)
    
    total_missions = len(filtered_df)
    success_count = len(filtered_df[filtered_df['MissionStatus'] == 'Success'])
    success_rate = (success_count / total_missions * 100) if total_missions > 0 else 0
    unique_companies = filtered_df['Company'].nunique()
    unique_rockets = filtered_df['Rocket'].nunique()
    
    with col1:
        st.metric("Total Missions", f"{total_missions:,}")
    with col2:
        st.metric("Success Rate", f"{success_rate:.1f}%")
    with col3:
        st.metric("Companies", unique_companies)
    with col4:
        st.metric("Rocket Types", unique_rockets)
    
    st.markdown("---")
    
    # Visualizations
    st.header("Data Visualizations")
    
    # Visualization 1: Success Rate Over Time
    st.subheader("1. Mission Success Rate Trends Over Time")
    st.markdown("""
    **Why this visualization?** Understanding how mission success rates have evolved over decades 
    reveals improvements in rocket technology, safety protocols, and engineering practices. 
    This temporal analysis helps identify periods of innovation vs. risk-taking in space exploration.
    """)
    
    # Calculate success rate by year
    yearly_data = filtered_df.groupby('Year').agg({
        'Mission': 'count',
        'MissionStatus': lambda x: (x == 'Success').sum()
    }).reset_index()
    yearly_data.columns = ['Year', 'Total_Missions', 'Successful_Missions']
    yearly_data['Success_Rate'] = (yearly_data['Successful_Missions'] / yearly_data['Total_Missions'] * 100)
    
    fig1 = px.line(
        yearly_data,
        x='Year',
        y='Success_Rate',
        title='Mission Success Rate by Year',
        labels={'Success_Rate': 'Success Rate (%)', 'Year': 'Year'},
        markers=True
    )
    fig1.update_traces(line_color='#1f77b4', line_width=2)
    fig1.update_layout(hovermode='x unified')
    st.plotly_chart(fig1, width='stretch')
    
    # Visualization 2: Top Companies by Mission Count
    st.subheader("2. Top Space Organizations by Launch Volume")
    st.markdown("""
    **Why this visualization?** This comparison reveals which organizations have dominated space access 
    over time. Bar charts effectively show ranking and relative scale, making it easy to identify 
    major players in the commercial and governmental space sectors.
    """)
    
    company_counts = filtered_df['Company'].value_counts().head(15).reset_index()
    company_counts.columns = ['Company', 'Mission_Count']
    
    fig2 = px.bar(
        company_counts,
        x='Mission_Count',
        y='Company',
        orientation='h',
        title='Top 15 Companies by Number of Missions',
        labels={'Mission_Count': 'Number of Missions', 'Company': 'Organization'},
        color='Mission_Count',
        color_continuous_scale='Viridis'
    )
    fig2.update_layout(showlegend=False, yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig2, width='stretch')
    
    # Visualization 3: Mission Status Distribution
    st.subheader("3. Overall Mission Outcome Distribution")
    st.markdown("""
    **Why this visualization?** A pie chart effectively shows the proportion of different outcomes 
    across all missions. This gives stakeholders a quick understanding of overall reliability and 
    risk in space launches - critical for insurance, investment, and safety assessments.
    """)
    
    status_counts = filtered_df['MissionStatus'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Count']
    
    fig3 = px.pie(
        status_counts,
        values='Count',
        names='Status',
        title='Mission Outcomes Distribution',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig3.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig3, width='stretch')
    
    # Visualization 4: Missions Per Year Trend
    st.subheader("4. Global Launch Activity Over Time")
    st.markdown("""
    **Why this visualization?** This area chart shows the volume of space activity across decades, 
    revealing the Space Race peak, post-Cold War decline, and modern commercial space boom. 
    Understanding launch frequency trends is essential for market analysis and capacity planning.
    """)
    
    missions_by_year = filtered_df.groupby('Year').size().reset_index(name='Mission_Count')
    
    fig4 = px.area(
        missions_by_year,
        x='Year',
        y='Mission_Count',
        title='Total Missions Launched Per Year',
        labels={'Mission_Count': 'Number of Missions', 'Year': 'Year'}
    )
    fig4.update_traces(line_color='#2ca02c', fillcolor='rgba(44, 160, 44, 0.3)')
    st.plotly_chart(fig4, width='stretch')
    st.markdown("---")
    
    # Data Table
    st.header("📋 Mission Data Explorer")
    st.markdown("**Interactive table with sorting and searching capabilities**")
    
    # Column selection
    available_columns = list(filtered_df.columns)
    display_columns = st.multiselect(
        "Select columns to display",
        options=available_columns,
        default=['Company', 'Date', 'Mission', 'Rocket', 'MissionStatus', 'Location']
    )
    
    if display_columns:
        display_df = filtered_df[display_columns].copy()
        
        # Format date for better display
        if 'Date' in display_columns:
            display_df['Date'] = display_df['Date'].dt.strftime('%Y-%m-%d')
        
        # Display with sorting
        st.dataframe(
            display_df,
            width='stretch',
            height=400
        )
        
        # Download button
        csv = display_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Filtered Data as CSV",
            data=csv,
            file_name="filtered_space_missions.csv",
            mime="text/csv"
        )
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <p>Data Source: Historical Space Mission Records (1957-Present)</p>
        <p>Built with Streamlit | Designed by Isabella Tochterman</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
